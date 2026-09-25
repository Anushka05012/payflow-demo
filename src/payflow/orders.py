"""Order totals, in paise."""


def order_total(items: list[dict]) -> int:
    return sum(item["price"] * item["quantity"] for item in items)
