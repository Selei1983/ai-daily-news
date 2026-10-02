#!/usr/bin/env python3
"""Offline tracked-file guard. Reports locations only, never matching values."""
import re
import subprocess
from pathlib import Path

RULES = {
    "literal secret argument": re.compile(r"--secret(?:\s+|=)[\"']?[A-Za-z0-9_-]{16,}"),
    "literal credential field": re.compile(
        r"(?i)(?:app\s*secret|access\s*token|secret\s*key|api\s*key)"
        r"[：:=\s]+[\"']?[A-Za-z0-9_-]{16,}"
    ),
    "hardcoded WordPress password": re.compile(r"^APP_PASSWORD\s*=\s*[\"'][^\"']+"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def findings(text):
    for line_number, line in enumerate(text.splitlines(), 1):
        for kind, pattern in RULES.items():
            if pattern.search(line):
                yield line_number, kind


def main():
    root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
    paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
    count = 0
    for name in filter(None, paths):
        path = root / name
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line, kind in findings(text):
            print(f"{name}:{line}: {kind}")
            count += 1
    print(f"Credential-pattern findings: {count}")
    return bool(count)


if __name__ == "__main__":
    raise SystemExit(main())
