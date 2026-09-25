from payflow.orders import order_total


def test_order_total_sums_items():
    items = [{"price": 25_000, "quantity": 2}, {"price": 9_900, "quantity": 1}]
    assert order_total(items) == 59_900
def test_discount_code_is_applied():
    from payflow.orders import apply_discount

    assert apply_discount(10_000, "welcome10") == 9_000
    assert apply_discount(10_000, "unknown") == 10_000
