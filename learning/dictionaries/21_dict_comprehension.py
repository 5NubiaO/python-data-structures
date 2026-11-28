#Problem Statement: Write a Python program to generate a dictionary of the squares of numbers from 1 to 10 using a dictionary comprehension in a single line.

#Purpose: Dictionary comprehensions offer a concise, readable alternative to building dictionaries with loops. Mastering this syntax is valuable for data transformation tasks where keys and values are derived from a common iterable.
print({k:k**2 for k in range(1,11)})