#Problem Statement: Write a Python program to retrieve a specific value from a dictionary that is nested inside another dictionary.

#Purpose: Nested dictionaries are widely used to represent structured data such as JSON responses, configuration files, and database records. This exercise trains you to navigate multiple levels of key access.
person = {'name': 'carol', 'address': {'city':'Paris', 'zip':'75001'}}

print(person['address']['city']) #chain bracet dict['outer+key']['inner_key']

print(person.get('address',{}).get('city')) #dict.get("outer_key", {}).get("inner_key") for safer access that avoids a KeyError if any level is missing.