"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""
import re

def has_vowel(string):
    """Return True iff the string contains one or more vowels."""
    return bool(re.search(r'[aeiou]', string, re.IGNORECASE))


def is_integer(string):
    """Return True iff the string represents a valid integer."""
    return bool(re.match(r'[+-]?\d+$', string))

def is_fraction(string):
    """Return True iff the string represents a valid fraction."""
    #return bool(re.match(r'[+-]?\d+/(1-9\d*)|(0-9\d+)$', string))

def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""
    return bool(re.search(r'\d\d\d\d-\d\d-\d\d',string))


def is_number(string):
    """Return True iff the string represents a decimal number."""


def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""
