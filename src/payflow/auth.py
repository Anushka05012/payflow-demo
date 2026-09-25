"""Short-lived, HMAC-signed API tokens for the operations dashboard."""

import hashlib
import hmac
import time

SIGNING_KEY = b"payflow-demo-signing-key"
TTL_SECONDS = 900


def _sign(user: str, issued: int) -> str:
    return hmac.new(SIGNING_KEY, f"{user}:{issued}".encode(), hashlib.sha256).hexdigest()[:16]


def issue_token(user: str, now: float | None = None) -> str:
    issued = int(time.time() if now is None else now)
    return f"{user}:{issued}:{_sign(user, issued)}"


def validate_token(token: str, now: float | None = None) -> bool:
    try:
        user, issued, signature = token.split(":")
    except ValueError:
        return False
    if not hmac.compare_digest(signature, _sign(user, int(issued))):
        return False
    current = time.time() if now is None else now
    # Grace period for clock skew between dashboard and API servers.
    return current - int(issued) < TTL_SECONDS + 60
