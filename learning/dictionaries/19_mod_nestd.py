#Problem Statement: Write a Python program to change a specific value inside a dictionary that is nested within another dictionary.

#Purpose: Modifying nested dictionary values is a routine task when updating records in hierarchical data structures such as configuration objects, user profiles, or JSON documents loaded from an API.

company = {"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}}
#change city to "Munich"

company["location"]["city"]="Munich"
print(company)