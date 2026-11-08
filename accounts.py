import hashlib
import secrets
from getpass import getpass

from tinydb import Query

from player import new_player


def password_hash(password, salt):
    # TinyDB can store the result of .hex() as ordinary text.
    result = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 600_000)
    return result.hex()


def authenticate(accounts):
    while True:
        choice = input("[1] Register  [2] Log in  [0] Exit: ").strip()
        if choice == "0":
            return None
        if choice not in ("1", "2"):
            print("Enter 1, 2, or 0.")
            continue

        username = input("Username: ").strip().lower()
        account = accounts.get(Query().username == username)
        if choice == "1":
            if not username.isalnum() or not 3 <= len(username) <= 20:
                print("Use 3 to 20 letters or digits for your username.")
                continue
            if account is not None:
                print("That username is already taken.")
                continue
            password = getpass("New password (6+ characters, typing is hidden): ")
            if len(password) < 6:
                print("Use at least 6 characters.")
                continue
            salt = secrets.token_hex(16)
            accounts.insert({
                "username": username,
                "salt": salt,
                "password_hash": password_hash(password, salt),
                "progress": new_player(),
            })
            print("Account created. Choose 2 to log in.")
        else:
            password = getpass("Password (typing is hidden): ")
            if account is not None:
                entered_hash = password_hash(password, account["salt"])
                if secrets.compare_digest(entered_hash, account["password_hash"]):
                    print(f"Welcome, {username}!")
                    return account
            print("Incorrect username or password.")


def save_game(accounts, account_id, player):
    # Update just the progress field of the logged-in account.
    accounts.update({"progress": player}, doc_ids=[account_id])
