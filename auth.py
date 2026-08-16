"""A minimal username / password check.

Passwords are never stored in plain text: users.json only holds a random salt
and a SHA-256 hash. That is fine for an internal survey. For anything exposed
to the internet, use a real identity provider (SSO, OAuth, Authelia, ...) or
the `streamlit-authenticator` package.

Add a user from the command line:

    python auth.py add alice
"""

from __future__ import annotations

import hashlib
import hmac
import json
import secrets
import sys
from getpass import getpass
from pathlib import Path

USERS_FILE = Path(__file__).parent / "users.json"

# Created automatically the first time the app starts, so you can log in
# straight away. Delete it (or the user) once you have added real accounts.
DEMO_USER = ("demo", "demo1234")


def _hash_password(password: str, salt: str) -> str:
    """Salted SHA-256 hash of a password."""
    return hashlib.sha256((salt + password).encode("utf-8")).hexdigest()


def load_users() -> dict:
    """Read users.json, or return an empty dict if it does not exist yet."""
    if not USERS_FILE.exists():
        return {}
    return json.loads(USERS_FILE.read_text(encoding="utf-8"))


def add_user(username: str, password: str) -> None:
    """Add or overwrite a user in users.json."""
    users = load_users()
    salt = secrets.token_hex(16)
    users[username] = {"salt": salt, "hash": _hash_password(password, salt)}
    USERS_FILE.write_text(json.dumps(users, indent=2), encoding="utf-8")


def ensure_demo_user() -> None:
    """Make sure at least one account exists, so the app is usable at once."""
    if not load_users():
        add_user(*DEMO_USER)


def check_credentials(username: str, password: str) -> bool:
    """True if the username exists and the password matches."""
    user = load_users().get(username)
    if user is None:
        return False
    expected = _hash_password(password, user["salt"])
    # compare_digest avoids leaking information through timing differences.
    return hmac.compare_digest(user["hash"], expected)


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "add":
        print("usage: python auth.py add <username>")
        raise SystemExit(1)

    name = sys.argv[2]
    pw = getpass(f"Password for {name}: ")
    if pw != getpass("Repeat password: "):
        print("Passwords do not match.")
        raise SystemExit(1)

    add_user(name, pw)
    print(f"Saved {name} to {USERS_FILE}")
