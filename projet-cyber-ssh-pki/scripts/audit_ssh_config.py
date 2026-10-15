#!/usr/bin/env python3
\"\"\"Basic explicit-line audit of sshd_config; not a full OpenSSH parser.\"\"\"
import argparse
from pathlib import Path

CHECKS = {
    "PermitRootLogin": {"no"},
    "PasswordAuthentication": {"no"},
    "PubkeyAuthentication": {"yes"},
    "X11Forwarding": {"no"},
    "MaxAuthTries": {"4", "3", "2"},
}

def read_config(path):
    values = {}
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            values[parts[0].lower()] = parts[1].lower()
    return values

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="/etc/ssh/sshd_config")
    args = parser.parse_args()
    values = read_config(args.config)
    for key, expected in CHECKS.items():
        value = values.get(key.lower(), "unset/default")
        status = "REVIEW" if value == "unset/default" else ("PASS" if value in expected else "REVIEW")
        print(f"{status:6} {key:28} value={value} expected={','.join(sorted(expected))}")
    print("NOTE: Includes, Match blocks and OpenSSH defaults are not evaluated by this script.")
    print("For effective configuration, review: sudo sshd -T")
if __name__ == "__main__":
    main()
