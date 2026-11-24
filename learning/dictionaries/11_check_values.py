#Problem Statement: Write a Python program to verify whether a specific value is present anywhere in a dictionary.

#Purpose: Checking for value existence is common in validation workflows — for example, confirming that a username, status code, or category is already recorded before inserting a duplicate entry.

roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}
print('editor exist as a value', 'editor' in roles.values() )
print('manager exist as a value', 'manager' in roles.values() )