from payflow.gateway import FakeGateway
from payflow.refunds import refund_payment
from payflow.service import PaymentService


def test_full_refund_returns_whole_amount():
    gateway = FakeGateway()
    charge_id = PaymentService(gateway).process_payment(30_000, "order-9")
    refund_payment(gateway, charge_id)
    assert gateway.refunds[0]["amount"] == 30_000
def test_partial_refunds_until_balance_is_used():
    gateway = FakeGateway()
    charge_id = PaymentService(gateway).process_payment(30_000, "order-10")
    refund_payment(gateway, charge_id, 10_000)
    refund_payment(gateway, charge_id)
    assert [item["amount"] for item in gateway.refunds] == [10_000, 20_000]
