#Problem Statement: Write a Python program to create a dictionary by mapping two equal-length lists, one containing keys and the other containing values.

#Purpose: Learn how to construct a dictionary dynamically from existing data, a common pattern when importing tabular data, pairing labels with values, or building lookup tables.

keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]
v = zip(keys,values)
print(dict(v))

#This can also get done with dictionary comprehension
dicti = {k: v for k, v in zip(keys,values)}
print(f"Using list comprehension: ",dicti)