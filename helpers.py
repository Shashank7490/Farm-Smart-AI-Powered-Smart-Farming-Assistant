"""
helpers.py
-----------
Shared helper utilities.
"""

import datetime


def format_date(date_obj: datetime.date) -> str:
    """Format date for display."""
    return date_obj.strftime("%d %b %Y")


def safe_float(value, default=0.0):
    """Convert to float safely."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def clamp(value, min_val, max_val):
    """Clamp value between min and max."""
    return max(min_val, min(value, max_val))