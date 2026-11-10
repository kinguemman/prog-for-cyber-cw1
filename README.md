# prog-for-cyber-cw1

Coursework 1 portfolio for **COMP08101 Programming for Cyber Security** at the University of the West of Scotland.

## Student details

| | |
|---|---|
| **Name** | Emmanuel Kalu |
| **Banner ID** | B01808189 |
| **Campus**    | Lanarkshire Campus |
| **Module** | COMP08101 Programming for Cyber Security |

## About this repository

The `main` branch is the overview of the portfolio. Each programming exercise lives on its own branch, with its Python code, its own README and a licence.

All programs are written in Python 3 and were developed and tested in VS Code on Windows.

## Exercises and branches

| Task | Exercise | Branch | Description |
|---|---|---|---|
| 1 | Security Tool | `security-tool` | Login-protected menu with a Security Event Counter, Brute-Force Simulation and Login Authentication (account freezes after 3 failed logins). |
| 2 | Security Event Logger | `security-event-logger` | Asks for login details until correct and prints a log entry (event ID, username, IP address, event, timestamp) for every attempt. |
| 3 | IP Address Validator | `ip-address-validator` | `validate_ip()` function that checks an IPv4 address has three dots, four numbers, and values from 0 to 255. |
| 4 | Security Incident Manager | `security-incident-manager` | Stores a security incident in a dictionary and shows adding, updating, removing and displaying fields. |
| 5 | Cyber Security Utilities | `cyber-security-utilities` | User-defined module `security_tools.py` (password validator, IP validator, strong password generator) imported by `main.py`. |

## How to view an exercise

On GitHub, use the branch dropdown to switch branch. Or locally:

```bash
git clone https://github.com/<your-username>/prog-for-cyber-cw1.git
cd prog-for-cyber-cw1
git switch security-tool
```

Each branch's README explains how to run that program.

## Licence

This project is released under the MIT License. See `LICENSE`.
