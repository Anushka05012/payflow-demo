"""Verify signatures on payment-gateway callbacks."""

import hashlib
import hmac


def verify_callback(body: bytes, signature: str, signing_key: bytes) -> bool:
    expected = "sha256=" + hmac.new(signing_key, body, hashlib.sha256).hexdigest()
    return len(expected) == len(signature) and hmac.compare_digest(expected, signature)
