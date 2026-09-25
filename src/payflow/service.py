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
        if idempotency_key in self._processed:
            return self._processed[idempotency_key]
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                charge_id = self.gateway.charge(amount, idempotency_key)
                break
            except GatewayError:
                if attempt == MAX_ATTEMPTS:
                    raise
        self._processed[idempotency_key] = charge_id
        return charge_id
