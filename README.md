# Task 3: IP Address Validator (using Function)

**Name:** Emmanuel Kalu  
**Banner ID:** B01808189  
**Campus:** Lanarkshire Campus  
**Module:** COMP08101 Programming for Cyber Security

## What the program does

IP addresses appear constantly in security logs. Before analysing one, a program can check that it has the expected structure.

The `validate_ip()` function performs a basic IPv4 format check. It:

1. Accepts an IP address as a parameter
2. Removes unnecessary spaces with `.strip()`
3. Checks the address contains dots
4. Checks there are exactly three dots
5. Checks there are exactly four numbers
6. Checks every number is between 0 and 255
7. Returns `True` if all checks pass, otherwise `False`

This is a basic format check, not a complete IPv4 validation system.

## Python concepts used

- User-defined function with a parameter and a return value
- String methods: `.strip()`, `.count()`, `.split()`, `.isdigit()`
- `in` operator, `len()`, `int()` conversion
- `for` loop over a list
- `if` statements with early `return`

## How to run

```bash
python ip_address_validator.py
```

## Example output

| Input | Output | Reason |
|---|---|---|
| `192.168.1.10` | Valid IP address | Passes every check |
| `192.168.1.300` | Invalid IP address | 300 is above 255 |
| `192.168.1` | Invalid IP address | Only two dots / three numbers |
| `192.168.one.10` | Invalid IP address | "one" is not a number |

```
Enter an IP address: 192.168.1.10
Valid IP address
```

## Screenshots

![Valid and invalid runs](Task%203%20%28Valid%2CInvalid%29.png)

## Licence

MIT License. See `LICENSE`.
