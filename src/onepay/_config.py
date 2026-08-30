"""Configuration management for the OnePay SDK.

Loads credentials from constructor arguments or environment variables.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field

_DEFAULT_BASE_URL = "https://api.onepay.lk"
_DEFAULT_TIMEOUT = 30.0
_DEFAULT_MAX_RETRIES = 3


@dataclass
class OnePayConfig:
    """Holds all configuration for an OnePay client instance.

    Values can be provided explicitly or fall back to environment variables:
        - ``ONEPAY_APP_ID``
        - ``ONEPAY_HASH_SALT``
        - ``ONEPAY_APP_TOKEN``
        - ``ONEPAY_API_KEY``
        - ``ONEPAY_ACCESS_TOKEN``
        - ``ONEPAY_BASE_URL``
    """

    app_id: str = ""
    hash_salt: str = ""
    app_token: str = ""
    api_key: str = ""
    access_token: str = ""
    base_url: str = _DEFAULT_BASE_URL
    timeout: float = _DEFAULT_TIMEOUT
    max_retries: int = _DEFAULT_MAX_RETRIES
    debug: bool = False

    # Internal — resolved after __post_init__
    _resolved: bool = field(default=False, repr=False, init=False)

    def __post_init__(self) -> None:
        """Resolve unset fields from environment variables."""
        if not self._resolved:
            self.app_id = self.app_id or os.environ.get("ONEPAY_APP_ID", "")
            self.hash_salt = self.hash_salt or os.environ.get("ONEPAY_HASH_SALT", "")
            self.app_token = self.app_token or os.environ.get("ONEPAY_APP_TOKEN", "")
            self.api_key = self.api_key or os.environ.get("ONEPAY_API_KEY", "")
            self.access_token = self.access_token or os.environ.get("ONEPAY_ACCESS_TOKEN", "")
            self.base_url = self.base_url or os.environ.get("ONEPAY_BASE_URL", _DEFAULT_BASE_URL)
            # Strip trailing slashes from base URL
            self.base_url = self.base_url.rstrip("/")
            self._resolved = True

    def get_app_token_or_raise(self) -> str:
        """Return the app token, raising if not configured."""
        if not self.app_token:
            raise ValueError(
                "app_token is required for this operation. "
                "Pass it to the OnePay constructor or set the ONEPAY_APP_TOKEN environment variable."  # noqa: E501
            )
        return self.app_token

    def get_api_key_or_raise(self) -> str:
        """Return the API key, raising if not configured."""
        if not self.api_key:
            raise ValueError(
                "api_key is required for this operation. "
                "Pass it to the OnePay constructor or set the ONEPAY_API_KEY environment variable."
            )
        return self.api_key

    def get_access_token_or_raise(self) -> str:
        """Return the access token, raising if not configured."""
        if not self.access_token:
            raise ValueError(
                "access_token is required for this operation. "
                "Pass it to the OnePay constructor or set the ONEPAY_ACCESS_TOKEN environment variable."  # noqa: E501
            )
        return self.access_token

    def get_hash_salt_or_raise(self) -> str:
        """Return the hash salt, raising if not configured."""
        if not self.hash_salt:
            raise ValueError(
                "hash_salt is required for this operation. "
                "Pass it to the OnePay constructor or set the ONEPAY_HASH_SALT environment variable."  # noqa: E501
            )
        return self.hash_salt

    def get_app_id_or_raise(self) -> str:
        """Return the app ID, raising if not configured."""
        if not self.app_id:
            raise ValueError(
                "app_id is required for this operation. "
                "Pass it to the OnePay constructor or set the ONEPAY_APP_ID environment variable."
            )
        return self.app_id

    def redacted_repr(self) -> str:
        """Return a string representation with secrets redacted."""

        def _redact(val: str) -> str:
            if not val:
                return "(not set)"
            if len(val) <= 8:
                return "***"
            return val[:4] + "***" + val[-4:]

        return (
            f"OnePayConfig("
            f"app_id={_redact(self.app_id)!r}, "
            f"hash_salt={_redact(self.hash_salt)!r}, "
            f"app_token={_redact(self.app_token)!r}, "
            f"api_key={_redact(self.api_key)!r}, "
            f"access_token={_redact(self.access_token)!r}, "
            f"base_url={self.base_url!r}, "
            f"timeout={self.timeout}, "
            f"max_retries={self.max_retries}, "
            f"debug={self.debug}"
            f")"
        )
