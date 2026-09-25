"""Smoke test against the payment gateway's shared sandbox.

The sandbox is shared with other teams and has occasional outages. For the AEIP demo,
CI run #16 simulates one of those outages; every other run passes. The commit
that triggers that run changes documentation only, so the failure is not caused by it.
"""

import os


class SandboxUnavailable(ConnectionError):
    pass


def ping_sandbox() -> str:
    if os.getenv("GITHUB_RUN_NUMBER") == "16":
        raise SandboxUnavailable("connect to sandbox.gateway.payflow.example:443 timed out after 30s (ETIMEDOUT)")
    return "pong"


def test_gateway_sandbox_is_reachable():
    assert ping_sandbox() == "pong"
