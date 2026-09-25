#!/usr/bin/env python3
"""Read-only public evidence collector for Second Review Evidence Closure 001.

This script reads the frozen Round-1 handoff, performs anonymous public GETs
with at most two workers, and writes new evidence only under audits/second-review.
It never sends a form, follows an action URL, or stores complete HTML.
"""
from __future__ import annotations

import json
import re
import subprocess
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audits/second-review/evidence"
INDEX = ROOT / "handoff/round1/round1-review-index.json"
UA = "Mariwork-SEO-SecondReview-Evidence/1.0"
MAX_BODY = 6 * 1024 * 1024


def source_timestamp():
    """Use the repository input revision as a stable collection timestamp."""
    try:
        return subprocess.check_output(
            ["git", "show", "-s", "--format=%cI", "HEAD"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return "SOURCE_TIMESTAMP_UNAVAILABLE"


COLLECTION_TIMESTAMP = source_timestamp()


class RedirectTracker(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        super().__init__()
        self.chain = []

    def redirect_request(self, req, fp, code, msg, headers, new):
        self.chain.append({"url": req.full_url, "status": code, "location": new})
        return super().redirect_request(req, fp, code, msg, headers, new)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = []
        self.meta_description = []
        self.meta_robots = []
        self.canonicals = []
        self.h1 = []
        self.jsonld = []
        self.microdata = []
        self._tag = None
        self._buf = []
        self._script_type = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        tag = tag.lower()
        if tag in {"title", "h1"}:
            self._tag, self._buf = tag, []
        if tag == "meta":
            name = (attrs.get("name") or attrs.get("property") or "").lower()
            if name == "description": self.meta_description.append(attrs.get("content", ""))
            if name in {"robots", "googlebot"}: self.meta_robots.append(attrs.get("content", ""))
        if tag == "link" and "canonical" in (attrs.get("rel") or "").lower().split():
            self.canonicals.append(attrs.get("href", ""))
        if tag == "script" and "json" in (attrs.get("type") or "").lower():
            self._tag, self._script_type, self._buf = "jsonld", attrs.get("type", ""), []
        if attrs.get("itemtype"):
            self.microdata.append(attrs["itemtype"])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data):
        if self._tag:
            self._buf.append(data)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self._tag == tag:
            value = " ".join("".join(self._buf).split())
            if tag == "title": self.title.append(value)
            elif tag == "h1": self.h1.append(value)
            self._tag, self._buf = None, []
        elif self._tag == "jsonld" and tag == "script":
            self.jsonld.append("".join(self._buf))
            self._tag, self._buf = None, []


def json_types(value):
    result = []
    if isinstance(value, dict):
        typ = value.get("@type")
        if isinstance(typ, str): result.append(typ)
        elif isinstance(typ, list): result.extend(str(x) for x in typ)
        for child in value.values(): result.extend(json_types(child))
    elif isinstance(value, list):
        for child in value: result.extend(json_types(child))
    return result


def fetch(item):
    entity, url = item["entity_id"], item["current_url"]
    tracker = RedirectTracker()
    record = {"entity_id": entity, "url": url, "collected_at": COLLECTION_TIMESTAMP, "method": "anonymous_public_get"}
    if not url or urllib.parse.urlparse(url).scheme not in {"http", "https"}:
        record.update({"error": "UNSAFE_URL_SKIPPED", "status": None})
        return record
    try:
        opener = urllib.request.build_opener(tracker)
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
        with opener.open(req, timeout=35) as response:
            body = response.read(MAX_BODY + 1)
            truncated = len(body) > MAX_BODY
            body = body[:MAX_BODY]
            charset = response.headers.get_content_charset() or "utf-8"
            html = body.decode(charset, errors="replace")
            parser = PageParser(); parser.feed(html)
            types, parse_errors = [], 0
            for block in parser.jsonld:
                try: types.extend(json_types(json.loads(block)))
                except Exception: parse_errors += 1
            lower = html.lower()
            markers = sorted(set(re.findall(r"rank[-_]math(?:[-_][a-z0-9_-]+)?", lower)))
            record.update({"status": response.status, "final_url": response.geturl(), "redirect_chain": tracker.chain, "content_type": response.headers.get("content-type", ""), "x_robots_tag": response.headers.get("x-robots-tag", ""), "title_count": len(parser.title), "title": parser.title, "meta_description_count": len(parser.meta_description), "meta_description": parser.meta_description, "robots_meta": parser.meta_robots, "canonical_count": len(parser.canonicals), "canonicals": parser.canonicals, "h1_count": len(parser.h1), "h1": parser.h1, "jsonld_script_count": len(parser.jsonld), "jsonld_types": sorted(set(types)), "microdata_itemtypes": sorted(set(parser.microdata)), "jsonld_parse_errors": parse_errors, "rank_math_public_markers": markers, "body_truncated": truncated})
    except Exception as exc:
        record.update({"status": None, "redirect_chain": tracker.chain, "error": f"{type(exc).__name__}: {str(exc)[:240]}"})
    return record


def xml_urls(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/xml,text/xml"})
    with urllib.request.urlopen(req, timeout=35) as response:
        root = ET.fromstring(response.read(MAX_BODY))
    return root, response.geturl()


def sitemap_walk(start):
    seen, memberships, errors = set(), {}, []
    queue = [start]
    while queue:
        url = queue.pop(0)
        if url in seen: continue
        seen.add(url)
        try: root, final = xml_urls(url)
        except Exception as exc:
            errors.append({"url": url, "error": f"{type(exc).__name__}: {str(exc)[:240]}"}); continue
        tag = root.tag.rsplit("}", 1)[-1]
        if tag == "sitemapindex":
            for node in root.iter():
                if node.tag.rsplit("}", 1)[-1] == "loc" and node.text:
                    queue.append(node.text.strip())
        elif tag == "urlset":
            for node in root:
                loc = next((n.text.strip() for n in node if n.tag.rsplit("}", 1)[-1] == "loc" and n.text), None)
                if loc: memberships.setdefault(loc, []).append(url)
    return {"start": start, "sitemaps_seen": sorted(seen), "membership": {k: sorted(v) for k, v in sorted(memberships.items())}, "errors": errors}


def main():
    rows = json.loads(INDEX.read_text(encoding="utf-8"))
    if len(rows) != 167: raise SystemExit(f"expected 167 handoff rows, got {len(rows)}")
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(fetch, row) for row in rows]
        for future in as_completed(futures): records.append(future.result())
    records.sort(key=lambda x: x["entity_id"])
    (OUT / "current-seo-output.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in records), encoding="utf-8")
    families = {}
    for row in rows:
        families.setdefault(row["family"], []).append(row["entity_id"])
    family_summary = {}
    for family, ids in sorted(families.items()):
        subset = [x for x in records if x["entity_id"] in ids]
        family_summary[family] = {"pages_checked": len(subset), "with_jsonld": sum(x.get("jsonld_script_count", 0) > 0 for x in subset), "without_jsonld": sum(x.get("jsonld_script_count", 0) == 0 for x in subset), "schema_types": sorted({t for x in subset for t in x.get("jsonld_types", [])}), "duplicate_jsonld_pages": sum(len(x.get("jsonld_types", [])) != len(set(x.get("jsonld_types", []))) for x in subset), "parse_errors": sum(x.get("jsonld_parse_errors", 0) for x in subset)}
    summary = {"source": "handoff/round1/round1-review-index.json", "entities_checked": len(records), "errors": sum("error" in x for x in records), "schema_family_summary": family_summary, "round1_parser_discrepancy": any((x.get("jsonld_script_count", 0) > 0) != bool(x.get("jsonld_types")) for x in records), "generated_at": COLLECTION_TIMESTAMP}
    (OUT / "current-seo-output-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sitemap = sitemap_walk("https://www.mariwork.ir/wp-sitemap.xml")
    normalized = lambda u: (u or "").rstrip("/")
    for row in rows:
        row["sitemap_membership"] = sitemap["membership"].get(row["current_url"], sitemap["membership"].get(normalized(row["current_url"]), []))
    (OUT / "sitemap-membership.json").write_text(json.dumps({"source": "https://www.mariwork.ir/wp-sitemap.xml", "sitemap_walk": sitemap, "entity_membership": {x["entity_id"]: x["sitemap_membership"] for x in rows}}, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"entities_checked": len(records), "errors": summary["errors"], "round1_parser_discrepancy": summary["round1_parser_discrepancy"], "sitemaps": len(sitemap["sitemaps_seen"])}))


if __name__ == "__main__": main()
