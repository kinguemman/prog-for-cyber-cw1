# Task 5: Reusable Cyber Security Utilities using User-Defined Modules

**Name:** Emmanuel Kalu  
**Banner ID:** B01808189  
**Campus:** Lanarkshire Campus  
**Module:** COMP08101 Programming for Cyber Security

## What the program does

Instead of placing all the code in one file, the security functions are organised into a separate, reusable module.

### `security_tools.py` (the module)

| Function | Purpose |
|---|---|
| `validate_password(password)` | Returns `True` if the password is at least 10 characters and contains at least one letter, one digit and one symbol. |
| `validate_ip(ip)` | Returns `True` if the IP address has three dots, four numbers, and every number is 0–255. |
| `generate_password()` | Returns a random strong password between 10 and 16 characters (length chosen randomly each time) containing uppercase, lowercase, digits and symbols. |

### `main.py` (the program)

Imports `security_tools`, asks the user for a password and an IP address, and displays whether each is valid. If the password is weak, it suggests a randomly generated strong password.

## Python concepts used

- User-defined modules and `import`
- Functions with parameters and return values
- `random.randint()` and `random.choice()`
- Lists: `append()`, indexing and `del`
- String methods: `.isalpha()`, `.isdigit()`, `.isalnum()`, `.split()`, `.count()`, `.strip()`
- `for` and `while` loops

## How to run

Keep both files in the same folder, then run:

```bash
python main.py
```

## Example output

Weak password and invalid IP:

```
Enter a password: short
Enter an IP address: 1.2.3

Results
-----------------------
Password: WEAK (needs 10+ characters with a letter, digit and symbol)
Suggested strong password: oio8m%B!Fm@49!
IP Address: INVALID
```

Strong password and valid IP:

```
Enter a password: Summer2026!x
Enter an IP address: 8.8.8.8

Results
-----------------------
Password: STRONG
IP Address: VALID
```

## Screenshots

### Valid and invalid input
![Valid and invalid runs](Task%205.png)

## Licence

MIT License. See `LICENSE`.
