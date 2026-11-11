# ==========================================================
# Task 2: Security Event Logger
# Name: Emmanuel Kalu
# Banner ID: B01808189
# Module: COMP08101 Programming for Cyber Security
# ==========================================================
# Asks for a username and password until the correct details
# are entered, and prints an event log entry for every try.
# ==========================================================

import random                   # used to create a random event ID
import socket                   # used to find this computer's IP address
from datetime import datetime   # used to create the timestamp

# Correct login details
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "admin123"


def get_ip_address():
    """Return this computer's IP address.
    If there is no network connection, return the local address instead."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except OSError:
        # Happens if the computer is offline
        return "127.0.0.1"


def print_event(username, event):
    """Print one security event log entry."""
    event_id = random.randint(1000, 9999)                          # 4-digit ID
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")       # readable time
    ip_address = get_ip_address()

    print(f"Event ID: {event_id}")
    print(f"Username: {username}")
    print(f"IP Address: {ip_address}")
    print(f"Event: {event}")
    print(f"Timestamp: {timestamp}")
    print()


# ---------------- Main program ----------------
print("SECURITY EVENT LOG")
print("==================")

logged_in = False

# Keep asking until the correct username and password are entered
while not logged_in:
    username = input("Enter username: ").strip()
    password = input("Enter password: ")
    print()

    # Decide whether this attempt is a success or a failure
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print_event(username, "Successful login")
        logged_in = True
    else:
        print_event(username, "Failed login")

print("Login complete. All attempts have been logged above.")
