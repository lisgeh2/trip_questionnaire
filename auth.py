"""A minimal username / password check.

Passwords are stored in plain text: users.json holds the password exactly as
typed. That is fine for a throwaway internal tool where the accounts guard
nothing of value. For anything exposed to the internet, or if any user might
reuse a password from elsewhere, use a real identity provider (SSO, OAuth,
Authelia, ...) or the `streamlit-authenticator` package.

Add a user from the command line:

    python auth.py add alice
"""

from __future__ import annotations

import json
import sys
from getpass import getpass
from pathlib import Path

USERS_FILE = Path(__file__).parent / "users.json"

# Created automatically the first time the app starts, so you can log in
# straight away. Delete it (or the user) once you have added real accounts.
DEMO_USER = ("demo", "demo123")


def load_users() -> dict:
    """Read users.json, or return an empty dict if it does not exist yet."""
    if not USERS_FILE.exists():
        return {}
    return json.loads(USERS_FILE.read_text(encoding="utf-8"))


def add_user(username: str, password: str) -> None:
    """Add or overwrite a user in users.json."""
    users = load_users()
    users[username] = {"password": password}
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
    return user["password"] == password


if __name__ == "__main__":
    users = load_users()
    print(users.get("demo"))
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