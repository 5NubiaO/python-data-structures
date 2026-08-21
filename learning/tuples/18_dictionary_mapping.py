#Write a Python program to zip two tuples together – one holding keys and the other holding values – to create a dictionary.
#Purpose: This exercise demonstrates a common pattern for building dictionaries from paired data sources. Combining zip() with dict() is widely used when parsing CSV headers, mapping configuration keys to values, and constructing lookup tables from separate lists.
keys =("name", "age", "city")
values = ("Alice", 30, "Pune")

result = dict(zip(keys,values)) #zip returns a lazy iterator so we have to cast it as tuple() or desired format
print(result)