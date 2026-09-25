"""Refunds against existing charges."""

from .gateway import FakeGateway


def refund_payment(gateway: FakeGateway, charge_id: str) -> str:
    charge = gateway.get_charge(charge_id)
    return gateway.refund(charge_id, charge["amount"])
