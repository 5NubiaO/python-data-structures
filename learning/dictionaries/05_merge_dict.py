#Problem Statement: Write a Python program to combine two dictionaries into a single dictionary. If both dictionaries share a key, the value from the second dictionary should take precedence.

#Purpose: Merging dictionaries is a frequent task in configuration management, data aggregation, and API response handling, making it essential to know the available approaches and their precedence rules.

dict1 = {'a':1,'b':2}
dict2 = {'b':3,'c':4}

merged = dict1 | dict2       #The merge operator introduced in Python 3.9 produces a new merged dictionary with the same precedence rules as unpacking, offering a cleaner, more readable syntax.
mergedun = {**dict1,**dict2} #Unpacks both dictionaries into a new dictionary literal. Keys appearing in both are resolved left to right, so dict2 values take precedence. The originals remain
dict1.update(dict2)          #Merges all key-value pairs from dict2 into dict1 in place. Where keys overlap, dict2‘s value wins. This method mutates dict1 directly.

print(f"Merge operator: {merged}")
print(f"Unpaking: {mergedun}")
print(f"Updating: {dict1}")