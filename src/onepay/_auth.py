"""Authentication utilities for the OnePay SDK.

Provides SHA-256 hash generation for payment requests and auth header
construction for different API endpoint groups.
"""

from __future__ import annotations

import hashlib


def generate_hash(app_id: str, currency: str, amount: str, hash_salt: str) -> str:
    """Generate SHA-256 hash for OnePay payment requests.

    The hash is computed as ``SHA256(app_id + currency + amount + hash_salt)``
    with all values concatenated as plain strings with no separators.

    Args:
        app_id: Your OnePay application identifier.
        currency: Three-letter ISO currency code (e.g., ``"LKR"``).
        amount: The transaction amount as a string (e.g., ``"100.00"``).
        hash_salt: Your OnePay hash salt (secret key).

    Returns:
        Lowercase hexadecimal SHA-256 hash string.

    Example:
        >>> generate_hash("APP123", "LKR", "100.00", "SALT456")
        'a1b2c3...'
    """
    payload = f"{app_id}{currency}{amount}{hash_salt}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_auth_header(token: str) -> dict[str, str]:
    """Build the Authorization header dictionary.

    Args:
        token: The bearer/API token value.

    Returns:
        Dictionary with ``Authorization`` and ``Content-Type`` headers.
    """
    return {
        "Authorization": token,
        "Content-Type": "application/json",
    }


def build_json_header() -> dict[str, str]:
    """Build a basic JSON Content-Type header (no auth).

    Returns:
        Dictionary with ``Content-Type`` header only.
    """
    return {
        "Content-Type": "application/json",
    }
