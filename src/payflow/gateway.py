"""In-memory payment gateway used by the service and tests."""


class GatewayError(Exception):
    """A transient gateway failure that is safe to retry."""


class FakeGateway:
    def __init__(self, fail_times: int = 0):
        self.charges: list[dict] = []
        self.refunds: list[dict] = []
        self._fail_times = fail_times

    def charge(self, amount: int, reference: str) -> str:
        if self._fail_times > 0:
            self._fail_times -= 1
            raise GatewayError("gateway timeout")
        charge_id = f"ch_{len(self.charges) + 1}"
        self.charges.append({"id": charge_id, "amount": amount, "reference": reference})
        return charge_id

    def refund(self, charge_id: str, amount: int) -> str:
        refund_id = f"re_{len(self.refunds) + 1}"
        self.refunds.append({"id": refund_id, "charge_id": charge_id, "amount": amount})
        return refund_id

    def get_charge(self, charge_id: str) -> dict:
        return next(charge for charge in self.charges if charge["id"] == charge_id)
