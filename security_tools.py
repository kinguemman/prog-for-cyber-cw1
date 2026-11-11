# ==========================================================
# Task 5: Reusable Cyber Security Utilities (module file)
# Name: Emmanuel Kalu
# Banner ID: B01808189
# Module: COMP08101 Programming for Cyber Security
# ==========================================================
# A user-defined module holding reusable security functions.
# It is imported and used by main.py.
# ==========================================================

import random   # used to pick the password length and characters

# Character groups used when generating passwords
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SYMBOLS = "!@#$%"

MIN_LENGTH = 10     # minimum length for a strong password


def validate_password(password):
    """Return True if the password is at least MIN_LENGTH characters
    and contains at least one letter, one digit and one symbol."""
    has_letter = False
    has_digit = False
    has_symbol = False

    # Check the length first
    if len(password) < MIN_LENGTH:
        return False

    # Look at every character and record which types appear
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum() and char != " ":
            has_symbol = True       # anything that isn't a letter, digit or space

    # Only valid if all three types were found
    return has_letter and has_digit and has_symbol


def validate_ip(ip):
    """Return True if the IP address has three dots, four numbers,
    and every number is between 0 and 255."""
    ip = ip.strip()

    if ip.count(".") != 3:
        return False

    parts = ip.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        number = int(part)
        if number < 0 or number > 255:
            return False

    return True


def generate_password():
    """Generate a strong random password between 10 and 16 characters long,
    containing uppercase, lowercase, digits and symbols."""

    # Pick a random length each time the function is called
    length = random.randint(10, 16)

    # Start with one character from each group so variety is guaranteed
    characters = [
        random.choice(UPPERCASE),
        random.choice(LOWERCASE),
        random.choice(DIGITS),
        random.choice(SYMBOLS)
    ]

    # Fill the remaining length with characters from any group
    all_characters = UPPERCASE + LOWERCASE + DIGITS + SYMBOLS
    while len(characters) < length:
        characters.append(random.choice(all_characters))

    # Mix the characters into a random order so the first four
    # aren't always uppercase, lowercase, digit, symbol
    password = ""
    while len(characters) > 0:
        index = random.randint(0, len(characters) - 1)
        password += characters[index]
        del characters[index]

    return password
