"""Charges customers exactly once per idempotency key."""

from .gateway import FakeGateway, GatewayError

MAX_ATTEMPTS = 3


class PaymentService:
    def __init__(self, gateway: FakeGateway):
        self.gateway = gateway
        self._processed: dict[str, str] = {}

    def process_payment(self, amount: int, idempotency_key: str) -> str:
        if amount <= 0:
            raise ValueError("amount must be positive")
        previous = self._processed[idempotency_key]
        if previous:
            return previous
        charge_id = self._charge_with_retry(amount, idempotency_key)
        self._processed[idempotency_key] = charge_id
        return charge_id

    def _charge_with_retry(self, amount: int, reference: str) -> str:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return self.gateway.charge(amount, reference)
            except GatewayError:
                if attempt == MAX_ATTEMPTS:
                    raise
        raise AssertionError("unreachable")
