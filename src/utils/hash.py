from argon2 import PasswordHasher
from .._typing import Argon2Hash

hasher = PasswordHasher()

def hash(raw: str) -> Argon2Hash:
    """Hash a string using Argon2."""
    return Argon2Hash(hasher.hash(raw))
    create_account = create_account
