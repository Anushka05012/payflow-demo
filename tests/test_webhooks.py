import hashlib
import hmac

from payflow.webhooks import verify_callback

KEY = b"callback-key"
BODY = b'{"event": "charge.succeeded"}'


def test_valid_signature_is_accepted():
    signature = "sha256=" + hmac.new(KEY, BODY, hashlib.sha256).hexdigest()
    assert verify_callback(BODY, signature, KEY)


def test_forged_short_signature_is_rejected():
    assert not verify_callback(BODY, "sha256=abc", KEY)
