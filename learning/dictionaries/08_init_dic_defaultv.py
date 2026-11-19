#Problem Statement: Write a Python program to create a dictionary from a list of keys, assigning the same default value to every key.
#Purpose: Initializing dictionaries with default values is a common setup step in counting, scoring, and configuration tasks, it ensures every expected key exists before any data is processed.
keys = ["math", "science", "english", "history"]
default = 0
init = dict.fromkeys(keys,default)
print(init)

#could also use dictionary comprehension
print(f"Dictionary comprehension:",{k: default for k in keys})