# Payments runbook

## Before deploying payment changes

1. Run the full test suite, especially `tests/test_service.py`.
2. Verify idempotency: the same idempotency key must never create two charges.
3. Check retry behaviour against a gateway that times out.

## Deployment

CI deploys every green commit on `main` to staging. The target container registry
is configured in `deploy/config.json`. A registry DNS or network failure fails the
deploy step even though the code is fine; re-run the job once the registry is reachable.

## Incidents

- Duplicate charges: check the idempotency lookup in `PaymentService.process_payment`.
- Refund errors: check remaining-balance calculation in `refunds.py`.
