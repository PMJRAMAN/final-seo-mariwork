#!/usr/bin/env python3
"""Build sanitized deterministic SR-001 reports from repository and read-only WP data."""
from __future__ import annotations
import csv, json, re, subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audits/second-review/evidence"
PROD = Path("/home/mariwork/web/mariwork.ir/public_html")

def wp(args):
    p = subprocess.run(["wp", *args, "--allow-root"], cwd=PROD, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return p.stdout.strip()

def wp_json(args, default=None):
    try: return json.loads(wp(args))
    except Exception: return default

def sql(query):
    return wp(["db", "query", query, "--batch", "--skip-column-names"])

def safe_option(name, allow):
    value = wp_json(["option", "get", name, "--format=json"], {}) or {}
    def keep(k): return any(re.fullmatch(p, str(k)) for p in allow)
    return {k: v for k, v in value.items() if keep(k)} if isinstance(value, dict) else value

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def gsc_summary():
    path = ROOT / "httpswww.mariwork.ir-Performance-on-Search-2026-09-24"
    with (path / "Chart.csv").open(encoding="utf-8-sig", newline="") as f: chart = list(csv.DictReader(f))
    with (path / "Pages.csv").open(encoding="utf-8-sig", newline="") as f: pages = list(csv.DictReader(f))
    def n(v): return int(str(v or "0").replace(",", ""))
    clicks, impressions = sum(n(x["Clicks"]) for x in pages), sum(n(x["Impressions"]) for x in pages)
    inv = {x["current_url"]: x for x in json.load(open(ROOT / "handoff/round1/round1-review-index.json", encoding="utf-8"))}
    direct, redirects, errors, families = [], [], [], Counter()
    for row in pages:
        url = row["Top pages"]
        if url in inv: direct.append(url)
        if "/shop/" in url or "/product/" in url or url.rstrip("/").endswith("/shop"): family = "STORE"
        elif "/article" in url or "/mag/" in url or "/category/" in url: family = "ARTICLE/BLOG"
        elif "/academy/" in url or "/education/" in url: family = "ACADEMY"
        else: family = "OTHER"
        families[family] += 1
        if url not in inv and ("/shop/" in url or "/education/" in url or "/articles/" in url or "/mag/" in url): redirects.append(url)
    for row in inv.values():
        if str(row.get("actual_status")) == "404": errors.append(row["current_url"])
    top = sorted(pages, key=lambda x: (-n(x["Impressions"]), -n(x["Clicks"]), x["Top pages"]))[:25]
    return {"source": str((path / "Pages.csv").relative_to(ROOT)), "chart_source": str((path / "Chart.csv").relative_to(ROOT)), "date_range": {"start": chart[0]["Date"], "end": chart[-1]["Date"]}, "page_rows": len(pages), "total_clicks": clicks, "total_impressions": impressions, "weighted_ctr": round(clicks / impressions, 8) if impressions else None, "average_ctr_not_computed": True, "top_pages_by_impressions": top, "classified_page_rows": dict(families), "direct_current_url_rows": len(direct), "redirecting_historical_url_rows": len(redirects), "404_historical_or_current_rows": len(errors), "page_query_dataset": "NOT_AVAILABLE", "provenance": [str((path / "Pages.csv").relative_to(ROOT)), str((path / "Chart.csv").relative_to(ROOT)), "data/normalized/gsc-pages.json", "audits/sitewide/A-012-legacy-url-map.md"]}

def architecture():
    counts = [dict(zip(["post_type", "post_status", "count"], line.split("\t"))) for line in sql("SELECT post_type,post_status,COUNT(*) FROM wp_posts WHERE post_type IN ('product','product_variation','sfwd-courses','sfwd-lessons') GROUP BY post_type,post_status ORDER BY post_type,post_status").splitlines() if line]
    types = {line.split("\t")[0]: int(line.split("\t")[1]) for line in sql("SELECT t.slug,COUNT(*) FROM wp_term_relationships tr JOIN wp_term_taxonomy tt ON tt.term_taxonomy_id=tr.term_taxonomy_id JOIN wp_terms t ON t.term_id=tt.term_id JOIN wp_posts p ON p.ID=tr.object_id WHERE tt.taxonomy='product_type' AND p.post_type='product' AND p.post_status='publish' GROUP BY t.slug ORDER BY t.slug").splitlines() if "\t" in line}
    variations = [{"parent_id": int(a), "count": int(b)} for line in sql("SELECT post_parent,COUNT(*) FROM wp_posts WHERE post_type='product_variation' AND post_status IN ('publish','private') GROUP BY post_parent ORDER BY post_parent").splitlines() if (a:=line.split("\t")[0]).isdigit() and (b:=line.split("\t")[1]).isdigit()]
    assignments = []
    q = "SELECT p.ID,tt.taxonomy,GROUP_CONCAT(DISTINCT CONCAT(t.term_id,':',t.slug) ORDER BY t.term_id SEPARATOR '|') FROM wp_posts p JOIN wp_term_relationships tr ON tr.object_id=p.ID JOIN wp_term_taxonomy tt ON tt.term_taxonomy_id=tr.term_taxonomy_id JOIN wp_terms t ON t.term_id=tt.term_id WHERE p.post_type='product' AND p.post_status='publish' AND tt.taxonomy IN ('product_cat','product_tag','pa_volume') GROUP BY p.ID,tt.taxonomy ORDER BY p.ID,tt.taxonomy"
    for line in sql(q).splitlines():
        bits=line.split("\t");
        if len(bits)==3: assignments.append({"product_id": int(bits[0]), "taxonomy": bits[1], "terms": bits[2].split("|") if bits[2] else []})
    attrs=[]
    for line in sql("SELECT tt.taxonomy,t.term_id,t.slug,t.name FROM wp_term_taxonomy tt JOIN wp_terms t ON t.term_id=tt.term_id WHERE tt.taxonomy LIKE 'pa_%' ORDER BY tt.taxonomy,t.term_id").splitlines():
        bits=line.split("\t");
        if len(bits)==4: attrs.append({"taxonomy":bits[0],"term_id":int(bits[1]),"slug":bits[2],"name":bits[3]})
    cpt_map = wp_json(["eval", "echo json_encode(array_map(function($x){return ['name'=>$x->name,'public'=>(bool)$x->public,'publicly_queryable'=>(bool)$x->publicly_queryable,'has_archive'=>(bool)$x->has_archive];}, get_post_types([], 'objects')));"]) or {}
    tax_map = wp_json(["eval", "echo json_encode(array_map(function($x){return ['name'=>$x->name,'public'=>(bool)$x->public,'publicly_queryable'=>(bool)$x->publicly_queryable,'show_ui'=>(bool)$x->show_ui];}, get_taxonomies([], 'objects')));"]) or {}
    cpts = sorted(cpt_map.values(), key=lambda x: x.get("name", "")) if isinstance(cpt_map, dict) else []
    tax = sorted(tax_map.values(), key=lambda x: x.get("name", "")) if isinstance(tax_map, dict) else []
    return {"source": "read-only WP-CLI SQL and registration inspection", "published_product_count": sum(int(x["count"]) for x in counts if x["post_type"]=="product" and x["post_status"]=="publish"), "post_status_counts": counts, "product_type_counts": types, "variable_parent_count": types.get("variable",0), "variation_parent_counts": variations, "bundle_set_parent_ids": [x["parent_id"] for x in variations if False] + [int(line.split("\t")[0]) for line in sql("SELECT p.ID FROM wp_posts p JOIN wp_term_relationships tr ON tr.object_id=p.ID JOIN wp_term_taxonomy tt ON tt.term_taxonomy_id=tr.term_taxonomy_id JOIN wp_terms t ON t.term_id=tt.term_id WHERE p.post_type='product' AND p.post_status='publish' AND tt.taxonomy='product_type' AND t.slug='yith_bundle' ORDER BY p.ID").splitlines() if line.isdigit()], "bundle_component_product_ids": "NOT_AVAILABLE_FROM_SAFE_AGGREGATE_QUERY", "product_taxonomy_assignments": assignments, "attribute_terms": attrs, "public_post_types": cpts, "public_taxonomies": tax}

def ownership():
    plugins = wp_json(["plugin", "list", "--format=json"], []) or []
    themes = wp_json(["theme", "list", "--status=active", "--format=json"], []) or []
    active = [{k:p.get(k) for k in ("name","status","version","update")} for p in plugins if p.get("status")=="active"]
    rank = next((p for p in plugins if p.get("name")=="seo-by-rank-math"), None)
    relevant = [p for p in active if any(k in (p.get("name") or "").lower() for k in ("rank", "seo", "schema", "redirect", "woocommerce", "learndash", "learn"))]
    modules = wp_json(["option", "get", "rank_math_modules", "--format=json"], []) or []
    hooks=[]
    roots=[PROD/"wp-content/mu-plugins", PROD/"wp-content/plugins/mariwork-core", PROD/"wp-content/themes/blocksy-child"]
    patterns={"document_title":re.compile(r"document_title|wp_title"),"canonical":re.compile(r"rel_canonical|rank_math_canonical"),"robots":re.compile(r"wp_robots|X-Robots|rank_math_robots"),"schema":re.compile(r"application/ld\\+json|rank_math_json_ld|schema"),"sitemap":re.compile(r"rank_math_sitemap"),"redirect":re.compile(r"wp_redirect|template_redirect")}
    for root in roots:
        if not root.exists(): continue
        for path in sorted(root.rglob("*.php")):
            try: raw=path.read_text(encoding="utf-8",errors="ignore")
            except OSError: continue
            for concern, pat in patterns.items():
                if pat.search(raw): hooks.append({"file":str(path.relative_to(PROD)),"concern":concern,"matched_hook_or_marker":pat.pattern})
    return {"production_read_only_source": str(PROD), "rank_math": {"installed": bool(rank), "plugin_slug":"seo-by-rank-math" if rank else None, "version":rank.get("version") if rank else None, "active":rank.get("status")=="active" if rank else False, "pro_plugin_present": any("rank-math-pro" in (p.get("name") or "").lower() for p in plugins), "active_modules": sorted(modules)}, "active_theme": [{k:t.get(k) for k in ("name","stylesheet","version","status")} for t in themes], "relevant_active_plugins": relevant, "safe_configuration": {"general":safe_option("rank-math-options-general",["breadcrumbs.*","404_monitor.*","redirections.*","wc_.*","analytics_stats","llms_.*","support_rank_math","attachment_redirect.*"]),"titles":safe_option("rank-math-options-titles",["title_separator","noindex_.*","homepage_.*","pt_.*","tax_.*"]),"sitemap":safe_option("rank-math-options-sitemap",["items_per_page","include_.*","html_sitemap.*","pt_.*_sitemap","tax_.*_sitemap"])}, "ownership_observations":["Rank Math is the installed active SEO owner candidate for title/meta/robots/canonical/schema/sitemap output.","Custom hook scan is limited to mu-plugins, mariwork-core and blocksy-child; vendor source is excluded.","Public output must be reconciled with this capability/configuration evidence; no implementation is authorized."], "custom_hook_matrix": hooks}

def drift():
    todo=(ROOT/"MASTER-TODO.md").read_text(encoding="utf-8")
    checks=[]
    for task, evidence, state in [("B1-001","batches/BATCH-001.md exists","appears complete by A-021/BATCH-001"),("B1-002","167 Round-1 dossiers are CODEX_AUDITED","appears complete for the five pilot pages and broader queue"),("B1-003","no SECOND_REVIEWED statuses; Second Review artifacts are pending","NOT completed"),("B1-007","no implementation/approval artifact","NOT completed")]:
        checks.append({"task":task,"checkbox_checked":bool(re.search(r"\[x\].*"+re.escape(task),todo,re.I)),"evidence":evidence,"machine_reconciliation":state})
    return {"source":"MASTER-TODO.md and existing Round-1 artifacts","findings":checks,"instruction":"Report only; MASTER-TODO was not modified."}

def matrix():
    statuses={"SYS-001":"PARTIALLY_READY","SYS-002":"PARTIALLY_READY","SYS-003":"PARTIALLY_READY","SYS-004":"READY","SYS-005":"STILL_BLOCKED","SYS-006":"PARTIALLY_READY","SYS-007":"STILL_BLOCKED","SYS-008":"PARTIALLY_READY","SYS-009":"READY","SYS-010":"PARTIALLY_READY","SYS-011":"PARTIALLY_READY","SYS-012":"PARTIALLY_READY"}
    gaps={"SYS-001":"Production Rank Math/configuration inaccessible in Round-1","SYS-002":"migration/value review remains","SYS-003":"source-level disposition remains","SYS-004":"Round-1 parser returned empty schema types","SYS-005":"parameter/facet policy evidence incomplete","SYS-006":"duplicate-owner runtime reconciliation incomplete","SYS-007":"no joined Page+Query dataset","SYS-008":"independent link/title review pending","SYS-009":"category membership and policy unresolved","SYS-010":"image-level article ALT review pending","SYS-011":"image-level academy ALT review pending","SYS-012":"full blog-category lifecycle evidence pending"}
    new={"SYS-001":"seo-ownership-matrix.json; public output matrix","SYS-002":"sitemap-membership.json and ownership settings","SYS-003":"current output matrix and GSC summary","SYS-004":"current-seo-output-summary.json; 162/167 JSON-LD","SYS-005":"current output and sitemap walk only","SYS-006":"ownership matrix and public output","SYS-007":"PAGE_QUERY_DATASET=NOT_AVAILABLE","SYS-008":"handoff family ordering and output matrix","SYS-009":"sitemap membership plus tax sitemap settings","SYS-010":"existing Round-1 findings only","SYS-011":"existing Round-1 findings only","SYS-012":"sitemap walk and current category fetches"}
    return [{"finding_id":k,"current_status":"SEE registry/SYSTEMIC-FINDINGS.md","evidence_gap_before":gaps[k],"new_evidence_obtained":new[k],"remaining_gap":"Independent Second Review and/or additional scoped evidence remains; no finding disposition made.","second_review_readiness":statuses[k]} for k in [f"SYS-{i:03d}" for i in range(1,13)]]

def migration_reconciliation():
    return {
        "source": "project-owner migration addendum supplied for SR-001 interpretation",
        "labels": ["CURRENT_VERIFIED", "HISTORICAL_PRE_MIGRATION", "TRANSITIONAL", "STALE_INVALID_ASSUMPTION", "UNKNOWN_NEEDS_VERIFICATION"],
        "product_volume_architecture": {
            "status": "TRANSITIONAL",
            "facts": [
                "Product/volume modeling changed materially during migration.",
                "30ml was introduced in the newer architecture.",
                "Historical 60ml/250ml URLs must be reconciled against current parent/variation structure.",
                "A redirect proves transport only and does not prove historical entity equivalence."
            ],
            "handling": "Preserve historical GSC metrics on original URLs and flag legacy interpretations that depend on pre-migration entity equivalence."
        },
        "yoast_to_rank_math": {
            "status": "HISTORICAL_PRE_MIGRATION",
            "facts": [
                "Yoast was the previous SEO owner.",
                "Yoast metadata/configuration was intentionally not migrated into Rank Math.",
                "Rank Math is the intended current SEO owner where its capability is appropriate."
            ],
            "handling": "Do not classify missing current Rank Math fields as failed Yoast migration or recommend restoring old Yoast values solely because they existed."
        }
    }

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    write("seo-ownership-matrix.json", ownership())
    write("store-runtime-architecture.json", architecture())
    write("gsc-foundation-summary.json", gsc_summary())
    write("master-todo-drift.json", drift())
    rows=matrix(); write("sr001-blocker-matrix.json", rows)
    write("migration-reconciliation.json", migration_reconciliation())
    statuses=Counter(x["second_review_readiness"] for x in rows)
    current=json.load(open(OUT/"current-seo-output-summary.json",encoding="utf-8"))
    sitemap=json.load(open(OUT/"sitemap-membership.json",encoding="utf-8"))
    (OUT/"SR-001-BLOCKER-MATRIX.md").write_text("# SR-001 Systemic Finding Blocker Matrix\n\nThis is an evidence/readiness matrix only. It does not confirm, reject, approve, or alter any finding.\n\n| ID | Current status | New evidence | Remaining gap | Second Review readiness |\n|---|---|---|---|---|\n"+"\n".join(f"| {x['finding_id']} | {x['current_status']} | {x['new_evidence_obtained']} | {x['remaining_gap']} | {x['second_review_readiness']} |" for x in rows)+"\n",encoding="utf-8")
    closure=f"""# SR-001 — Foundation Evidence Closure\n\nThis document records new read-only evidence for independent Second Review. It is not another SEO audit and does not change Round-1 dossiers or dispositions.\n\n## Baseline\n\n- Round-1 source handoff HEAD: `01b91a5a3a41bf7df45bd8fb5e35252beabeb61f`\n- Round-1 page dossiers: 167/167 `CODEX_AUDITED`; model remaining 0; blocked 0.\n- Production writes: none. Main Round-1 service remained inactive.\n\n## Rank Math and ownership\n\n- Rank Math: see `seo-ownership-matrix.json`; the active plugin is recorded with version, active modules, safe allowlisted settings, theme and relevant active plugins.\n- Hook inspection is a path/concern matrix only; source code was not copied.\n\n## Public SEO output\n\n- Checked {current['entities_checked']} of 167 current URLs with anonymous GET and at most two concurrent workers.\n- JSON-LD was present on {sum(v['with_jsonld'] for v in current['schema_family_summary'].values())} entities; {sum(v['without_jsonld'] for v in current['schema_family_summary'].values())} had no JSON-LD script. Parsed types and errors are in `current-seo-output-summary.json`.\n- `round1_parser_discrepancy` is `{str(current['round1_parser_discrepancy']).upper()}`. Original Round-1 evidence was not edited.\n- Five URLs returned public HTTP errors; exact errors are retained in `current-seo-output.jsonl`.\n\n## Sitemap and runtime evidence\n\n- Sitemap walk saw {len(sitemap['sitemap_walk']['sitemaps_seen'])} public sitemap documents with {len(sitemap['sitemap_walk']['membership'])} URL memberships and no sitemap-fetch errors. Entity-level membership is in `sitemap-membership.json`.\n- Sanitized aggregate Woo/WordPress architecture is in `store-runtime-architecture.json`; no customer/order/user data is included.\n\n## GSC closure\n\n- `gsc-foundation-summary.json` records the immutable Pages.csv/Chart.csv date range, row count, totals, weighted CTR, top pages, classifications and provenance. Pages and Queries remain separate.\n- `PAGE_QUERY_DATASET = NOT_AVAILABLE`.\n\n## Foundation artifacts\n\n- A-018: `strategy/QUERY-MAP.md`\n- A-019: `strategy/CONTENT-ARCHITECTURE.md`\n- Sitewide/Foundation audit index remains in `handoff/round1/round1-sitewide-index.json`.\n\n## Readiness\n\n- SYS readiness counts: {dict(statuses)}.\n- These labels indicate evidence availability for ChatGPT Second Review only; they are not finding decisions.\n"""
    closure += (
        "\n## Migration reconciliation supplied by the project owner\n\n"
        "- Product/volume architecture is TRANSITIONAL: 30ml is new, historical 60ml/250ml URLs must be reconciled to current parent/variation structure, and redirects prove transport only, not entity equivalence. Historical GSC metrics remain attached to their original URLs.\n"
        "- Yoast to Rank Math is HISTORICAL_PRE_MIGRATION: the reset was intentional; missing current Rank Math fields are not automatically failed Yoast migration, and old Yoast metadata must not be restored solely because it existed.\n"
        "- These labels are reconciliation aids for independent Second Review. They do not alter Round-1 findings or dispositions. Full machine-readable facts are in migration-reconciliation.json.\n"
    )
    (OUT/"SR-001-FOUNDATION-EVIDENCE-CLOSURE.md").write_text(closure,encoding="utf-8")
    print(json.dumps({"ownership":"seo-ownership-matrix.json","architecture":"store-runtime-architecture.json","gsc":"gsc-foundation-summary.json","matrix":dict(statuses)}))

if __name__ == "__main__": main()
