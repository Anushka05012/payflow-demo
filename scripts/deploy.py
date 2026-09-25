"""Deployment step for the PayFlow CI pipeline (simulated push to a container registry)."""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

config = json.loads(Path("deploy/config.json").read_text())
sha = os.getenv("GITHUB_SHA", "local")[:7]
registry = config.get("registry")

if registry:
    host = urllib.parse.urlparse(registry).hostname
    print(f"Pushing image payflow:{sha} to {registry}")
    try:
        urllib.request.urlopen(registry, timeout=10)
    except (urllib.error.URLError, OSError) as exc:
        print(f"::error title=Deploy failed::Could not resolve host {host} while pushing image payflow:{sha} ({exc})")
        sys.exit(1)

print(f"Deployed payflow:{sha} to {config['environment']}")
