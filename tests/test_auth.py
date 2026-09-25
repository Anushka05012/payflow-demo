from payflow.auth import TTL_SECONDS, issue_token, validate_token


def test_fresh_token_is_valid():
    token = issue_token("ops", now=1_000)
    assert validate_token(token, now=1_010)


def test_tampered_token_is_rejected():
    user, issued, signature = issue_token("ops", now=1_000).split(":")
    assert not validate_token(f"admin:{issued}:{signature}", now=1_010)


def test_token_is_invalid_long_after_expiry():
    token = issue_token("ops", now=1_000)
    assert not validate_token(token, now=1_000 + TTL_SECONDS + 3_600)
def test_token_is_rejected_just_after_expiry():
    token = issue_token("ops", now=1_000)
    assert not validate_token(token, now=1_000 + TTL_SECONDS + 30)
