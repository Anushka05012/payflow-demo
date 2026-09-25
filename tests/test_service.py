import pytest

from payflow.gateway import FakeGateway
from payflow.service import PaymentService


def test_charges_customer_once():
    gateway = FakeGateway()
    service = PaymentService(gateway)
    assert service.process_payment(50_000, "order-1") == "ch_1"
    assert len(gateway.charges) == 1


def test_duplicate_request_is_idempotent():
    gateway = FakeGateway()
    service = PaymentService(gateway)
    first = service.process_payment(50_000, "order-1")
    second = service.process_payment(50_000, "order-1")
    assert first == second
    assert len(gateway.charges) == 1


def test_rejects_non_positive_amount():
    with pytest.raises(ValueError):
        PaymentService(FakeGateway()).process_payment(0, "order-2")
