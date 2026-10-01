#write a python program to create a set, add a new element to it, remove an element using remove(), and dicard an element using discard()
#This exercise introduces you to the core mutation methods of Python sets. Understanding the difference between remove() and discard() is essential because one raises an error on missing elements while the other does not, making each suited to different real-world scenarios.

fruits = {"apple", "banana","cherry"}
print(fruits)
fruits.add("mango")
print(f"After add: {fruits}")
fruits.remove('banana')
fruits.discard("banana")
print(f"After remove: {fruits}")
print(f"After discard: {fruits}")
