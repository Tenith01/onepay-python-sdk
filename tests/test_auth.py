"""Tests for hash generation and auth utilities."""

from __future__ import annotations

import hashlib

from onepay._auth import build_auth_header, build_json_header, generate_hash


class TestGenerateHash:
    """Tests for the SHA-256 hash generation function."""

    def test_basic_hash(self):
        """Hash should match manual SHA-256 computation."""
        app_id = "APP123"
        currency = "LKR"
        amount = "100.00"
        hash_salt = "SALT456"

        expected_payload = f"{app_id}{currency}{amount}{hash_salt}"
        expected_hash = hashlib.sha256(expected_payload.encode("utf-8")).hexdigest()

        result = generate_hash(app_id, currency, amount, hash_salt)
        assert result == expected_hash

    def test_hash_is_lowercase_hex(self):
        """Hash output should be lowercase hexadecimal."""
        result = generate_hash("a", "b", "c", "d")
        assert result == result.lower()
        assert all(c in "0123456789abcdef" for c in result)

    def test_hash_length(self):
        """SHA-256 produces a 64-character hex string."""
        result = generate_hash("app", "LKR", "500.00", "salt")
        assert len(result) == 64

    def test_different_inputs_different_hashes(self):
        """Different inputs must produce different hashes."""
        h1 = generate_hash("APP1", "LKR", "100.00", "SALT")
        h2 = generate_hash("APP2", "LKR", "100.00", "SALT")
        h3 = generate_hash("APP1", "USD", "100.00", "SALT")
        h4 = generate_hash("APP1", "LKR", "200.00", "SALT")

        assert len({h1, h2, h3, h4}) == 4

    def test_no_separators(self):
        """Values are concatenated with no separators."""
        # "APP" + "LKR" + "100.00" + "SALT" = "APPLKR100.00SALT"
        expected = hashlib.sha256(b"APPLKR100.00SALT").hexdigest()
        assert generate_hash("APP", "LKR", "100.00", "SALT") == expected


class TestBuildAuthHeader:
    """Tests for auth header construction."""

    def test_auth_header_includes_token(self):
        """Authorization header should contain the token."""
        headers = build_auth_header("my_token_123")
        assert headers["Authorization"] == "my_token_123"
        assert headers["Content-Type"] == "application/json"

    def test_json_header_no_auth(self):
        """JSON-only header should not include Authorization."""
        headers = build_json_header()
        assert "Authorization" not in headers
        assert headers["Content-Type"] == "application/json"
