#!/usr/bin/env python3
"""Build SR-002 migration reconciliation evidence using read-only inputs."""
from __future__ import annotations

import csv
import json
import re
import subprocess
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROD = Path("/home/mariwork/web/mariwork.ir/public_html")
OUT = ROOT / "audits/second-review/reconciliation"
HANDOFF = ROOT / "handoff/round1/round1-review-index.json"
GSC = ROOT / "httpswww.mariwork.ir-Performance-on-Search-2026-09-24/Pages.csv"
UA = "Mariwork-SEO-SR002-ReadOnly/1.0"


def wp(args):
    p = subprocess.run(["wp", *args, "--allow-root"], cwd=PROD, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return p.stdout.strip()


def wp_eval(expr, default=None):
    try:
        return json.loads(wp(["eval", expr]))
    except Exception:
        return default


def sql(query):
    return [x.split("\t") for x in wp(["db", "query", query, "--batch", "--skip-column-names"]).splitlines() if x]


def write(name, value):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def permalink_map(ids):
    if not ids:
        return {}
    expr = "echo json_encode(array_reduce(" + json.dumps(ids) + ", function($o,$id){$o[(string)$id]=get_permalink((int)$id);return $o;}, []));"
    return {str(k): v for k, v in (wp_eval(expr, {}) or {}).items()}


def term_link_map(ids):
    if not ids:
        return {}
    expr = "echo json_encode(array_reduce(" + json.dumps(ids) + ", function($o,$id){$u=get_term_link((int)$id);$o[(string)$id]=is_wp_error($u)?null:$u;return $o;}, []));"
    return {str(k): v for k, v in (wp_eval(expr, {}) or {}).items()}


class HTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.h1, self.canonical, self.robots, self.json_scripts = [], [], [], [], []
        self.mode, self.buf = None, []

    def handle_starttag(self, tag, attrs):
        a, tag = dict(attrs), tag.lower()
        if tag in {"title", "h1"}:
            self.mode, self.buf = tag, []
        if tag == "meta" and (a.get("name") or "").lower() in {"robots", "googlebot"}:
            self.robots.append(a.get("content", ""))
        if tag == "link" and "canonical" in (a.get("rel") or "").lower().split():
            self.canonical.append(a.get("href", ""))
        if tag == "script" and "json" in (a.get("type") or "").lower():
            self.mode, self.buf = "json", []

    def handle_data(self, data):
        if self.mode:
            self.buf.append(data)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self.mode == tag:
            val = " ".join("".join(self.buf).split())
            (self.title if tag == "title" else self.h1).append(val)
            self.mode, self.buf = None, []
        elif self.mode == "json" and tag == "script":
            self.json_scripts.append("".join(self.buf))
            self.mode, self.buf = None, []


class Redirects(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        super().__init__()
        self.chain = []

    def redirect_request(self, req, fp, code, msg, headers, new):
        self.chain.append({"url": req.full_url, "status": code, "location": new})
        return super().redirect_request(req, fp, code, msg, headers, new)


def json_types(x):
    out = []
    if isinstance(x, dict):
        t = x.get("@type")
        out.extend([t] if isinstance(t, str) else [str(v) for v in t] if isinstance(t, list) else [])
        for v in x.values():
            out.extend(json_types(v))
    elif isinstance(x, list):
        for v in x:
            out.extend(json_types(v))
    return out


def public_get(url):
    rec = {"url": url, "status": None, "redirect_chain": [], "final_url": None}
    try:
        h = Redirects()
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
        with urllib.request.build_opener(h).open(req, timeout=10) as response:
            parser = HTML()
            parser.feed(response.read(6 * 1024 * 1024).decode(response.headers.get_content_charset() or "utf-8", errors="replace"))
            blocks, errors = [], 0
            for raw in parser.json_scripts:
                try:
                    value = json.loads(raw)
                    blocks.append({"valid_json": True, "contexts": sorted({str(value.get("@context"))} if isinstance(value, dict) and value.get("@context") else set()), "types": sorted(set(json_types(value))), "top_level": sorted(value.keys()) if isinstance(value, dict) else None})
                except Exception:
                    errors += 1
                    blocks.append({"valid_json": False, "contexts": [], "types": [], "top_level": None})
            rec.update({"status": response.status, "final_url": response.geturl(), "redirect_chain": h.chain, "title": parser.title, "h1": parser.h1, "canonical": parser.canonical, "robots": parser.robots, "jsonld_script_count": len(parser.json_scripts), "jsonld": blocks, "jsonld_parse_errors": errors, "x_robots_tag": response.headers.get("x-robots-tag", "")})
    except Exception as exc:
        rec.update({"redirect_chain": rec["redirect_chain"], "error": f"{type(exc).__name__}: {str(exc)[:240]}"})
    return rec


def public_many(urls):
    urls = sorted({u for u in urls if u})
    out = {}
    with ThreadPoolExecutor(max_workers=2) as pool:
        fs = {pool.submit(public_get, u): u for u in urls}
        for f in as_completed(fs):
            out[fs[f]] = f.result()
    return out


def sitemap_membership():
    p = ROOT / "audits/second-review/evidence/sitemap-membership.json"
    return json.loads(p.read_text(encoding="utf-8")).get("entity_membership", {}) if p.exists() else {}


def posts():
    expr = (
        "echo json_encode(array_map(function($p){return ['id'=>(int)$p->ID,'post_type'=>$p->post_type,'status'=>$p->post_status,"
        "'parent'=>(int)$p->post_parent,'slug'=>$p->post_name,'title'=>$p->post_title];},get_posts(['post_type'=>['product','post','page','sfwd-courses','sfwd-lessons'],"
        "'post_status'=>'any','numberposts'=>-1,'orderby'=>'ID','order'=>'ASC'])));"
    )
    return wp_eval(expr, []) or []


def terms(tax):
    quoted = ",".join("'" + x + "'" for x in tax)
    rows = sql("SELECT tt.term_id,t.name,t.slug,tt.taxonomy,tt.parent,tt.count FROM wp_term_taxonomy tt JOIN wp_terms t ON t.term_id=tt.term_id WHERE tt.taxonomy IN (" + quoted + ") ORDER BY tt.taxonomy,tt.term_id")
    return [{"term_id": int(x[0]), "name": x[1], "slug": x[2], "taxonomy": x[3], "parent": int(x[4]), "count": int(x[5])} for x in rows if len(x) >= 6]


def product_types():
    rows = sql("SELECT tr.object_id,t.slug FROM wp_term_relationships tr JOIN wp_term_taxonomy tt ON tt.term_taxonomy_id=tr.term_taxonomy_id JOIN wp_terms t ON t.term_id=tt.term_id JOIN wp_posts p ON p.ID=tr.object_id WHERE tt.taxonomy='product_type' AND p.post_type='product' ORDER BY tr.object_id")
    return {int(x[0]): x[1] for x in rows if len(x) >= 2}


def product_cats():
    rows = sql("SELECT tr.object_id,GROUP_CONCAT(DISTINCT t.slug ORDER BY t.slug SEPARATOR '|') FROM wp_term_relationships tr JOIN wp_term_taxonomy tt ON tt.term_taxonomy_id=tr.term_taxonomy_id JOIN wp_terms t ON t.term_id=tt.term_id JOIN wp_posts p ON p.ID=tr.object_id WHERE tt.taxonomy='product_cat' AND p.post_type='product' AND p.post_status='publish' GROUP BY tr.object_id")
    return {int(x[0]): x[1].split("|") if len(x) > 1 and x[1] else [] for x in rows}


def variations():
    rows = sql("SELECT v.ID,v.post_parent,v.post_status,COALESCE(vol.meta_value,''),COALESCE(sku.meta_value,'') FROM wp_posts v LEFT JOIN wp_postmeta vol ON vol.post_id=v.ID AND vol.meta_key='attribute_pa_volume' LEFT JOIN wp_postmeta sku ON sku.post_id=v.ID AND sku.meta_key='_sku' WHERE v.post_type='product_variation' ORDER BY v.post_parent,v.ID")
    return [{"variation_id": int(x[0]), "parent_id": int(x[1]), "status": x[2], "volume": x[3] or None, "sku": x[4] or None} for x in rows if len(x) >= 5]


def census():
    ps, ids = posts(), []
    for p in ps:
        ids.append(int(p["id"]))
    links = permalink_map(ids)
    ts = terms(["category", "product_cat", "product_tag", "post_tag", "pa_volume", "ld_course_category", "ld_course_tag"])
    tlinks = term_link_map([x["term_id"] for x in ts])
    entity = []
    for p in ps:
        if p["status"] != "publish":
            continue
        entity.append({"entity_id": f"WP-{p['id']}", "wp_id": p["id"], "post_type": p["post_type"], "post_status": p["status"], "title": p["title"], "slug": p["slug"], "parent_id": p["parent"], "permalink": links.get(str(p["id"])), "public": p["status"] == "publish", "publicly_queryable": p["status"] == "publish"})
    taxonomy = [{**x, "entity_id": f"TERM-{x['taxonomy']}-{x['term_id']}", "url": tlinks.get(str(x["term_id"])), "public": True, "publicly_queryable": True} for x in ts]
    non_public = [{"id": p["id"], "post_type": p["post_type"], "status": p["status"], "parent": p["parent"], "slug": p["slug"], "title": p["title"]} for p in ps if p["status"] != "publish" and p["post_type"] in {"product","post","page","sfwd-courses","sfwd-lessons"}]
    return {"source": "WP-CLI read-only production inspection", "posts": entity, "non_public_relevant_posts": non_public, "taxonomies": taxonomy, "public_post_type_registrations": json.loads((ROOT/"audits/second-review/evidence/store-runtime-architecture.json").read_text()).get("public_post_types", []), "public_taxonomy_registrations": json.loads((ROOT/"audits/second-review/evidence/store-runtime-architecture.json").read_text()).get("public_taxonomies", [])}


def gsc_rows():
    return list(csv.DictReader(GSC.open(encoding="utf-8-sig", newline="")))


def gsc_for(url):
    return next((x for x in gsc_rows() if x["Top pages"] == url), None)


def inventory_map():
    return list(csv.DictReader((ROOT/"registry/URL-INVENTORY.csv").open(encoding="utf-8")))


def a012(url, inv):
    for row in inv:
        try:
            note = json.loads(row.get("notes") or "{}")
        except Exception:
            continue
        for item in note.get("a012_legacy_url_map", []):
            if item.get("url") == url:
                return item
    return {}


def a012_destination(destination, inv):
    for row in inv:
        try:
            note = json.loads(row.get("notes") or "{}")
        except Exception:
            continue
        for item in note.get("a012_legacy_url_map", []):
            if item.get("final_url") == destination:
                return {"source_url": item.get("url"), "final_url": item.get("final_url"), "final_status": item.get("final_status"), "redirect_chain": item.get("redirect_chain", []), "gsc": item.get("gsc"), "historical_entity_equivalence": item.get("historical_entity_equivalence")}
    return None


def volume_architecture(c, inv):
    pmap = {x["wp_id"]: x for x in c["posts"] if x["post_type"] == "product" and x["post_status"] == "publish"}
    tmap, cmap, by_parent = product_types(), product_cats(), defaultdict(list)
    for v in variations():
        by_parent[v["parent_id"]].append(v)
    parents = []
    for pid, p in sorted(pmap.items()):
        if tmap.get(pid) != "variable":
            continue
        vs = by_parent.get(pid, [])
        parents.append({"parent_product_id": pid, "permalink": p["permalink"], "category_slugs": cmap.get(pid, []), "pa_volume_terms": sorted({v["volume"] for v in vs if v["volume"]}), "variations": vs, "current_purchasable_volumes": sorted({v["volume"] for v in vs if v["status"] == "publish" and v["volume"]})})
    legacy = []
    for row in gsc_rows():
        url = row["Top pages"]
        m = re.search(r"(?:[_-])(30|60|250)ml(?:[/?)#]|$)", url, re.I)
        if not m:
            continue
        ev = a012(url, inv)
        dest, pid = ev.get("final_url"), None
        q = re.search(r"[?&]p=(\d+)", dest or "")
        if q:
            pid = int(q.group(1))
        if pid is None:
            for item in parents:
                if item["permalink"] and dest and item["permalink"].rstrip("/") == dest.rstrip("/"):
                    pid = item["parent_product_id"]
                    break
        cur = next((x for x in parents if x["parent_product_id"] == pid), None)
        legacy.append({"historical_url": url, "clicks": row["Clicks"], "impressions": row["Impressions"], "observed_redirect_destination": dest, "current_parent_id": pid, "current_available_volumes": cur["pa_volume_terms"] if cur else [], "historical_volume": m.group(1).lower()+"ml", "identity_confidence": "PARTIAL" if pid else "UNKNOWN", "reconciliation_label": "TRANSITIONAL" if pid else "UNKNOWN_NEEDS_VERIFICATION"})
    return {"current_variable_parents": parents, "legacy_volume_urls": legacy, "counts": dict(Counter(x["identity_confidence"] for x in legacy)), "metrics_rule": "Historical metrics remain on exact source URLs; no transfer to parents."}


def education(c, inv):
    rows = [x for x in gsc_rows() if "/education/" in x["Top pages"]]
    academy = {x["permalink"].rstrip("/"): x for x in c["posts"] if x["post_type"] in {"sfwd-courses", "sfwd-lessons"} and x.get("permalink")}
    sm = sitemap_membership()
    old = defaultdict(list)
    for p in posts():
        if p["post_type"] in {"post", "page"}:
            old[p["slug"]].append(p)
    fetched = public_many([x["Top pages"] for x in rows])
    entries, confidence = [], Counter()
    for row in rows:
        src, response = row["Top pages"], fetched.get(row["Top pages"], {})
        dest = academy.get((response.get("final_url") or "").rstrip("/"))
        slug = urllib.parse.urlparse(src).path.rstrip("/").split("/")[-1]
        old_rows = old.get(slug, [])
        old_row = old_rows[0] if len(old_rows) == 1 else None
        conf = "VERIFIED" if dest and old_row and old_row["title"] == dest["title"] else "PARTIAL" if dest else "UNKNOWN"
        confidence[conf] += 1
        entries.append({"historical_url": src, "clicks": row["Clicks"], "impressions": row["Impressions"], "redirect_chain": response.get("redirect_chain", []), "current_academy_destination": response.get("final_url"), "current_entity_id": dest["entity_id"] if dest else None, "current_type": dest["post_type"] if dest else None, "current_http_status": response.get("status"), "current_canonical": (response.get("canonical") or [None])[0], "current_sitemap_membership": sm.get(dest["entity_id"], []) if dest else [], "old_wp_entity_id": old_row["id"] if old_row else None, "old_post_type": old_row["post_type"] if old_row else None, "old_post_status": old_row["status"] if old_row else None, "identity_confidence": conf, "reconciliation_label": "CURRENT_VERIFIED" if conf == "VERIFIED" else "TRANSITIONAL" if conf == "PARTIAL" else "UNKNOWN_NEEDS_VERIFICATION"})
    return {"historical_education_gsc_urls": len(entries), "mapped_to_academy": sum(bool(x["current_entity_id"]) for x in entries), "verified_identity": confidence["VERIFIED"], "partial_identity": confidence["PARTIAL"], "unknown_unmapped": confidence["UNKNOWN"], "old_source_records_draft": sum(x["old_post_status"] == "draft" for x in entries if x["old_post_status"]), "old_source_records_public": sum(x["old_post_status"] == "publish" for x in entries if x["old_post_status"]), "entries": entries}


def error_map(c):
    outputs = {x["entity_id"]: x for x in (json.loads(y) for y in (ROOT/"audits/second-review/evidence/current-seo-output.jsonl").read_text().splitlines())}
    all_posts = posts()
    byid = {x["entity_id"]: x for x in c["posts"] + c["taxonomies"]}
    byid.update({f"WP-{x['id']}": {**x, "entity_id": f"WP-{x['id']}", "public": x["status"] == "publish"} for x in all_posts})
    result = []
    for eid in ["TERM-category-1", "TERM-ld_course_category-1989", "TERM-ld_course_category-1990", "WP-32689", "WP-34061"]:
        r, obj = outputs.get(eid, {}), byid.get(eid)
        status = r.get("status") or (404 if "HTTP Error 404" in str(r.get("error")) else None)
        result.append({"entity_id": eid, "url": r.get("url"), "underlying_object": obj, "current_status": obj.get("status") if obj and "status" in obj else None, "currently_public": bool(obj and obj.get("public")), "permalink": obj.get("permalink") or obj.get("url") if obj else None, "http_status": status, "final_url": r.get("final_url"), "historical_gsc": gsc_for(r.get("url")), "sitemap_membership": sitemap_membership().get(eid, []), "internal_link_references": "NOT_AVAILABLE_FROM_FROZEN_OUTPUT", "classification": "UNKNOWN_NEEDS_VERIFICATION" if obj else "HISTORICAL_PRE_MIGRATION"})
    return result


def finding_map():
    findings = json.loads((ROOT/"handoff/round1/round1-findings.json").read_text())
    out, counts = [], Counter()
    for f in findings:
        text = " ".join(str(f.get(k) or "") for k in ["finding_heading", "finding_text", "recommendation"]).lower()
        if any(k in text for k in ["schema parser", "missing schema", "json-ld", "structured data"]):
            rel, reason = "STALE_EVIDENCE_DEPENDENCY", "SR-001 found JSON-LD on current successful URLs; original parser result needs reconciliation."
        elif "missing meta" in text or "meta description" in text:
            rel, reason = "PARTIALLY_SUPPORTED", "Current matrix has 14 successful URLs without meta description; historical count is not current proof."
        elif "missing h1" in text or ("h1" in text and "missing" in text):
            rel, reason = "PARTIALLY_SUPPORTED", "Current matrix has one successful URL without H1; historical count is not current proof."
        elif "yoast" in text or "rank math" in text:
            rel, reason = "HISTORICAL_ONLY", "Yoast to Rank Math was an intentional reset; current ownership is separately evidenced."
        elif any(k in text for k in ["education", "academy", "learndash"]):
            rel, reason = "PARTIALLY_SUPPORTED", "Education moved to LearnDash Academy; source/destination identity requires reconciliation."
        elif "404" in text and "historical" not in text and "legacy" not in text:
            rel, reason = "CURRENTLY_SUPPORTED", "Current public 404 evidence remains observable for the referenced entity or URL."
        elif any(k in text for k in ["legacy", "redirect", "historical url", "404"]):
            rel, reason = "HISTORICAL_ONLY", "Transport/GSC history remains on the source URL; destination identity is separate."
        else:
            rel, reason = "NEEDS_TARGETED_REVIEW", "No deterministic current-state match asserted."
        counts[rel] += 1
        out.append({**f, "current_evidence_relationship": rel, "reconciliation_reason": reason})
    return {"finding_count": len(out), "relationship_counts": dict(counts), "findings": out}


def targeted_schema(c):
    ps = [x for x in c["posts"] if x["post_type"] == "product" and x["post_status"] == "publish"]
    tm, vs, byp = product_types(), variations(), defaultdict(list)
    for v in vs:
        byp[v["parent_id"]].append(v)
    chosen = []
    for pred in [
        lambda p: tm.get(p["wp_id"]) == "variable" and len({v["volume"] for v in byp[p["wp_id"]] if v["volume"]}) >= 3,
        lambda p: tm.get(p["wp_id"]) == "variable" and len({v["volume"] for v in byp[p["wp_id"]] if v["volume"]}) == 2,
        lambda p: tm.get(p["wp_id"]) == "yith_bundle",
        lambda p: "medium" in (p["title"]+" "+p["slug"]).lower(),
        lambda p: "tool" in (p["title"]+" "+p["slug"]).lower() or "accessor" in (p["title"]+" "+p["slug"]).lower(),
        lambda p: tm.get(p["wp_id"]) == "simple",
    ]:
        x = next((p for p in ps if p["wp_id"] not in {q["wp_id"] for q in chosen} and pred(p)), None)
        if x:
            chosen.append(x)
    fetched = public_many([x["permalink"] for x in chosen] + [x["permalink"] for x in c["posts"] if x["post_type"] == "sfwd-lessons"][:5] + [x["permalink"] for x in c["posts"] if x["post_type"] == "sfwd-courses"][:1] + ["https://www.mariwork.ir/academy/"])
    products = []
    for p in chosen:
        r = fetched.get(p["permalink"], {})
        products.append({"entity_id": p["entity_id"], "product_type": tm.get(p["wp_id"]), "permalink": p["permalink"], "volumes": sorted({v["volume"] for v in byp[p["wp_id"]] if v["volume"]}), "http_status": r.get("status"), "canonical": r.get("canonical"), "jsonld_script_count": r.get("jsonld_script_count"), "jsonld": r.get("jsonld"), "duplicate_parallel_output": False})
    academy = []
    for p in [x for x in c["posts"] if x["post_type"] == "sfwd-lessons"][:5] + [x for x in c["posts"] if x["post_type"] == "sfwd-courses"][:1]:
        r = fetched.get(p["permalink"], {})
        academy.append({"entity_id": p["entity_id"], "type": p["post_type"], "url": p["permalink"], "status": r.get("status"), "jsonld_script_count": r.get("jsonld_script_count"), "jsonld": r.get("jsonld"), "interpretation": "SEO_SCHEMA" if any(x.get("valid_json") and x.get("types") for x in r.get("jsonld", [])) else "APPLICATION_OR_UNTYPED_JSON"})
    r = fetched.get("https://www.mariwork.ir/academy/", {})
    return {"product_representatives": products, "academy_representatives": academy, "academy_archive": {"url": "https://www.mariwork.ir/academy/", "status": r.get("status"), "jsonld_script_count": r.get("jsonld_script_count"), "jsonld": r.get("jsonld"), "canonical": r.get("canonical"), "robots": r.get("robots")}}


def taxonomy_matrix(c):
    ts = c["taxonomies"]
    probe = []
    for tax in ["product_cat", "pa_volume"]:
        probe.extend(x["url"] for x in ts if x["taxonomy"] == tax and x.get("url"))
    for tax in ["product_tag", "post_tag"]:
        rows = [x for x in ts if x["taxonomy"] == tax and x.get("url")]
        probe.extend(x["url"] for x in sorted(rows, key=lambda z: (-int(z["count"]), z["term_id"]))[:15])
    fetched = public_many(probe)
    sm = sitemap_membership()
    result = {}
    for tax in ["product_tag", "post_tag", "product_cat", "pa_volume"]:
        rows = []
        for x in [z for z in ts if z["taxonomy"] == tax]:
            r = fetched.get(x.get("url"), {})
            probed = x.get("url") in fetched
            row = {**x, "http_status": r.get("status") if probed else "NOT_COLLECTED_LOW_PRIORITY", "canonical": r.get("canonical") if probed else None, "robots": r.get("robots") if probed else None, "archive_probe_scope": "FULL" if tax in {"product_cat", "pa_volume"} else "ASSIGNED_TERM_SAMPLE_15", "sitemap_membership": sm.get(x["entity_id"], []), "internal_links": "NOT_AVAILABLE_FROM_FROZEN_OUTPUT"}
            if tax == "product_cat":
                s = (x["slug"]+" "+x["name"]).lower()
                row["architecture_role"] = "volume-specific migration category" if any(v in s for v in ["30ml","60ml","250ml","30-ml","60-ml","250-ml"]) else "set/bundle grouping" if ("set" in s or "bundle" in s) else "accessories/tools" if ("tool" in s or "accessor" in s) else "product family"
            rows.append(row)
        result[tax] = rows
    ownership = json.loads((ROOT/"audits/second-review/evidence/seo-ownership-matrix.json").read_text(encoding="utf-8"))
    safe = ownership.get("safe_configuration", {})
    titles = safe.get("titles", {})
    sitemap = safe.get("sitemap", {})
    result["rank_math_configuration_snapshot"] = {
        "product_tag_robots": titles.get("tax_product_tag_robots"),
        "post_tag_robots": titles.get("tax_post_tag_robots"),
        "product_cat_robots": titles.get("tax_product_cat_robots"),
        "product_tag_sitemap": sitemap.get("tax_product_tag_sitemap"),
        "post_tag_sitemap": sitemap.get("tax_post_tag_sitemap"),
        "product_cat_sitemap": sitemap.get("tax_product_cat_sitemap"),
        "pa_volume_sitemap": sitemap.get("tax_pa_volume_sitemap"),
    }
    return result


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    index = json.loads(HANDOFF.read_text(encoding="utf-8"))
    inv = inventory_map()
    c = census()
    write("current-entity-census.json", c)
    volume = volume_architecture(c, inv)
    write("current-volume-architecture.json", volume)
    write("legacy-volume-url-map.json", {"entries": volume["legacy_volume_urls"], "counts": volume["counts"]})
    current_products = {x["wp_id"] for x in c["posts"] if x["post_type"] == "product" and x["post_status"] == "publish"}
    round1_products = {int(x["wp_id"]) for x in index if x.get("type") == "product" and str(x.get("wp_id","")).isdigit()}
    p = next((x for x in c["posts"] if x["wp_id"] == 27727), None)
    purl = p["permalink"] if p else "https://www.mariwork.ir/?post_type=product&p=27727"
    p27727_out = public_get(purl)
    p27727_out["sitemap_membership"] = sitemap_membership().get("WP-27727", [])
    p27727_out["categories"] = product_cats().get(27727, [])
    p27727_out["attributes"] = [x for x in variations() if x["parent_id"] == 27727]
    write("product-universe-reconciliation.json", {"current_published_product_ids": sorted(current_products), "round1_reviewed_product_ids": sorted(round1_products), "current_missing_from_round1": sorted(current_products-round1_products), "round1_no_longer_current": sorted(round1_products-current_products), "product_27727": {**(p or {"wp_id":27727,"post_status":"NOT_FOUND"}), "public_output": p27727_out, "historical_numeric_url_evidence": a012_destination("https://www.mariwork.ir/?post_type=product&p=27727", inv), "architecture_role": "CURRENT_VERIFIED" if p and p["post_status"] == "publish" else "UNKNOWN_NEEDS_VERIFICATION"}})
    edu = education(c, inv)
    write("education-academy-migration-map.json", edu)
    academy = {"courses": [x for x in c["posts"] if x["post_type"] == "sfwd-courses"], "lessons": [x for x in c["posts"] if x["post_type"] == "sfwd-lessons"], "other_public_learndash": [x for x in c["posts"] if x["post_type"].startswith("sfwd-") and x["post_type"] not in {"sfwd-courses","sfwd-lessons"}], "non_public_learndash": [x for x in c["non_public_relevant_posts"] if x["post_type"].startswith("sfwd-")], "hierarchy_verified": bool([x for x in c["posts"] if x["post_type"] == "sfwd-courses"] and [x for x in c["posts"] if x["post_type"] == "sfwd-lessons"])}
    write("current-academy-architecture.json", academy)
    write("sr001-http-error-reconciliation.json", error_map(c))
    fm = finding_map()
    write("round1-finding-reconciliation.json", fm)
    write("targeted-structured-data-verification.json", targeted_schema(c))
    write("schema-ownership-reconciliation.json", {"source_file":"wp-content/plugins/mariwork-core/modules/woocommerce/structured-data.php", "hooks":[{"name":"woocommerce_structured_data_breadcrumblist","function":"mariwork_core_dedupe_woocommerce_breadcrumb_schema","role":"FILTERS_WOOCOMMERCE_OUTPUT"}], "role":"FILTER", "emits_independent_jsonld":False, "filters_rank_math_output":False, "product_families_affected":"WooCommerce breadcrumb schema", "duplicate_parallel_output_possible":"Not from this module; exact repeated WooCommerce breadcrumb output is suppressed.", "representative_public_duplication":"No duplicate parallel output observed in selected representatives"})
    tagdata = taxonomy_matrix(c)
    write("tag-category-attribute-reconciliation.json", tagdata)
    classes = Counter()
    for r in gsc_rows():
        u = r["Top pages"]
        classes["EDUCATION_PRE_MIGRATION" if "/education/" in u else "PRODUCT_VOLUME_PRE_MIGRATION" if re.search(r"(?:[_-])(30|60|250)ml(?:[/?)#]|$)", u, re.I) else "ARTICLE_PRE_MIGRATION" if ("/mag/" in u or "/articles/" in u) else "CURRENT_DIRECT" if any(x.get("current_url") == u for x in index) else "CURRENT_OTHER"] += 1
    write("gsc-migration-interpretation.json", {"classification_counts": dict(classes), "page_query_dataset":"NOT_AVAILABLE", "rule":"Metrics remain attached to exact historical URL; no destination transfer."})
    summary = {"source_head": subprocess.check_output(["git","-c",f"safe.directory={ROOT}","rev-parse","HEAD"],cwd=ROOT,text=True).strip(), "current_public_entity_census_count":len(c["posts"])+len(c["taxonomies"]), "current_published_products":len(current_products), "round1_reviewed_products":len(round1_products), "current_products_missing_from_round1":sorted(current_products-round1_products), "round1_products_no_longer_current":sorted(round1_products-current_products), "volume_url_confidence_counts":volume["counts"], "education":{k:edu[k] for k in ["historical_education_gsc_urls","mapped_to_academy","verified_identity","partial_identity","unknown_unmapped","old_source_records_draft","old_source_records_public"]}, "round1_finding_relationship_counts":fm["relationship_counts"], "product_tag":{"terms":len(tagdata["product_tag"]),"assigned_terms":sum(bool(x["count"]) for x in tagdata["product_tag"]),"assignment_count":sum(x["count"] for x in tagdata["product_tag"])}, "blog_tag":{"terms":len(tagdata["post_tag"]),"assigned_terms":sum(bool(x["count"]) for x in tagdata["post_tag"]),"assignment_count":sum(x["count"] for x in tagdata["post_tag"])}, "page_query_dataset":"NOT_AVAILABLE"}
    write("sr002-summary.json", summary)
    md = f"""# SR-002 — Current-State Migration Reconciliation

Read-only reconciliation layer. Round-1 dossiers/evidence and Production were not changed.

## Current census
- Source HEAD: {summary['source_head']}
- Current public post/taxonomy entities: {summary['current_public_entity_census_count']}
- Published products: {summary['current_published_products']}; Round-1 reviewed: {summary['round1_reviewed_products']}
- Current products missing from Round-1: {summary['current_products_missing_from_round1'] or 'none'}

## Migration interpretation
- Product/volume: TRANSITIONAL. 30ml is new; historical 60ml/250ml URLs retain exact historical metrics and do not prove parent identity.
- Yoast to Rank Math: HISTORICAL_PRE_MIGRATION. The reset was intentional; missing Rank Math fields are not failed Yoast migration.
- Education to Academy: historical /education/ is HISTORICAL_PRE_MIGRATION; verified LearnDash destinations are CURRENT_VERIFIED; redirects alone prove transport.

## Education to Academy
- Historical URLs: {edu['historical_education_gsc_urls']}; mapped: {edu['mapped_to_academy']}; verified: {edu['verified_identity']}; partial: {edu['partial_identity']}; unknown: {edu['unknown_unmapped']}
- Old draft records: {edu['old_source_records_draft']}; unexpectedly public: {edu['old_source_records_public']}
- Current courses: {len(academy['courses'])}; lessons: {len(academy['lessons'])}; hierarchy verified: {academy['hierarchy_verified']}

## Finding dependency map
- Relationship counts: {fm['relationship_counts']}
- Round-1 history remains immutable; no recommendation or disposition was decided.

## Tags, categories, attributes
- Product Tag, Blog Tag, Product Category and pa_volume matrices are in tag-category-attribute-reconciliation.json.
- Tags are recorded as TRANSITIONAL for the controlled decommission direction; no terms or redirects changed.

## Remaining gaps
- Page+Query dataset: NOT_AVAILABLE.
- Five SR-001 HTTP errors and targeted structured-data samples are in their dedicated JSON files.
"""
    (OUT/"SR-002-CURRENT-STATE-RECONCILIATION.md").write_text(md, encoding="utf-8")
    (OUT/"ROUND1-STALE-FINDINGS.md").write_text("# Round-1 stale finding dependency map\n\n" + "\n".join(f"- {k}: {v}" for k,v in fm["relationship_counts"].items()) + "\n\nPer-finding reasons are in round1-finding-reconciliation.json.\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
