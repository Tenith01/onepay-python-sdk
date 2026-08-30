"""Enumerations used across the OnePay SDK models."""

from __future__ import annotations

from enum import Enum


class Currency(str, Enum):
    """Supported OnePay currencies."""

    LKR = "LKR"
    USD = "USD"
    GBP = "GBP"
    EUR = "EUR"
    AUD = "AUD"
    JPY = "JPY"
    INR = "INR"
    CHF = "CHF"
    CAD = "CAD"
    SGD = "SGD"


class RefundReason(str, Enum):
    """Predefined refund reason codes accepted by the OnePay Refund API."""

    DUPLICATED = "DUPLICATED"
    FRAUDULENT = "FRAUDULENT"
    OUT_OF_ORDER = "OUT_OF_ORDER"
    REQUESTED_BY_CUSTOMER = "REQUESTED_BY_CUSTOMER"
    OTHER = "OTHER"


class SubscriptionInterval(str, Enum):
    """Subscription billing interval units."""

    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"


class PaymentStatus(str, Enum):
    """Payment status values."""

    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
