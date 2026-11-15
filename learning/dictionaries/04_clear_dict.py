#Problem Statement: Write a Python program to remove all items from a dictionary while keeping the dictionary object itself intact.

#Purpose: Understand the difference between clearing a dictionary and deleting it entirely, an important distinction when the same dictionary reference is shared across multiple parts of a program.

inventory = {"apples": 10, "bananas":5, "oranges":8}
inventory.clear()
print(inventory)