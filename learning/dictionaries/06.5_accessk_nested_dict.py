#Problem Statement: Write a Python program to access the value associated with the key 'history' from a dictionary nested within a larger data structure.

#Purpose: Understand multi-level dictionary traversal using a realistic data structure that resembles student records, course databases, or API payloads situations where a specific field must be extracted from deeply nested data.

student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}

print(f"Math grade:",student.get('grades',{}).get('math'))
print(f"Science grade:",student['grades']['science'])

