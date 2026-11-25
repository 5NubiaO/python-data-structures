#Problem Statement: Write a Python program that uses zip() to combine a list of keys and a list of values into a single dictionary.

#Purpose: Mapping two parallel lists into a dictionary with zip() is a pattern that appears constantly when processing tabular data, for example, pairing a header row with a data row read from a CSV file to produce a named-field record.

attributes = ["brand", "model", "year", "color"]
details = ["Honda", "Civic", 2023, "silver"]

merged = dict(zip(attributes,details))
print(merged)