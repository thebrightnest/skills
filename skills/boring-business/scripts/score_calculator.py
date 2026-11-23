#!/usr/bin/env python3
"""
score_calculator.py - Zero-dependency scoring calculator for Boring Business ideas.

Supports:
1. Quick Validation (Tier 1): Rapid Go / No-Go decision based on 4 quick signals.
2. Deep Validation (Tier 2): Full 5-factor weighted scorecard (Search Demand 25%,
   Distribution 25%, Organic Growth 20%, Automation 15%, Willingness to Pay 15%).
"""

import argparse
import json
import sys


def calculate_quick(search_volume, competition_difficulty, intent_commercial, automatable):
    """
    Tier 1 Quick Validation Scoring:
    - search_volume: e.g. monthly searches (int) or score 1-5
    - competition_difficulty: 'low', 'medium', 'high' (or int KD 0-100)
    - intent_commercial: bool (True if commercial/transactional, False if purely informational)
    - automatable: bool (True if can be largely automated)
    """
    flags = []
    score = 0

    # Volume check
    if isinstance(search_volume, (int, float)):
        if search_volume >= 5000:
            score += 30
            flags.append("✅ High search demand (5,000+/mo)")
        elif search_volume >= 1000:
            score += 20
            flags.append("✅ Moderate search demand (1,000-5,000/mo)")
        elif search_volume >= 300:
            score += 10
            flags.append("⚠️ Niche/low volume (300-1,000/mo)")
        else:
            score += 0
            flags.append("❌ Very low or zero search demand (<300/mo)")
    else:
        score += 15

    # Competition check
    if isinstance(competition_difficulty, (int, float)):
        if competition_difficulty < 30:
            score += 25
            flags.append("✅ Low keyword difficulty (<30)")
        elif competition_difficulty < 60:
            score += 15
            flags.append("⚠️ Moderate keyword difficulty (30-60)")
        else:
            score += 0
            flags.append("❌ Saturated / high keyword difficulty (60+)")
    elif isinstance(competition_difficulty, str):
        comp = competition_difficulty.lower()
        if "low" in comp:
            score += 25
            flags.append("✅ Low competition")
        elif "med" in comp:
            score += 15
            flags.append("⚠️ Moderate competition")
        else:
            score += 0
            flags.append("❌ High competition")

    # Commercial Intent
    if intent_commercial:
        score += 25
        flags.append("✅ Clear commercial / problem-solving intent")
    else:
        score += 0
        flags.append("❌ Purely informational or entertainment intent")

    # Automatable
    if automatable:
        score += 20
        flags.append("✅ Feasible for solo automation / no heavy manual ops")
    else:
        score += 0
        flags.append("❌ Requires manual fulfillment / high operational overhead")

    # Decision
    if score >= 70:
        decision = "🟢 ADVANCE TO DEEP VALIDATION (GO)"
    elif score >= 50:
        decision = "🟡 CONDITIONAL ADVANCE / PIVOT ANGLE"
    else:
        decision = "🔴 DISQUALIFY / DROP (NO-GO)"

    return {
        "tier": "Quick Validation (Tier 1)",
        "score_total": score,
        "max_score": 100,
        "decision": decision,
        "signals": flags,
    }


def calculate_deep(search_demand, distribution, organic_growth, automation, willingness_to_pay):
    """
    Tier 2 Deep Validation Scoring:
    Scores 1-5 for each:
    - Search Demand (25%)
    - Distribution Potential (25%)
    - Organic Growth Potential (20%)
    - Automation Level (15%)
    - Willingness to Pay (15%)
    """
    weights = {
        "search_demand": 0.25,
        "distribution": 0.25,
        "organic_growth": 0.20,
        "automation": 0.15,
        "willingness_to_pay": 0.15,
    }

    scores = {
        "Search Demand (25%)": (search_demand, search_demand * weights["search_demand"]),
        "Distribution Potential (25%)": (distribution, distribution * weights["distribution"]),
        "Organic Growth Potential (20%)": (organic_growth, organic_growth * weights["organic_growth"]),
        "Automation Level (15%)": (automation, automation * weights["automation"]),
        "Willingness to Pay (15%)": (willingness_to_pay, willingness_to_pay * weights["willingness_to_pay"]),
    }

    weighted_total = sum(v[1] for v in scores.values())

    if weighted_total >= 4.0:
        decision = "🟢 BUILD IT (High confidence MVP)"
    elif weighted_total >= 3.5:
        decision = "🟡 PRE-SELL & VALIDATE (Landing page + 10 pre-orders)"
    elif weighted_total >= 3.0:
        decision = "🟡 INVESTIGATE FURTHER (Customer discovery interviews)"
    elif weighted_total >= 2.5:
        decision = "🟠 PIVOT (Rethink angle/audience)"
    elif weighted_total >= 2.0:
        decision = "🔴 LIKELY ABANDON (Weak fundamentals)"
    else:
        decision = "🔴 ABANDON (Not a viable boring cash cow)"

    return {
        "tier": "Deep Validation (Tier 2)",
        "overall_score": round(weighted_total, 2),
        "decision": decision,
        "breakdown": {k: {"raw_score": v[0], "weighted": round(v[1], 2)} for k, v in scores.items()},
    }


def main():
    parser = argparse.ArgumentParser(description="Boring Business Scorecard Calculator")
    subparsers = parser.add_subparsers(dest="command")

    # Quick validation subparser
    qp = subparsers.add_parser("quick", help="Calculate Tier 1 Quick Validation score")
    qp.add_argument("--volume", type=int, required=True, help="Total monthly search volume")
    qp.add_argument("--difficulty", default="medium", help="Keyword difficulty or competition (low, medium, high, or 0-100)")
    qp.add_argument("--commercial-intent", action="store_true", help="Set if search queries show commercial/buying intent")
    qp.add_argument("--automatable", action="store_true", help="Set if product can run with high automation")
    qp.add_argument("--json", action="store_true", help="Output as JSON")

    # Deep validation subparser
    dp = subparsers.add_parser("deep", help="Calculate Tier 2 Deep Validation score (1-5 each)")
    dp.add_argument("--search", type=float, required=True, help="Search Demand (1-5)")
    dp.add_argument("--dist", type=float, required=True, help="Distribution Potential (1-5)")
    dp.add_argument("--organic", type=float, required=True, help="Organic Growth (1-5)")
    dp.add_argument("--auto", type=float, required=True, help="Automation Level (1-5)")
    dp.add_argument("--wtp", type=float, required=True, help="Willingness to Pay (1-5)")
    dp.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.command == "quick":
        diff = args.difficulty
        try:
            diff = float(diff)
        except ValueError:
            pass
        res = calculate_quick(args.volume, diff, args.commercial_intent, args.automatable)
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"\n=== {res['tier']} ===")
            print(f"Total Score: {res['score_total']}/{res['max_score']}")
            print(f"Decision:    {res['decision']}")
            print("\nKey Signals:")
            for s in res["signals"]:
                print(f"  {s}")
            print()

    elif args.command == "deep":
        res = calculate_deep(args.search, args.dist, args.organic, args.auto, args.wtp)
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"\n=== {res['tier']} ===")
            print(f"Overall Score: {res['overall_score']} / 5.0")
            print(f"Decision:      {res['decision']}")
            print("\nBreakdown:")
            for k, v in res["breakdown"].items():
                print(f"  - {k}: {v['raw_score']}/5 (Weighted: {v['weighted']})")
            print()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
