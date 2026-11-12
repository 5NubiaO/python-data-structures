#Problem Statement: Write a Python program to add a new key-value pair to a dictionary, modify an existing value, and access a specific key.

#Purpose: Learn and practice the most fundamental dictionary operations such as insertion, update, and lookup, which form the backbone of working with key-value data in Python.

student = {"name": "Alice", "age": 20, "grade": "B"}
student["city"] = "New York"
student["age"] = 21

print(student)
print(f"Name: {student["name"]}")