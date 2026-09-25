# Architecture

Requests arrive at `PaymentService.process_payment(amount, idempotency_key)`.
The service keeps a map of processed idempotency keys to charge IDs so a retried
HTTP request never charges a customer twice. New keys are charged through the
gateway; transient `GatewayError`s are retried up to `MAX_ATTEMPTS` times.

Refunds (`refunds.py`) look up the original charge and refund against it.
Order totals (`orders.py`) are computed in paise to avoid floating-point errors.
Dashboard API tokens (`auth.py`) are HMAC-signed and expire after `TTL_SECONDS`.

CI (`.github/workflows/ci.yml`) runs the test suite on every push and pull request,
then deploys `main` to staging with `scripts/deploy.py`.
