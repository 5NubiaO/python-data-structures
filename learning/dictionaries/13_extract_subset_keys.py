#Problem Statement: Write a Python program to create a new dictionary containing only a specified subset of keys from an existing dictionary.

#Purpose: Extracting a key subset is essential when preparing data for display, serialisation, or an API call, you often need to expose only certain fields from a larger record while keeping the original intact.

user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}

extract =['id','username','email']


print({k: user[k] for k in extract})