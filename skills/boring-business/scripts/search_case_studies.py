#!/usr/bin/env python3
"""
search_case_studies.py - Zero-dependency CLI search tool for Boring Business Case Studies.

Bundled with the boring-business skill. Searches 137+ verified profitable,
bootstrapped, and automated businesses.
"""

import argparse
import json
import os
import sys
from pathlib import Path


def load_data():
    script_dir = Path(__file__).resolve().parent
    data_path = script_dir.parent / "data" / "case_studies.json"
    if not data_path.exists():
        # Fallback to local data dir if run from repo root
        data_path = Path("skills/boring-business/data/case_studies.json")
    if not data_path.exists():
        sys.stderr.write(f"Error: case_studies.json not found at {data_path}\n")
        return []
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)


def search(query=None, min_revenue=None, max_revenue=None, biz_type=None, channel=None, limit=5):
    items = load_data()
    results = []

    query_tokens = query.lower().split() if query else []

    for item in items:
        # Filter by revenue
        rev = item.get("revenue_normalized") or 0
        if min_revenue is not None and rev < min_revenue:
            continue
        if max_revenue is not None and rev > max_revenue:
            continue

        # Filter by business type
        b_type = (item.get("business_type") or "").lower()
        if biz_type and biz_type.lower() not in b_type:
            continue

        # Filter by distribution channel
        channels = (item.get("distribution_channels") or "").lower()
        if channel and channel.lower() not in channels:
            continue

        # Keyword matching
        if query_tokens:
            searchable_text = " ".join([
                item.get("business_name") or "",
                item.get("niche") or "",
                item.get("tags") or "",
                item.get("business_type") or "",
                item.get("distribution_channels") or "",
                item.get("revenue_raw") or "",
            ]).lower()

            if not any(token in searchable_text for token in query_tokens):
                continue

        results.append(item)

    return results[:limit]


def format_markdown(results):
    if not results:
        return "No case studies found matching criteria."

    lines = [
        f"### Found {len(results)} Boring Business Case Studies\n",
        "| Business Name | Type | Revenue / MRR | Distribution | Tags |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]
    for r in results:
        name = r.get("business_name") or "Unnamed"
        b_type = r.get("business_type") or "N/A"
        rev = r.get("revenue_raw") or (f"${r.get('revenue_normalized'):,}/mo" if r.get("revenue_normalized") else "N/A")
        channels = r.get("distribution_channels") or "N/A"
        tags = (r.get("tags") or "")[:40]
        lines.append(f"| **{name}** | {b_type} | `{rev}` | {channels} | {tags} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search Boring Business case studies and real-world cash cows.")
    parser.add_argument("query", nargs="?", default="", help="Keywords to search (e.g. 'seo', 'slack bot', 'pdf', 'affiliate')")
    parser.add_argument("-n", "--num-results", type=int, default=5, help="Number of results to return (default: 5)")
    parser.add_argument("--min-revenue", type=int, default=None, help="Minimum monthly revenue in USD")
    parser.add_argument("--max-revenue", type=int, default=None, help="Maximum monthly revenue in USD")
    parser.add_argument("--type", dest="biz_type", help="Filter by business type (tool, saas, content, directory)")
    parser.add_argument("--channel", help="Filter by distribution channel (seo, content_marketing, social, affiliate)")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()

    results = search(
        query=args.query,
        min_revenue=args.min_revenue,
        max_revenue=args.max_revenue,
        biz_type=args.biz_type,
        channel=args.channel,
        limit=args.num_results,
    )

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(format_markdown(results))


if __name__ == "__main__":
    main()
