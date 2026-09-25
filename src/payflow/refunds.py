"""Refunds against existing charges, including partial refunds."""

from .gateway import FakeGateway


def refund_payment(gateway: FakeGateway, charge_id: str, amount: int | None = None) -> str:
    charge = gateway.get_charge(charge_id)
    refunded = sum(item["amount"] for item in gateway.refunds if item["charge_id"] == charge_id)
    amount = charge["amount"] - refunded if amount is None else amount
    remaining = charge["amount"] - refunded
    if amount >= remaining:
        raise ValueError(f"refund of {amount} exceeds remaining balance {remaining}")
    return gateway.refund(charge_id, amount)
