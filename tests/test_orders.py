from payflow.orders import order_total


def test_order_total_sums_items():
    items = [{"price": 25_000, "quantity": 2}, {"price": 9_900, "quantity": 1}]
    assert order_total(items) == 59_900
