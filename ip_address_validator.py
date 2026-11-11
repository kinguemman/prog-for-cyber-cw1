# ==========================================================
# Task 3: IP Address Validator (using Function)
# Name: Emmanuel Kalu
# Banner ID: B01808189
# Module: COMP08101 Programming for Cyber Security
# ==========================================================
# Performs a basic format check on an IPv4 address using
# string operations inside a function called validate_ip().
# ==========================================================


def validate_ip(ip):
    """Return True if the IP address passes the basic format checks,
    otherwise return False."""

    # Remove spaces from the start and end of the input
    ip = ip.strip()

    # Check the address contains dots at all
    if "." not in ip:
        return False

    # An IPv4 address must have exactly three dots
    if ip.count(".") != 3:
        return False

    # Split the address into its parts using the dots
    parts = ip.split(".")

    # There must be exactly four parts (octets)
    if len(parts) != 4:
        return False

    # Check each part one at a time
    for part in parts:
        # Each part must only contain digits (this rejects "one" or "")
        if not part.isdigit():
            return False

        # Convert the text to a number so it can be compared
        number = int(part)

        # Each number must be between 0 and 255
        if number < 0 or number > 255:
            return False

    # All checks passed
    return True


# ---------------- Main program ----------------
ip_address = input("Enter an IP address: ")

# Call the function and display the result
if validate_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")
