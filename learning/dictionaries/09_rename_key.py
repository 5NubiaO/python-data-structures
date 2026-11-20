#Problem Statement: Write a Python program to rename an existing key in a dictionary while preserving its associated value and the rest of the dictionary unchanged.

#Purpose: Renaming keys comes up frequently when normalizing data from external sources — such as API responses or CSV headers, to match the field names expected by your application.

employee = {"fname": "John", "age": 30, "dept": "Engineering"}

employee['fisrt name'] = employee.pop("fname")
print(employee) #In Python 3.7+, dictionaries preserve insertion order. The renamed key appears at the end of the dictionary