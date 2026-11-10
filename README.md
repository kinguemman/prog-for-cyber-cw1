# Task 1: Security Tool

**Name:** Emmanuel Kalu  
**Banner ID:** B01808189  
**Campus:** Lanarkshire Campus                                                                                                                                                                                                 
**Module:** COMP08101 Programming for Cyber Security

## What the program does

A basic security tool for a small organisation. The user must log in first. After logging in, a security menu is shown and the program keeps running until the user chooses **Exit**.

| Option | Function |
|---|---|
| 1. Security Event Counter | Asks for a password 10 times, counts correct and incorrect entries, shows the percentage of incorrect entries, and raises an alert if it is more than 50%. |
| 2. Brute-Force Simulation | Lets the user guess a predefined password. Stops when the password is found or when the maximum of 5 attempts is reached. |
| 3. Login Authentication | Asks for a username and password. Allows three failed logins, then displays that the account is frozen for 24 hours. |
| 4. Exit | Displays "Thank you for using the security tool" and ends the program. |

## Python concepts used

- Variables, strings and integers
- `if` / `elif` / `else` decisions
- `for` loops (fixed 10 attempts) and `while` loops (menu, login retries)
- `break` to leave the menu loop
- Functions with parameters and return values (`authenticate()`)
- Comparison and logical operators (`==`, `<`, `>`, `and`, `not`)
- f-strings for formatted output

## Test credentials

| Purpose | Value |
|---|---|
| Login username | `admin` |
| Login password | `admin123` |
| Event counter password | `Cyber123` |
| Brute-force password | `letmein` |

## How to run

1. Open the project folder in VS Code.
2. Open a terminal in VS Code (**Terminal → New Terminal**).
3. Run:

```bash
python security_tool.py
```

Or open `security_tool.py` and click **Run → Start Debugging → Python Debugger**.

## Example output

```
Welcome to the Security Tool
Please log in to continue.
Username: admin
Password: admin123
Login successful.

==============================
        SECURITY MENU
==============================
1. Security Event Counter
2. Brute-Force Simulation
3. Login Authentication
4. Exit
Select an option (1-4): 4
Thank you for using the security tool
```

## Screenshots

<!-- Add your output screenshots here, e.g. ![Menu](screenshots/menu.png) -->

## Licence

MIT License. See `LICENSE`.
