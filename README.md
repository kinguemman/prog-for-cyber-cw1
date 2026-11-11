# Task 4: Security Incident Manager using Dictionaries

**Name:** Emmanuel Kalu  
**Banner ID:** B01808189  
**Campus:** [Lankshire Campus]  
**Module:** COMP08101 Programming for Cyber Security

## What the program does

Stores information about a security incident in a Python dictionary and updates it. The program:

1. Creates a dictionary with a username, IP address, event type and risk level
2. Displays the username and IP address
3. Adds a new field called `status`
4. Updates the risk level from Medium to High
5. Removes the `event_type` field
6. Displays all remaining keys and values
7. Displays the total number of key-value pairs

## Why a dictionary?

A dictionary stores data as **key-value pairs**, so each value is found by a meaningful name (like `"ip_address"`) instead of a number position. This suits incident records, where each piece of information has a clear label.

## Python concepts used

- Creating a dictionary with `{}`
- Accessing values by key: `incident["username"]`
- Adding and updating with `incident["key"] = value`
- Removing with `del`
- Looping with `.items()`
- Counting with `len()`

## How to run

```bash
python security_incident_manager.py
```

## Example output

```
Username: alice
IP Address: 192.168.1.25

Remaining incident details:
username: alice
ip_address: 192.168.1.25
risk_level: High
status: Under investigation

Total number of key-value pairs: 4
```

## Screenshots

<!-- Add your output screenshots here -->

## Licence

MIT License. See `LICENSE`.
