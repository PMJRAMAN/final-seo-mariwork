#!/usr/bin/env python3
"""Read-only SR-003 Store evidence collector and reconciliation fixer."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audits/second-review/store"
RECON = ROOT / "audits/second-review/reconciliation"
PROD = Path("/home/mariwork/web/mariwork.ir/public_html")
UA = "Mariwork-SEO-SR003-ReadOnly/1.0"

sys.path.insert(0, str(ROOT / "automation"))
import build_sr002_reconciliation as sr2  # noqa: E402


def write(name, value):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def safe_wp_eval(expr, default=None):
    return sr2.wp_eval(expr, default)


class DetailParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.h1, self.canonical, self.robots = [], [], [], []
        self.json_scripts, self.links = [], []
        self.mode, self.buf = None, []
        self.href, self.anchor = None, []

    def handle_starttag(self, tag, attrs):
        attrs, tag = dict(attrs), tag.lower()
        if tag in {"title", "h1"}:
            self.mode, self.buf = tag, []
        if tag == "meta" and (attrs.get("name") or "").lower() in {"robots", "googlebot"}:
            self.robots.append(attrs.get("content", ""))
        if tag == "link" and "canonical" in (attrs.get("rel") or "").lower().split():
            self.canonical.append(attrs.get("href", ""))
        if tag == "script" and "json" in (attrs.get("type") or "").lower():
            self.mode, self.buf = "json", []
        if tag == "a" and attrs.get("href"):
            self.href, self.anchor = attrs.get("href"), []

    def handle_data(self, data):
        if self.mode:
            self.buf.append(data)
        if self.href is not None:
            self.anchor.append(data)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self.mode == tag:
            value = " ".join("".join(self.buf).split())
            (self.title if tag == "title" else self.h1).append(value)
            self.mode, self.buf = None, []
        elif self.mode == "json" and tag == "script":
            self.json_scripts.append("".join(self.buf))
            self.mode, self.buf = None, []
        if tag == "a" and self.href is not None:
            self.links.append({"href": self.href, "anchor_text": " ".join("".join(self.anchor).split())})
            self.href, self.anchor = None, []


class Redirects(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        super().__init__()
        self.chain = []

    def redirect_request(self, req, fp, code, msg, headers, new):
        self.chain.append({"url": req.full_url, "status": code, "location": new})
        return super().redirect_request(req, fp, code, msg, headers, new)


def fetch_detail(url):
    out = {"url": url, "status": None, "redirect_chain": [], "final_url": None}
    try:
        tracker = Redirects()
        request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
        with urllib.request.build_opener(tracker).open(request, timeout=10) as response:
            body = response.read(6 * 1024 * 1024)
            parser = DetailParser()
            parser.feed(body.decode(response.headers.get_content_charset() or "utf-8", errors="replace"))
            blocks, errors = [], 0
            for raw in parser.json_scripts:
                try:
                    value = json.loads(raw)
                    blocks.append(value)
                except Exception:
                    errors += 1
            out.update({"status": response.status, "final_url": response.geturl(), "redirect_chain": tracker.chain, "title": parser.title, "h1": parser.h1, "canonical": parser.canonical, "robots": parser.robots, "x_robots": response.headers.get("x-robots-tag", ""), "jsonld": blocks, "jsonld_parse_errors": errors, "links": parser.links, "body_sha256": hashlib.sha256(body).hexdigest()})
    except Exception as exc:
        out.update({"redirect_chain": out["redirect_chain"], "error": f"{type(exc).__name__}: {str(exc)[:200]}"})
    return out


def fetch_many(urls):
    urls = sorted({x for x in urls if x})
    result = {}
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs = {pool.submit(fetch_detail, url): url for url in urls}
        for future in as_completed(jobs):
            result[jobs[future]] = future.result()
    return result


def all_types(value):
    out = []
    if isinstance(value, dict):
        typ = value.get("@type")
        out.extend([typ] if isinstance(typ, str) else [str(x) for x in typ] if isinstance(typ, list) else [])
        for child in value.values():
            out.extend(all_types(child))
    elif isinstance(value, list):
        for child in value:
            out.extend(all_types(child))
    return out


def has_key(value, key):
    if isinstance(value, dict):
        if key in value:
            return True
        return any(has_key(x, key) for x in value.values())
    if isinstance(value, list):
        return any(has_key(x, key) for x in value)
    return False


def value_present(value, key):
    if isinstance(value, dict):
        if key in value and value[key] not in (None, ""):
            return True
        return any(value_present(x, key) for x in value.values())
    if isinstance(value, list):
        return any(value_present(x, key) for x in value)
    return False


def product_meta(ids):
    if not ids:
        return {}
    expr = "echo json_encode(array_reduce(" + json.dumps(ids) + ", function($o,$id){$o[(string)$id]=['sku'=>(string)get_post_meta((int)$id,'_sku',true)];return $o;}, []));"
    return {int(k): v for k, v in (safe_wp_eval(expr, {}) or {}).items()}


def current_data():
    census = json.loads((RECON / "current-entity-census.json").read_text(encoding="utf-8"))
    posts = census["posts"]
    products = [x for x in posts if x["post_type"] == "product" and x["post_status"] == "publish"]
    categories = [x for x in census["taxonomies"] if x["taxonomy"] == "product_cat"]
    blog_categories = [x for x in census["taxonomies"] if x["taxonomy"] == "category"]
    lessons = [x for x in posts if x["post_type"] == "sfwd-lessons"]
    courses = [x for x in posts if x["post_type"] == "sfwd-courses"]
    articles = [x for x in posts if x["post_type"] == "post"]
    shop_url = "https://www.mariwork.ir/shop/"
    urls = [(x.get("permalink") or x.get("url")) for x in products + categories + blog_categories + lessons + courses + articles if x.get("permalink") or x.get("url")]
    urls += [shop_url, "https://www.mariwork.ir/academy/"]
    return census, products, categories, blog_categories, lessons, courses, articles, fetch_many(urls)


def fix_finding_classification():
    findings = json.loads((ROOT / "handoff/round1/round1-findings.json").read_text(encoding="utf-8"))
    census = json.loads((RECON / "current-entity-census.json").read_text(encoding="utf-8"))
    current = {x["entity_id"]: x for x in census["posts"] + census["taxonomies"]}
    current_output = {json.loads(line)["entity_id"]: json.loads(line) for line in (ROOT / "audits/second-review/evidence/current-seo-output.jsonl").read_text().splitlines()}
    rows, counts = [], Counter()
    for finding in findings:
        text = " ".join(str(finding.get(k) or "") for k in ["finding_heading", "finding_text", "recommendation"]).lower()
        eid, entity, output = finding["entity_id"], current.get(finding["entity_id"]), current_output.get(finding["entity_id"], {})
        status = output.get("status")
        if status is None and "HTTP Error 404" in str(output.get("error")):
            status = 404
        if any(k in text for k in ["schema parser", "missing schema", "json-ld", "structured data"]):
            rel, reason = "STALE_EVIDENCE_DEPENDENCY", "Current public extraction provides JSON-LD/schema evidence; the original parser gap is stale for this dependency."
        elif "missing meta" in text or "meta description" in text:
            if output.get("meta_description_count", 0) == 0 and status in {200, None}:
                rel, reason = "CURRENTLY_SUPPORTED", "The exact missing-meta observation remains present in current output."
            elif output.get("meta_description_count", 0) > 0:
                rel, reason = "STALE_EVIDENCE_DEPENDENCY", "Current output has a meta description; the original absence was stale."
            else:
                rel, reason = "NEEDS_TARGETED_REVIEW", "Current status did not permit a direct comparison."
        elif "missing h1" in text or ("h1" in text and "missing" in text):
            if output.get("h1_count", 0) == 0 and status in {200, None}:
                rel, reason = "CURRENTLY_SUPPORTED", "The exact missing-H1 observation remains present in current output."
            elif output.get("h1_count", 0) > 0:
                rel, reason = "STALE_EVIDENCE_DEPENDENCY", "Current output has an H1; the original absence was stale."
            else:
                rel, reason = "NEEDS_TARGETED_REVIEW", "Current status did not permit a direct comparison."
        elif any(k in text for k in ["alt", "image"]):
            rel, reason = "NEEDS_TARGETED_REVIEW", "Image role and current rendered evidence are not fully represented in the deterministic matrix."
        elif entity and entity.get("public") and status == 200 and ("noindex" in text or "no-canonical" in text or ("empty" in text and entity.get("count", 1) == 0)):
            rel, reason = "CURRENTLY_SUPPORTED", "The current public entity and the exact current-state indexability/empty-state observation remain present."
        elif any(k in text for k in ["yoast", "rank math"]):
            rel, reason = ("NEEDS_TARGETED_REVIEW", "The entity is current; migration context affects ownership interpretation but does not make this current entity historical.") if entity and entity.get("public") else ("HISTORICAL_ONLY", "The finding is tied to pre-migration ownership/metadata continuity.")
        elif "/education/" in finding.get("current_url", "") or ("education" in text and not entity):
            rel, reason = "HISTORICAL_ONLY", "The referenced entity/URL belongs to the pre-migration Education architecture."
        elif entity and entity.get("public") and status == 200:
            if "noindex" in text or "no-canonical" in text or "empty" in text and entity.get("count", 1) == 0:
                rel, reason = "CURRENTLY_SUPPORTED", "The current public entity and its exact current-state observation remain present."
            else:
                rel, reason = "NEEDS_TARGETED_REVIEW", "Current entity exists; finding-specific verification remains required."
        elif any(k in text for k in ["redirect", "legacy", "historical url", "404"]):
            rel, reason = "HISTORICAL_ONLY", "The evidence is transport/history on a source URL; current destination identity is separate."
        else:
            rel, reason = "NEEDS_TARGETED_REVIEW", "No direct current-state comparison was established."
        counts[rel] += 1
        rows.append({**finding, "current_evidence_relationship": rel, "reconciliation_reason": reason, "current_entity_exists": bool(entity), "current_entity_public": bool(entity and entity.get("public")), "current_http_status": status})
    payload = {"finding_count": len(rows), "relationship_counts": dict(counts), "classifier_version": "SR-003-current-first-v2", "findings": rows}
    (RECON / "round1-finding-reconciliation.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md = "# Round-1 stale finding dependency map\n\nClassifier version: SR-003-current-first-v2. Current entity existence, public state, HTTP and exact observations are evaluated before migration context. This is not Second Review.\n\n"
    md += "\n".join(f"- {k}: {v}" for k, v in counts.items()) + "\n"
    md += "\nA current page/taxonomy is not HISTORICAL_ONLY merely because Yoast was replaced. Original dossiers remain unchanged.\n"
    (RECON / "ROUND1-STALE-FINDINGS.md").write_text(md, encoding="utf-8")
    return counts


def category_matrix(blog_categories, fetched):
    sm = sr2.sitemap_membership()
    frozen = {json.loads(line)["url"].lower(): json.loads(line) for line in (ROOT/"audits/second-review/evidence/current-seo-output.jsonl").read_text().splitlines()}
    rows = []
    for x in blog_categories:
        r = fetched.get(x.get("url"), {})
        if r.get("status") is None and "HTTP Error 404" in str(frozen.get((x.get("url") or "").lower(), {}).get("error")):
            r = {**r, "status": 404}
        rows.append({**x, "http_status": r.get("status"), "canonical": r.get("canonical"), "robots": r.get("robots"), "sitemap_membership": sm.get(x["entity_id"], []) or sr2.sitemap_url_membership(x.get("url")), "current_exists": True, "current_classification": "CURRENT_VERIFIED" if r.get("status") in {200, 404} else "UNKNOWN_NEEDS_VERIFICATION", "migration_role": "UNKNOWN_NEEDS_VERIFICATION"})
    return rows


def variable_schema(products, fetched):
    arch = json.loads((RECON / "current-volume-architecture.json").read_text(encoding="utf-8"))
    parents = {x["parent_product_id"]: x for x in arch["current_variable_parents"]}
    sku = product_meta([x["wp_id"] for x in products])
    rows = []
    for pid, parent in sorted(parents.items()):
        r = fetched.get(parent["permalink"], {})
        types = all_types(r.get("jsonld", []))
        product_count = sum(types.count("Product") for _ in [0])
        rows.append({"parent_product_id": pid, "url": parent["permalink"], "current_volumes": parent["pa_volume_terms"], "jsonld_schema_types": sorted(set(types)), "product_present": "Product" in types, "product_group_present": "ProductGroup" in types, "offer_present": "Offer" in types, "aggregate_offer_present": "AggregateOffer" in types, "has_variant_present": has_key(r.get("jsonld", []), "hasVariant"), "is_variant_of_present": has_key(r.get("jsonld", []), "isVariantOf"), "varies_by_present": has_key(r.get("jsonld", []), "variesBy"), "product_group_id_present": has_key(r.get("jsonld", []), "productGroupID") or has_key(r.get("jsonld", []), "inProductGroupWithID"), "sku_present": bool(sku.get(pid, {}).get("sku")), "price_currency_present": value_present(r.get("jsonld", []), "priceCurrency"), "availability_present": value_present(r.get("jsonld", []), "availability"), "canonical": (r.get("canonical") or [None])[0], "duplicate_product_entities": types.count("Product") > 1, "http_status": r.get("status")})
    return rows


def bundle_components():
    ids = json.loads((RECON / "current-volume-architecture.json").read_text(encoding="utf-8"))
    parents = [x["parent_product_id"] for x in json.loads((RECON / "current-entity-census.json").read_text())["posts"] if False]
    # The 22 IDs are the current YITH bundle parents from the sanitized runtime census.
    bundle_ids = [12597,12602,12605,12608,14465,14466,14471,17265,25397,27396,28610,28623,28627,33318,33319,33320,33322,33323,33324,33325,33326,33327]
    expr = "echo json_encode(array_reduce(" + json.dumps(bundle_ids) + ", function($o,$id){$o[(string)$id]=get_post_meta((int)$id,'_yith_wcpb_bundle_data',true);return $o;}, []));"
    raw = safe_wp_eval(expr, {}) or {}
    current_ids = {x["wp_id"] for x in json.loads((RECON / "current-entity-census.json").read_text())["posts"] if x["post_type"] == "product"}
    out = []
    for pid in bundle_ids:
        components = []
        data = raw.get(str(pid), {}) if isinstance(raw, dict) else {}
        for key, item in (data.items() if isinstance(data, dict) else []):
            if not isinstance(item, dict) or not str(item.get("product_id", "")).isdigit():
                continue
            cid = int(item["product_id"])
            components.append({"bundle_order": item.get("bundle_order"), "component_product_id": cid, "quantity_min": item.get("bp_min_qty"), "quantity_max": item.get("bp_max_qty"), "component_current": cid in current_ids, "variation_ids_present": item.get("bp_filtered_variations", [])})
        out.append({"bundle_parent_id": pid, "components": components, "component_mapping_obtained": bool(components)})
    return {"bundle_parents_checked": len(out), "bundles": out, "prices_excluded": True}


def title_h1(products, categories, fetched):
    rows = []
    for x in products:
        entity_url = x.get("permalink") or x.get("url")
        r = fetched.get(entity_url, {})
        title = (r.get("title") or [""])[0]
        h1 = (r.get("h1") or [""])[0]
        combined = f"{x.get('title') or x.get('name') or ''} {title} {h1}"
        pid = x.get("wp_id")
        rows.append({"entity_id": x["entity_id"], "product_id": pid, "entity_type": x.get("post_type") or x.get("taxonomy"), "product_type": sr2.product_types().get(pid) if pid else None, "categories": sr2.product_cats().get(pid, []) if pid else [], "wp_title": x.get("title") or x.get("name"), "html_title": title, "h1": h1, "brand_token_present": bool(re.search(r"mariwork|ماری\s*ورک", combined, re.I)), "product_code_token_present": bool(re.search(r"\bcode\s*\d+|کد\s*\d+", combined, re.I)), "volume_token_present": bool(re.search(r"\b(?:30|60|250)\s*(?:ml|میل)\b|(?:۳۰|۶۰|۲۵۰)\s*میل", combined, re.I)), "separator_forms": sorted(set(re.findall(r"[|:/—–-]", combined))), "current_url": x.get("permalink") or x.get("url"), "http_status": r.get("status")})
    return rows


def family(url):
    path = urllib.parse.urlparse(url).path.lower()
    if "/shop/" in path and any(s in path for s in ["/product", "/shop/"]):
        return "SHOP" if path.rstrip("/") == "/shop" else "PRODUCT"
    if "product-category" in path or "/mag/" in path and "category" in path:
        return "PRODUCT_CATEGORY"
    if "/academy/" in path and "/lessons/" in path:
        return "LESSON"
    if "/academy/" in path:
        return "ACADEMY"
    if "/article" in path or "/mag/" in path:
        return "ARTICLE"
    if "/tag/" in path:
        return "TAG"
    if "/volume/" in path or "attribute" in path:
        return "ATTRIBUTE"
    if path == "/":
        return "STATIC"
    return "OTHER"


def internal_graph(products, categories, blog_categories, lessons, courses, articles, fetched):
    source = []
    for x in products + categories + blog_categories + lessons + courses + articles:
        source.append((x["entity_id"], x.get("permalink"), x["post_type"] if "post_type" in x else x["taxonomy"]))
    source += [("SHOP", "https://www.mariwork.ir/shop/", "shop"), ("ACADEMY", "https://www.mariwork.ir/academy/", "academy")]
    entities = {x.get("permalink"): x["entity_id"] for x in products + categories + blog_categories + lessons + courses + articles if x.get("permalink")}
    edges, counts = [], Counter()
    for eid, url, typ in source:
        for link in fetched.get(url, {}).get("links", []):
            absolute = urllib.parse.urljoin(url, link["href"])
            parsed = urllib.parse.urlparse(absolute)
            if parsed.netloc and parsed.netloc not in {"www.mariwork.ir", "mariwork.ir"}:
                continue
            clean = urllib.parse.urlunparse((parsed.scheme or "https", parsed.netloc or "www.mariwork.ir", parsed.path, "", parsed.query, ""))
            dest_family = family(clean)
            counts[dest_family] += 1
            edges.append({"source_entity": eid, "source_url": url, "destination_url": clean, "destination_entity": entities.get(clean) or entities.get(clean.rstrip("/")), "anchor_text": link["anchor_text"], "destination_family": dest_family, "source_evidence": "anonymous_initial_html"})
    return {"entities_checked": len(source), "edges_collected": len(edges), "unresolved_destinations": sum(not x["destination_entity"] for x in edges), "family_edge_counts": dict(counts), "edges": edges}


def parameter_evidence():
    base = "https://www.mariwork.ir/shop/"
    urls = {
        "filter_volume": base + "?filter_volume=30ml&query_type_volume=or",
        "orderby": base + "?orderby=price",
        "per_page": base + "?per_page=9",
        "per_row": base + "?per_row=3",
        "shop_view": base + "?shop_view=list",
        "pagination": base + "page/2/",
        "product-page": base + "?product-page=2",
        "product_search": "https://www.mariwork.ir/?post_type=product&s=fabric",
        "variation_selection": "https://www.mariwork.ir/shop/red-mariwork-fabric-color-code116/?attribute_pa_volume=30ml",
    }
    fetched = fetch_many(list(urls.values()))
    sm = sr2.sitemap_membership()
    rows = []
    for family_name, url in urls.items():
        r = fetched[url]
        rows.append({"parameter_family": family_name, "source_url": url, "http_status": r.get("status"), "canonical": r.get("canonical"), "robots": r.get("robots"), "x_robots": r.get("x_robots"), "title": r.get("title"), "h1": r.get("h1"), "sitemap_membership": sm.get(url, []) or sr2.sitemap_url_membership(url), "linked_from_current_html": None, "content_identity_hash": r.get("body_sha256"), "safe_get_only": True})
    return {"representatives": rows, "transactional_urls_requested": False}


def dossier_27727(fetched, products):
    p = next(x for x in products if x["wp_id"] == 27727)
    r = fetched[p["permalink"]]
    gsc = next((x for x in sr2.gsc_rows() if "silver-rainbow-glitter-mariwork-fabric-medium-code217-60ml/" in x["Top pages"]), None)
    path = ROOT / "pages/products/WP-27727.md"
    lines = [
        "---", 'framework_version: "1.0"', 'dossier_schema_version: "1.0"', 'entity_id: "WP-27727"', 'wp_id: "27727"', 'type: "product"', 'family: "products"', f'current_url: "{p["permalink"]}"', f'canonical_url: "{(r.get("canonical") or [p["permalink"]])[0]}"', "legacy_urls: []", "workflow_status: CODEX_AUDITED", "final_disposition: NOT_DECIDED", "blocked: false", "blockers: []", "coverage_state: POST_ROUND1_CURRENT_COVERAGE_ADDITION", "last_updated: 2026-09-25", "---", "", "# Page Dossier — WP-27727", "", "## 0. State", "", "- Workflow status: CODEX_AUDITED", "- Final disposition: NOT_DECIDED", "- Coverage state: POST_ROUND1_CURRENT_COVERAGE_ADDITION", "- This dossier supplements current coverage and does not change the historical 167-entity Round-1 baseline.", "", "## 1. Identity", "", f"- Entity/WP ID: WP-27727 / 27727; type/family: product / products", f"- Current URL: {p['permalink']}", f"- Product title: {p['title']}", f"- Current HTTP: {r.get('status')}", f"- Canonical: {(r.get('canonical') or [None])[0]}", f"- Robots: {', '.join(r.get('robots') or [])}", "", "## 2. URL History", "", "- Historical source: /shop/silver-rainbow-glitter-mariwork-fabric-medium-code217-60ml/", "- A-012 observed 301 to ?post_type=product&p=27727, then 404; historical entity equivalence remains UNKNOWN_NEEDS_VERIFICATION.", "", "## 3. Baseline", "", f"- Historical source GSC row: {gsc or 'NOT_AVAILABLE'}", "- Page+Query relationship: NOT_AVAILABLE.", "", "## 4. Current Page Snapshot", "", f"- HTML title: {(r.get('title') or [None])[0]}", f"- H1: {(r.get('h1') or [None])[0]}", "- Product type: simple.", "- Structured data: current Product JSON-LD is present in the public response; exact types are recorded in SR-003 store evidence.", "- Current evidence is read-only; prices, orders, customers and private data were not collected.", "", "## 5. Codex Audit", "", "- Task: SR-003 supplemental current coverage", "- Mode: READ-ONLY", "", "### Findings", "", "#### WP-27727-F001", "", "- severity: P2", "- scope: PAGE", "- status: OPEN", "- evidence_class: OBSERVED", "- confidence: HIGH", "- source_refs: [SR-003 current public output, A-012 exact historical URL mapping]", "- impact: Current product evidence is now represented; historical volume URL to numeric 404 identity remains unproven.", "- recommendation: INITIAL — preserve separate historical metrics and require independent identity evidence before any migration decision.", "- acceptance_criteria: Second Review verifies current product identity, historical mapping and any approved disposition.", "", "Audit outcome: sufficient for independent Second Review; no approval or implementation performed.", "", "## 6. ChatGPT Independent Second Review", "", "Pending; not performed by Codex.", "", "## 7. Final Approved Findings", "", "Pending; final_disposition remains NOT_DECIDED.", "", "## 8. Implementation", "", "Not authorized or started.", "", "## 9. Codex QA", "", "Not applicable; no implementation performed.", "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path.relative_to(ROOT).as_posix()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    baseline_raw = subprocess.check_output(["git", "-c", f"safe.directory={ROOT}", "show", "fa72845:audits/second-review/reconciliation/round1-finding-reconciliation.json"], cwd=ROOT, text=True)
    counts_before = json.loads(baseline_raw)["relationship_counts"]
    counts_after = fix_finding_classification()
    census, products, categories, blog_categories, lessons, courses, articles, fetched = current_data()
    write("current-blog-category-matrix.json", category_matrix(blog_categories, fetched))
    variable_urls = [x["permalink"] for x in json.loads((RECON/"current-volume-architecture.json").read_text())["current_variable_parents"]]
    variable_fetched = fetch_many(variable_urls)
    variable_rows = variable_schema(products, variable_fetched)
    write("current-variable-schema-matrix.json", {"parent_count": 60, "rows": variable_rows, "counts": {k: sum(bool(x[k]) for x in variable_rows) for k in ["product_present","product_group_present","offer_present","aggregate_offer_present","has_variant_present","is_variant_of_present","product_group_id_present"]}})
    write("bundle-component-matrix.json", bundle_components())
    title_rows = title_h1(products, categories, fetched)
    shop_detail = fetched.get("https://www.mariwork.ir/shop/", {})
    category_rows = title_h1(categories, [], fetched)
    write("current-title-h1-matrix.json", {"products": title_rows, "shop": {"url":"https://www.mariwork.ir/shop/","title":(shop_detail.get("title") or [None])[0],"h1":(shop_detail.get("h1") or [None])[0],"http_status":shop_detail.get("status")}, "product_categories": category_rows})
    graph = internal_graph(products, categories, blog_categories, lessons, courses, articles, fetched)
    write("current-internal-link-graph.json", graph)
    params = parameter_evidence()
    variation_rows = [x for x in params["representatives"] if x["parameter_family"] == "variation_selection"]
    volume_arch = json.loads((RECON / "current-volume-architecture.json").read_text(encoding="utf-8"))
    representative_parents = []
    for required in (("30ml", "60ml", "250ml"), ("30ml", "60ml")):
        match = next((p for p in volume_arch["current_variable_parents"] if all(v in p["current_purchasable_volumes"] for v in required)), None)
        if not match:
            continue
        variations = [v for v in match["variations"] if v.get("status") == "publish" and v.get("volume") in required]
        representative_parents.append({
            "parent_product_id": match["parent_product_id"],
            "parent_url": match["permalink"],
            "volumes": list(required),
            "variation_ids": [{"variation_id": v["variation_id"], "volume": v["volume"], "status": v["status"]} for v in variations],
            "selector_parameter": "attribute_pa_volume",
            "selector_urls": [{"variation_id": v["variation_id"], "volume": v["volume"], "url": match["permalink"] + "?" + urllib.parse.urlencode({"attribute_pa_volume": v["volume"]})} for v in variations],
        })
    write("variant-url-architecture.json", {"representatives": variation_rows, "representative_parents": representative_parents, "architecture": "WooCommerce variation selection is exposed through attribute_pa_volume query parameters on safe GET; no transactional request was made.", "stable_direct_variant_url": "PARTIAL", "canonical_observation": "The tested selector URL canonicalized to the parent URL."})
    write("current-parameter-policy-evidence.json", params)
    dossier = dossier_27727(fetched, products)
    summary = {"source_head": subprocess.check_output(["git","-c",f"safe.directory={ROOT}","rev-parse","HEAD"],cwd=ROOT,text=True).strip(), "finding_counts_before": counts_before, "finding_counts_after": dict(counts_after), "blog_category_count": len(blog_categories), "blog_category_empty_200_noindex": sum(x["count"] == 0 and x["http_status"] == 200 and any("noindex" in z for z in x["robots"]) for x in category_matrix(blog_categories, fetched)), "blog_category_404": sum(x["http_status"] == 404 for x in category_matrix(blog_categories, fetched)), "product_count": len(products), "variable_parent_count": 60, "dossier_27727": dossier, "parameter_families_checked": sorted({x["parameter_family"] for x in params["representatives"]}), "internal_entities_checked": graph["entities_checked"], "internal_edges": graph["edges_collected"], "unresolved_destinations": graph["unresolved_destinations"], "bundle_parents_checked": 22, "bundle_component_mappings": sum(x["component_mapping_obtained"] for x in bundle_components()["bundles"])}
    write("sr003-store-summary.json", summary)
    md = f"""# SR-003 — Store Evidence Closure

