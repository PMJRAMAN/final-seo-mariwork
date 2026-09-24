#!/usr/bin/env python3
"""Build a deterministic, read-only Round-1 -> Second Review handoff."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "handoff" / "round1"
EXPECTED = 167
AUDITED = {"CODEX_AUDITED", "SECOND_REVIEWED", "APPROVED", "IMPLEMENTED", "CODEX_QA_PASSED", "FINAL_QA_PASSED"}
GROUPS = ["SITEWIDE / FOUNDATION", "STORE / SHOP", "HOMEPAGE", "STATIC PAGES", "BLOG / ARTICLES", "ACADEMY", "CUSTOM CONTENT", "ARCHIVES / SYSTEM / TAXONOMIES", "OTHER / UNMAPPED"]


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="strict")


def scalar(value: str):
    value = value.strip()
    if not value:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.lower() in {"null", "none", "not_available", "not applicable"}:
        return None if value.lower() in {"null", "none"} else value
    return value


def frontmatter(raw: str) -> dict:
    if not raw.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = raw.find("\n---", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    out = {}
    for line in raw[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = scalar(value)
    return out


def section(raw: str, heading: str, next_heading: str | None = None) -> str:
    m = re.search(r"^" + re.escape(heading) + r"\s*$", raw, re.M | re.I)
    if not m:
        return ""
    tail = raw[m.end():]
    if next_heading:
        # Section labels may carry a title, e.g. ``## 7. ChatGPT ...``.
        pattern = r"^" + re.escape(next_heading.rstrip(".")) + r"(?:\.|\s).*$" if next_heading.endswith(".") else r"^" + re.escape(next_heading) + r"\s*$"
        n = re.search(pattern, tail, re.M | re.I)
        if n:
            tail = tail[:n.start()]
    return tail.strip()


def field(raw: str, name: str):
    # Findings use both one-field-per-line YAML and compact semicolon rows.
    m = re.search(r"(?:^|\n|;)\s*(?:[-*]\s*)?" + re.escape(name) + r"\s*:\s*([^;\n]+)", raw, re.I)
    return scalar(m.group(1)) if m else None


def recursive_metrics(value):
    if isinstance(value, dict):
        keys = {str(k).lower() for k in value}
        if {"clicks", "impressions"} & keys:
            return {"clicks": value.get("Clicks", value.get("clicks")), "impressions": value.get("Impressions", value.get("impressions")), "ctr": value.get("CTR", value.get("ctr")), "position": value.get("Position", value.get("position"))}
        for child in value.values():
            found = recursive_metrics(child)
            if found:
                return found
    elif isinstance(value, list):
        for child in value:
            found = recursive_metrics(child)
            if found:
                return found
    return None


def evidence_map():
    result = {}
    path = ROOT / "data/normalized/round1-page-evidence.jsonl"
    if not path.exists():
        raise ValueError(f"missing authoritative evidence: {path}")
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        record = json.loads(line)
        entity = record.get("entity_id")
        if not entity or entity in result:
            raise ValueError(f"duplicate/missing evidence entity at line {line_no}")
        result[entity] = record
    return result


def inventory():
    path = ROOT / "registry/URL-INVENTORY.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_id = {}
    for row in rows:
        entity = row.get("entity_id", "").strip()
        if entity in by_id:
            raise ValueError(f"duplicate inventory entity: {entity}")
        by_id[entity] = row
    return by_id


def dossiers():
    found = {}
    for path in sorted((ROOT / "pages").rglob("*.md")):
        raw = text(path)
        try:
            meta = frontmatter(raw)
        except ValueError:
            continue
        entity = str(meta.get("entity_id") or "").strip()
        if not entity:
            continue
        if entity in found:
            raise ValueError(f"duplicate dossier entity: {entity}")
        found[entity] = (path, raw, meta)
    return found


def review_group(row):
    typ = (row.get("type") or "").lower()
    family = (row.get("family") or "").lower()
    hay = f"{typ} {family}"
    if typ in {"taxonomy", "term", "archive"} and any(x in hay for x in ("category", "tag", "attribute", "product_cat", "product_tag", "pa_")):
        return "ARCHIVES / SYSTEM / TAXONOMIES"
    if any(family.startswith(x) for x in ("product_cat", "product_tag", "post_tag", "pa_")):
        return "ARCHIVES / SYSTEM / TAXONOMIES"
    if any(x in hay for x in ("product", "shop", "woocommerce")) and not any(x in hay for x in ("tag", "attribute", "category")):
        return "STORE / SHOP"
    if "homepage" in hay:
        return "HOMEPAGE"
    if typ in {"page", "static"} or "static" in hay:
        return "STATIC PAGES"
    if any(x in hay for x in ("article", "blog", "post")):
        return "BLOG / ARTICLES"
    if any(x in hay for x in ("academy", "education", "course", "lesson")):
        return "ACADEMY"
    if any(x in hay for x in ("category", "taxonomy", "tag", "attribute", "archive", "system", "url_space")):
        return "ARCHIVES / SYSTEM / TAXONOMIES"
    if any(x in hay for x in ("cpt", "custom")):
        return "CUSTOM CONTENT"
    return "OTHER / UNMAPPED"


def number(value):
    if value in (None, "", "NOT_AVAILABLE", "UNKNOWN_NEEDS_VERIFICATION"):
        return -1.0
    try:
        return float(str(value).replace(",", ""))
    except ValueError:
        return -1.0


def parse_findings(raw: str, entity: str):
    body = section(raw, "### Findings", "## 7.")
    if not body:
        raise ValueError(f"{entity}: missing Findings section")
    starts = list(re.finditer(r"^(?:####\s+|[-*]\s+id:\s*)([A-Za-z0-9_.:-]+-F\d{3})(?:\s+[—–-]\s*(.*))?$", body, re.M))
    if not starts:
        raise ValueError(f"{entity}: no parseable findings")
    result = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(body)
        block = body[match.start():end].strip()
        finding_id = match.group(1)
        title = (match.group(2) or "").strip()
        if not title:
            first = block.splitlines()[0]
            # ``- id: ENTITY-F001`` has no stored heading/title; retain null.
            title = "" if first.lstrip().lower().startswith(("- id:", "* id:")) else ""
        result.append({
            "entity_id": entity,
            "finding_id": finding_id,
            "finding_heading": title,
            "finding_text": block,
            "evidence_class": field(block, "evidence_class"),
            "severity": field(block, "severity"),
            "scope": field(block, "scope"),
            "status": field(block, "status"),
            "recommendation": field(block, "recommendation") or field(block, "Recommendation"),
        })
    return result, body


def normalized_signature(value: str) -> str:
    value = re.sub(r"https?://\S+", "<URL>", value or "")
    value = re.sub(r"\b(?:WP|TERM)-[A-Za-z0-9_-]+\b", "<ENTITY>", value)
    return re.sub(r"\s+", " ", value.strip().lower())


def csv_write(path: Path, rows: list[dict], fields: list[str]):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows([{key: row.get(key, "") if row.get(key) is not None else "" for key in fields} for row in rows])


def git_head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def sitewide_index():
    records = []
    for path in sorted((ROOT / "audits/sitewide").glob("A-*.md")):
        raw = text(path)
        match = re.match(r"#\s+(A-\d+[A-Z]?)\s*[—-]\s*(.+)", raw)
        if not match:
            continue
        findings = re.findall(r"^(?:####?\s+)?([A-Z]-?\d+-F\d{3}|SYS-\d{3})", raw, re.M)
        direct = []
        for line in raw.splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith(("#", "---", "framework_version", "workflow_status", "final_disposition")) and not stripped.startswith("-"):
                direct.append(stripped)
            if len(direct) == 3:
                break
        records.append({"audit_id": match.group(1), "title": match.group(2).strip(), "status": "COMPLETED", "source_file": str(path.relative_to(ROOT)), "direct_extracts": direct, "references": sorted(set(findings))})
    return records


def main():
    inv = inventory()
    ev = evidence_map()
    docs = dossiers()
    entity_rows = []
    findings = []
    missing = []
    malformed = []
    for entity, (path, raw, meta) in sorted(docs.items()):
        if meta.get("workflow_status") not in AUDITED:
            continue
        if entity not in inv:
            raise ValueError(f"audited dossier not in inventory: {entity}")
        source_row = inv[entity]
        # Keep the review index compact; raw inventory notes remain authoritative in
        # registry/URL-INVENTORY.csv and are not copied into every handoff row.
        row = {key: source_row.get(key) for key in ("entity_id", "wp_id", "type", "family", "current_url", "canonical_url", "intended_indexability", "actual_status", "sitemap", "dossier", "final_disposition", "disposition_ref")}
        evidence = ev.get(entity, {})
        metrics = recursive_metrics(json.loads(source_row.get("notes") or "{}")) if source_row.get("notes") else None
        try:
            parsed, finding_body = parse_findings(raw, entity)
            if not re.search(r"Audit outcome\s*:", finding_body, re.I):
                # Some dossiers use a compact outcome sentence outside Findings; retain it if present.
                outcome_match = re.search(r"Audit outcome\s*:\s*(.+)", raw, re.I)
            else:
                outcome_match = re.search(r"Audit outcome\s*:\s*(.+)", finding_body, re.I)
            if not outcome_match:
                outcome_match = re.search(r"Audit outcome\s*:\s*(.+)", raw, re.I)
            outcome = outcome_match.group(1).strip() if outcome_match else ""
        except ValueError as exc:
            malformed.append(str(exc))
            continue
        for finding in parsed:
            finding.update({"family": row.get("family", ""), "current_url": row.get("current_url", ""), "dossier_path": str(path.relative_to(ROOT))})
        findings.extend(parsed)
        row.update({
            "workflow_status": meta.get("workflow_status"),
            "final_disposition": meta.get("final_disposition"),
            "priority": meta.get("priority"),
            "review_group": review_group(row),
            "historical_clicks": (metrics or {}).get("clicks"),
            "historical_impressions": (metrics or {}).get("impressions"),
            "historical_ctr": (metrics or {}).get("ctr"),
            "historical_position": (metrics or {}).get("position"),
            "current_http_status": evidence.get("status", row.get("actual_status")),
            "indexability_observation": "; ".join(evidence.get("meta_robots", [])) if evidence.get("meta_robots") else None,
            "canonical_observation": evidence.get("canonical") if evidence.get("canonical") else row.get("canonical_url"),
            "title_observation": evidence.get("title"),
            "meta_description_observation": evidence.get("meta_description"),
            "h1_observation": evidence.get("h1"),
            "schema_observation": ", ".join(evidence.get("schema_types", [])) if evidence.get("schema_types") else None,
            "finding_count": len(parsed),
            "finding_ids": ";".join(x["finding_id"] for x in parsed),
            "finding_headings": " | ".join(x["finding_heading"] for x in parsed),
            "evidence_classes": ";".join(sorted({x["evidence_class"] or "" for x in parsed})),
            "audit_outcome": outcome,
            "dossier_path": str(path.relative_to(ROOT)),
        })
        entity_rows.append(row)
    if len(entity_rows) != EXPECTED:
        raise ValueError(f"expected {EXPECTED} audited entities, indexed {len(entity_rows)}")
    ids = [x["entity_id"] for x in entity_rows]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate entity IDs in handoff")
    if missing or malformed:
        raise ValueError("malformed/missing dossiers: " + "; ".join(missing + malformed))
    entity_rows.sort(key=lambda x: (GROUPS.index(x["review_group"]), -number(x.get("historical_impressions")), -number(x.get("historical_clicks")), x["entity_id"]))
    finding_groups = defaultdict(list)
    for finding in findings:
        exact = finding["finding_heading"] + "\n" + finding["finding_text"]
        finding_groups[("exact-match", exact)].append(finding)
    normalized_groups = defaultdict(list)
    for finding in findings:
        normalized_groups[normalized_signature(finding["finding_text"])].append(finding)
    repeated = []
    seen = set()
    for key, group in finding_groups.items():
        if len(group) > 1:
            repeated.append((len(group), "exact-match", key[1], group))
            seen.update(id(x) for x in group)
    for key, group in normalized_groups.items():
        if len(group) > 1 and not all(id(x) in seen for x in group):
            repeated.append((len(group), "normalized-exact-match", group[0]["finding_text"], group))
    repeated.sort(key=lambda x: (-x[0], x[1], x[2]))
    repeated_rows = []
    for index, (count, method, representative, group) in enumerate(repeated, 1):
        repeated_rows.append({"group_id": f"R{index:03d}", "signature_type": method, "representative_finding": representative, "occurrence_count": count, "families": ";".join(sorted({x["family"] for x in group})), "entity_ids": ";".join(sorted({x["entity_id"] for x in group})), "urls": ";".join(sorted({x["current_url"] for x in group})), "second_review_label": "repeated Round-1 finding candidate"})
    OUT.mkdir(parents=True, exist_ok=True)
    entity_fields = ["entity_id", "wp_id", "type", "family", "current_url", "canonical_url", "workflow_status", "final_disposition", "priority", "review_group", "historical_clicks", "historical_impressions", "historical_ctr", "historical_position", "actual_status", "current_http_status", "intended_indexability", "indexability_observation", "canonical_observation", "title_observation", "meta_description_observation", "h1_observation", "schema_observation", "finding_count", "finding_ids", "finding_headings", "evidence_classes", "audit_outcome", "dossier_path"]
    finding_fields = ["entity_id", "family", "current_url", "finding_id", "finding_heading", "finding_text", "evidence_class", "severity", "scope", "status", "recommendation", "dossier_path"]
    repeated_fields = ["group_id", "signature_type", "representative_finding", "occurrence_count", "families", "entity_ids", "urls", "second_review_label"]
    csv_write(OUT / "round1-review-index.csv", entity_rows, entity_fields)
    csv_write(OUT / "round1-findings.csv", findings, finding_fields)
    csv_write(OUT / "round1-repeated-findings.csv", repeated_rows, repeated_fields)
    sitewide = sitewide_index()
    summary = {"source_head": git_head(), "round1_complete": True, "expected_model_entities": EXPECTED, "indexed_model_entities": len(entity_rows), "missing_dossiers": len(missing), "malformed_dossiers": len(malformed), "duplicate_entity_ids": 0, "blocked_entities": 0, "model_remaining": 0, "workflow_status_counts": dict(Counter(x["workflow_status"] for x in entity_rows)), "type_counts": dict(Counter(x["type"] for x in entity_rows)), "family_counts": dict(Counter(x["family"] for x in entity_rows)), "review_group_counts": dict(Counter(x["review_group"] for x in entity_rows)), "finding_count": len(findings), "repeated_finding_candidate_count": len(repeated_rows), "sitewide_audit_count": len(sitewide), "source_evidence_summary": "data/normalized/round1-evidence-summary.json", "source_foundation_context": "data/normalized/round1-foundation-context.json"}
    (OUT / "round1-review-index.json").write_text(json.dumps(entity_rows, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "round1-findings.json").write_text(json.dumps(findings, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "round1-repeated-findings.json").write_text(json.dumps(repeated_rows, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "round1-sitewide-index.json").write_text(json.dumps(sitewide, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "round1-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    top = sorted(entity_rows, key=lambda x: (-number(x.get("historical_impressions")), -number(x.get("historical_clicks")), x["entity_id"]))[:10]
    lines = ["# Mariwork SEO — Round 1 Handoff", "", "## Baseline", f"- Source HEAD: `{summary['source_head']}`", "- Generation is deterministic and timestamp-free; reruns from identical inputs are byte-stable.", "- Framework version: 1.0; dossier schema: 1.0.", "- Round-1 completion: 167/167 model-reviewed entities; page queue complete.", "", "## Integrity", f"- Expected/indexed entities: {EXPECTED}/{len(entity_rows)}", f"- Missing/malformed dossiers: {len(missing)}/{len(malformed)}", f"- CODEX_AUDITED or later: {sum(x['workflow_status'] in AUDITED for x in entity_rows)}", "- Blocked entities: 0", f"- NOT_DECIDED: {sum(x['final_disposition'] == 'NOT_DECIDED' for x in entity_rows)}", "", "## Entity Breakdown"]
    for key, value in summary["review_group_counts"].items(): lines.append(f"- Review group — {key}: {value}")
    lines += ["", "## Highest Historical-Importance Entities", "Historical metrics are copied from existing inventory notes only; Page and Query exports are not joined."]
    for row in top: lines.append(f"- `{row['entity_id']}` — impressions={row.get('historical_impressions') or 'NOT_AVAILABLE'}, clicks={row.get('historical_clicks') or 'NOT_AVAILABLE'} — `{row['dossier_path']}`")
    lines += ["", "## Existing Finding Breakdown", f"- Existing findings extracted verbatim: {len(findings)}", f"- Repeated finding candidates: {len(repeated_rows)}", "", "## Repeated Round-1 Finding Candidates", "These are grouping aids, not Second Review conclusions."]
    for row in repeated_rows[:15]: lines.append(f"- `{row['group_id']}` — {row['occurrence_count']} occurrences ({row['signature_type']}); families={row['families']}")
    lines += ["", "## Sitewide/Foundation Work"]
    for item in sitewide: lines.append(f"- `{item['audit_id']}` — {item['title']} — `{item['source_file']}`")
    lines += ["", "## Second Review Order", "1. Sitewide/Foundation index and systemic findings.", "2. Store/shop entities, then remaining review groups in `round1-review-index.csv` order.", "3. Page-specific findings in `round1-findings.csv`; original dossier paths are retained.", "", "Final dispositions remain `NOT_DECIDED` until independent human Second Review and approval. No Production implementation is authorized by this handoff."]
    (OUT / "ROUND1-HANDOFF.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (OUT / "SECOND-REVIEW-START-HERE.md").write_text("\n".join(["# Second Review — Start Here", "", "Authoritative inputs are the 167 page dossiers under `pages/`, the sitewide audits under `audits/sitewide/`, `registry/URL-INVENTORY.csv`, and the deterministic indexes in this directory.", f"The handoff contains {len(entity_rows)} entities and {len(findings)} existing findings; repeated candidates are in `round1-repeated-findings.csv`.", "Review sitewide findings first, then Store/shop, then the remaining groups in `round1-review-index.csv` order.", "Round-1 findings are Codex findings awaiting independent Second Review; `final_disposition` remains `NOT_DECIDED` until human approval.", "GSC `Pages.csv` and `Queries.csv` are separate aggregations and must not be treated as page-query joined data.", "This handoff adds no SEO analysis, recommendations, or Production changes.", ""]) , encoding="utf-8")
    print(json.dumps({"source_head": summary["source_head"], "entities": len(entity_rows), "findings": len(findings), "repeated_candidates": len(repeated_rows), "sitewide": len(sitewide), "out": str(OUT)}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"HANDOFF_BUILD_FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
