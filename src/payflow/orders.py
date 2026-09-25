"""Order totals, in paise."""


def order_total(items: list[dict]) -> int:
    return sum(item["price"] * item["quantity"] for item in items)
DISCOUNT_CODES = {"WELCOME10": 10, "FESTIVE20": 20}


def apply_discount(total: int, code: str | None) -> int:
    percent = DISCOUNT_CODES.get((code or "").upper(), 0)
    return total - total * percent // 100
def format_amount(paise: int, currency: str = "INR") -> str:
    symbol = {"INR": "₹", "USD": "$"}.get(currency, currency + " ")
    return f"{symbol}{paise // 100:,}.{paise % 100:02d}"
