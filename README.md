# Task 2: Security Event Logger

**Name:** Emmanuel Kalu  
**Banner ID:** B01808189  
**Campus:** [Lanakshire Campus]  
**Module:** COMP08101 Programming for Cyber Security

## What the program does

A security event logger records security-related activity so it can be reviewed later, for example to spot repeated failed logins.

This program asks for a username and password until the correct details are entered. For **every** attempt, failed or successful, it prints a log entry containing:

- Event ID (random 4-digit number)
- Username
- IP address of the computer
- Event (Failed login / Successful login)
- Timestamp

## Python concepts used

- Python libraries: `random`, `datetime`, `socket`
- `while` loop that repeats until the correct login is entered
- Functions (`get_ip_address()`, `print_event()`)
- `try` / `except` so the program still works if the computer is offline
- String methods (`.strip()`) and f-strings

## Test credentials

- Username: `admin`
- Password: `admin123`

## How to run

```bash
python security_event_logger.py
```

Or open the file in VS Code and click **Run → Start Debugging → Python Debugger**.

## Example output

```
SECURITY EVENT LOG
==================
Enter username: admin
Enter password: wrong

Event ID: 8009
Username: admin
IP Address: 192.168.1.25
Event: Failed login
Timestamp: 2026-11-10 12:16:07

Enter username: admin
Enter password: admin123

Event ID: 7849
Username: admin
IP Address: 192.168.1.25
Event: Successful login
Timestamp: 2026-11-10 12:16:15

Login complete. All attempts have been logged above.
```

## Screenshots

<!-- Add your output screenshots here -->

## Licence

MIT License. See `LICENSE`.
