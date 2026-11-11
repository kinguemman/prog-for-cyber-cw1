# ==========================================================
# Task 4: Security Incident Manager using Dictionaries
# Name: Emmanuel Kalu
# Banner ID: B01808189
# Module: COMP08101 Programming for Cyber Security
# ==========================================================
# Stores a security incident as a dictionary and shows how to
# read, add, update and remove its information.
# ==========================================================

# 1. Create a dictionary to store the incident as key-value pairs
incident = {
    "username": "alice",
    "ip_address": "192.168.1.25",
    "event_type": "failed_login",
    "risk_level": "Medium"
}

print("Original incident:", incident)

# 2. Display the username and IP address by using their keys
print("\nUsername:", incident["username"])
print("IP Address:", incident["ip_address"])

# 3. Add a new field called status (a new key creates a new pair)
incident["status"] = "Under investigation"
print("\nAfter adding status:", incident)

# 4. Update the risk level (an existing key is overwritten)
incident["risk_level"] = "High"
print("\nAfter updating risk level:", incident)

# 5. Remove one field from the dictionary using del
del incident["event_type"]
print("\nAfter removing event_type:", incident)

# 6. Display all remaining keys and values
# items() gives each key together with its value
print("\nRemaining incident details:")
for key, value in incident.items():
    print(f"{key}: {value}")

# 7. Display the total number of key-value pairs
print("\nTotal number of key-value pairs:", len(incident))
