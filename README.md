# PayFlow

PayFlow is a small payments service: it charges customers through a payment gateway,
exactly once per idempotency key, and supports refunds, order totals and short-lived
API tokens for the operations dashboard.

This repository is a demonstration project for **AEIP (AI Engineering Intelligence
Platform)**. Its history deliberately contains CI failures of different kinds so AEIP's
failure analysis, risk scoring and repository Q&A can be shown on real GitHub data.

## Layout

- `src/payflow/service.py` – payment processing with idempotency and retries
- `src/payflow/gateway.py` – in-memory payment gateway
- `src/payflow/refunds.py` – refunds against existing charges
- `src/payflow/orders.py` – order totals
- `src/payflow/auth.py` – dashboard API tokens
- `scripts/deploy.py` – deployment step used by CI
- `docs/` – runbook and architecture notes

Operational procedures live in [docs/runbook.md](docs/runbook.md).

## Development

```bash
pip install -r requirements-dev.txt
pytest
```
