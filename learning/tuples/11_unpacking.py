#write a Python program to unpack a four element tuple into four distinct variables in a single assignment
#Purpose: This exercise introduces tuple unpacking, one of Python’s most elegant features. Unpacking makes code more readable by giving meaningful names to positional data, and it is widely used when working with function return values, database rows, and coordinate pairs.
person = ("Alice", 30, "Engineer", "Pune")
name,age,job,city = person
print(f"Name: {name}\n Age: {age}\n Job: {job}\n City: {city}")