#Problem Statement: Write a Python program to remove a specific key from a dictionary, retrieve all key-value pairs, and check whether a given key exists.

#Purpose: To builds familiarity with essential dictionary methods pop(), items(), and the in operator, which are routinely used when processing and validating structured data

car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
car.pop("color")

print(car)
print(car.items())
print("'brand' exists: ","brand" in car)
print("'color' exists: ","color" in car)
