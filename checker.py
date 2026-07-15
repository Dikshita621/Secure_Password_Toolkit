import math
import string


def check_password_strength(password):
    """
    Checks the strength of a password.

    Returns:
        strength (str)
        score (float)
        entropy (float)
        suggestions (list)
    """

    score = 0
    suggestions = []

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    # Length
    if len(password) >= 8:
        score += 0.25
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase
    if has_upper:
        score += 0.25
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase
    if has_lower:
        score += 0.25
    else:
        suggestions.append("Add lowercase letters")

    # Numbers / Symbols
    if has_digit or has_symbol:
        score += 0.25
    else:
        suggestions.append("Add numbers or symbols")

    # Strength label
    if score <= 0.25:
        strength = "Weak"

    elif score <= 0.50:
        strength = "Medium"

    elif score <= 0.75:
        strength = "Strong"

    else:
        strength = "Very Strong"

    # Entropy calculation
    pool = 0

    if has_lower:
        pool += 26

    if has_upper:
        pool += 26

    if has_digit:
        pool += 10

    if has_symbol:
        pool += len(string.punctuation)

    entropy = 0

    if pool > 0:
        entropy = round(len(password) * math.log2(pool), 2)

    return strength, score, entropy, suggestions