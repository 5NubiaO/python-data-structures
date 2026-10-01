#Write a Python program to combine two sets into one, containing all unique elements from both sets.
#This exercise introduces the union operation, a fundamental concept in set theory and database-style data merging. It is commonly used when aggregating data from multiple sources while automatically eliminating duplicates.
set_a = {1,2,3,4}
set_b = {3,4,5,6,}
print(f"Union of sets: {set_a|set_b}")
