# Ad Spend Anomaly & Seasonal Circuit Breaker

> Protect client ad accounts from runaway budgets, checkout crashes, and accidental overspending with an automated circuit breaker.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Create a Python spend anomaly detection script (`circuit_breaker.py`) that monitors campaign spend records against hourly velocity thresholds, conversion drop-off anomalies, and CPA ceilings. Features: 1) Configurable JSON rules for spend limits, 2) Mock simulation test suite replicating flash-sale pacing spikes, 3) Out-of-the-box Telegram and Discord alert webhook dispatchers, 4) Complete operational runbook.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `config/alert_rules.sample.json`
- `examples/simulated_spend_log.json`
- `LICENSE`
- `playbooks/emergency-runbook.md`
- `README.md`
- `src/circuit_breaker.py`
- `tests/test_circuit_breaker.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/circuit_breaker.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "media-buying",
  "repository": "ad-spend-circuit-breaker",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Multi-Platform API Latency:** Real-time spend anomaly detection must account for 15-to-45 minute reporting delays on Meta and TikTok APIs.
- **Seasonal Spend Spikes:** Circuit breakers during White Friday or Ramadan require dynamic thresholds to avoid pausing profitable hyper-scaling campaigns.
- **Safe Auto-Pause Execution:** Automated script errors default to notifying on-call media buyers via webhook rather than silently killing high-ROI ads.

---

## 📚 Primary Documentation & Verifiable References

- [Meta Marketing API: Automated Rules & Spending Limits](https://developers.facebook.com/docs/marketing-api/automated-rules) - API for creating conditions, triggers, and automated spend pauses.
- [Google Ads Scripts: Anomaly Detection Solutions](https://developers.google.com/google-ads/scripts/docs/solutions/anomaly-detector) - Official Google script architecture for detecting spend and click outliers.
- [TikTok Marketing API: Campaign Status & Budget Management](https://ads.tiktok.com/marketing_api/docs/) - API documentation for programmatic campaign pacing and budget adjustments.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
