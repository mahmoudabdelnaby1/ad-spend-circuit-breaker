#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

def evaluate_spend(log_path, rules_path):
    with open(rules_path, "r", encoding="utf-8") as f:
        rules = json.load(f)
    with open(log_path, "r", encoding="utf-8") as f:
        logs = json.load(f)

    alerts = []
    for entry in logs:
        campaign = entry.get("campaign_name")
        hourly_spend = entry.get("hourly_spend", 0)
        max_hourly = rules.get("max_hourly_spend_sar", 500)
        cpa = entry.get("hourly_cpa", 0)
        max_cpa = rules.get("max_allowable_cpa_sar", 100)

        if hourly_spend > max_hourly:
            alerts.append({
                "severity": "CRITICAL",
                "campaign": campaign,
                "message": f"Hourly spend SAR {hourly_spend} breached limit of SAR {max_hourly}!",
                "circuit_tripped": True
            })
        elif cpa > max_cpa:
            alerts.append({
                "severity": "WARNING",
                "campaign": campaign,
                "message": f"Hourly CPA SAR {cpa} exceeded threshold SAR {max_cpa}.",
                "circuit_tripped": False
            })

    return {
        "status": "CIRCUIT_BREAKER_TRIPPED" if any(a["circuit_tripped"] for a in alerts) else "NORMAL",
        "total_alerts": len(alerts),
        "alerts": alerts
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--logs", required=True)
    p.add_argument("--rules", required=True)
    args = p.parse_args()

    res = evaluate_spend(args.logs, args.rules)
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
