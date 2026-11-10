# ==========================================================
# Task 1: Security Tool
# Name: Emmanuel Kalu
# Banner ID: B01808189
# Module: COMP08101 Programming for Cyber Security
# ==========================================================
# A basic security tool for a small organisation.
# The user must log in first, then chooses options from a
# security menu until they select Exit.
# ==========================================================

# ---------- Stored credentials and settings ----------
# These values act as the "correct" details the program checks against
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

CORRECT_PASSWORD = "Cyber123"       # used by the Security Event Counter
SECRET_PASSWORD = "letmein"         # used by the Brute-Force Simulation
MAX_GUESSES = 5                     # maximum brute-force attempts
MAX_LOGIN_ATTEMPTS = 3              # maximum failed logins before freezing


def authenticate(username, password):
    """Return True if the username and password match the stored credentials."""
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD


def security_event_counter():
    """Ask for a password 10 times, count correct and incorrect entries,
    then show the percentage of incorrect entries and raise an alert if over 50%."""
    correct = 0
    incorrect = 0

    print("\n--- Security Event Counter ---")

    # A for loop is used because we know it must run exactly 10 times
    for attempt in range(1, 11):
        password = input(f"Attempt {attempt}/10 - Enter password: ")

        # Compare each entry with the stored password
        if password == CORRECT_PASSWORD:
            correct += 1
        else:
            incorrect += 1

    # Work out the percentage of incorrect entries
    percentage = (incorrect / 10) * 100

    print("\nResults")
    print("-----------------------")
    print(f"Correct passwords:   {correct}")
    print(f"Incorrect passwords: {incorrect}")
    print(f"Incorrect percentage: {percentage}%")

    # Raise an alert only when more than half the attempts were wrong
    if percentage > 50:
        print("ALERT: More than 50% of password attempts were incorrect!")
    else:
        print("No alert: incorrect attempts are within the normal range.")


def brute_force_simulation():
    """Let the user guess a predefined password up to MAX_GUESSES times."""
    attempts = 0
    found = False

    print("\n--- Brute-Force Simulation ---")
    print(f"You have a maximum of {MAX_GUESSES} attempts.")

    # Keep looping while attempts remain and the password has not been found
    while attempts < MAX_GUESSES and not found:
        guess = input("Enter a password guess: ")
        attempts += 1

        if guess == SECRET_PASSWORD:
            found = True
            print(f"Password found after {attempts} attempt(s)!")
        else:
            print(f"Incorrect guess. Attempts used: {attempts}/{MAX_GUESSES}")

    # If the loop ended without finding the password, the limit was reached
    if not found:
        print("Maximum number of attempts reached. Simulation stopped.")


def login_authentication():
    """Ask for a username and password, allowing three failed logins
    before the account is frozen for 24 hours."""
    failed_logins = 0

    print("\n--- Login Authentication ---")

    # Keep asking until the user logs in or the limit is reached
    while failed_logins < MAX_LOGIN_ATTEMPTS:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if authenticate(username, password):
            print("Authentication succeeded.")
            return      # leave the function on success
        else:
            failed_logins += 1
            print(f"Authentication failed. Failed attempts: {failed_logins}/{MAX_LOGIN_ATTEMPTS}")

    # Only reached when the user failed three times
    print("Account frozen for 24 hours due to too many failed logins.")


def show_menu():
    """Display the security menu options."""
    print("\n==============================")
    print("        SECURITY MENU")
    print("==============================")
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")


# ---------------- Main program ----------------
print("Welcome to the Security Tool")
print("Please log in to continue.")

# The user must log in before seeing the menu
logged_in = False
while not logged_in:
    username = input("Username: ")
    password = input("Password: ")

    if authenticate(username, password):
        logged_in = True
        print("Login successful.")
    else:
        print("Invalid username or password. Please try again.")

# Main menu loop: keeps running until the user chooses Exit
while True:
    show_menu()
    choice = input("Select an option (1-4): ").strip()

    # if/elif/else decides which function to run
    if choice == "1":
        security_event_counter()
    elif choice == "2":
        brute_force_simulation()
    elif choice == "3":
        login_authentication()
    elif choice == "4":
        print("Thank you for using the security tool")
        break       # stop the loop and end the program
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
