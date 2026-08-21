#Write a Python program to filter a tuple and keep only the elements that satisfy a given condition, using both filter() and a list comprehension approach.
#Purpose: This exercise demonstrates two idiomatic ways to select a subset of items from a sequence based on a condition. Filtering is a foundational operation in data processing, validation, and functional-style programming.

numbers = (3, 14, 7, 22, 9, 41, 18, 5)
filtered = tuple(filter(lambda x: x>10, numbers))
print(filtered)

#this can also be done with list comprehension
filtered_comp= tuple(x for x in numbers if x>10)
print(f"Using list comprehension: {filtered_comp}")