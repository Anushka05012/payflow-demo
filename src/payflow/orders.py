"""Order totals, in paise."""


def order_total(items: list[dict]) -> int:
    return sum(item["price"] * item["quantity"] for item in items)
DISCOUNT_CODES = {"WELCOME10": 10, "FESTIVE20": 20}


def apply_discount(total: int, code: str | None) -> int:
    percent = DISCOUNT_CODES.get((code or "").upper(), 0)
    return total - total * percent // 100
