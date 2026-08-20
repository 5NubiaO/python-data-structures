#Write a Python program to use the .count() method to find how many times a specific element appears in a tuple.
#Purpose: This exercise introduces one of the two built-in methods that tuples provide. Knowing how to count occurrences without writing a manual loop is a practical skill used in frequency analysis, data validation, and duplicate detection.
votes = ("yes", "no","yes","yes", "no","yes")
print(f"yes apears {votes.count("yes")} times")
print(f"No appears {votes.count("no")} times")