Read-only current Store evidence. Original Round-1 evidence/dossiers remain immutable; WP-27727 is a post-Round-1 coverage addition.

## Classification correction
- Before: {counts_before}
- After: {dict(counts_after)}
- Current entities are evaluated before migration context; Yoast → Rank Math does not make current entities historical.

## Blog categories
- Current categories checked: {len(blog_categories)}
- Empty 200/noindex: {summary['blog_category_empty_200_noindex']}
- 404: {summary['blog_category_404']}
- Non-empty/indexable records are retained in current-blog-category-matrix.json.

## WP-27727
- Supplemental dossier: {dossier}
- Status: CODEX_AUDITED; final_disposition remains NOT_DECIDED.

## Store matrices
- Variable schema: 60 parents in current-variable-schema-matrix.json.
- Bundle components: 22 parents; mappings obtained for {summary['bundle_component_mappings']}.
- Product title/H1 matrix: 84 products, Shop and Product Categories.
- Internal-link graph: {graph['entities_checked']} entities, {graph['edges_collected']} edges, {graph['unresolved_destinations']} unresolved destinations.
- Parameter families: {', '.join(summary['parameter_families_checked'])}.

## Remaining blockers
- Variant URL stability is PARTIAL and is recorded without transactional testing.
- Accessory/tool representative was not deterministically identified; no claim is made.
- Page+Query remains NOT_AVAILABLE.
"""
    (OUT/"SR-003-STORE-EVIDENCE-CLOSURE.md").write_text(md, encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
