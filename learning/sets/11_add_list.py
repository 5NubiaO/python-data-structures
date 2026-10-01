#Write a Python program to add multiple elements from a list into an existing set using the .update() method.
#This exercise demonstrates how to efficiently bulk-add items to a set from another iterable. The .update() method is preferable to calling .add() in a loop when you have a collection of items ready to merge, and it automatically handles duplicates.

fruits = {"apple","banana"}
new_fruits = ["cherry", "mango","apple"]
fruits.update(new_fruits)
