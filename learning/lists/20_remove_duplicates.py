'''
Remove all duplicate values from a list while keeping only one instance of each element.
Exercise Purpose: This exercise introduces Set Theory. In programming, you often need to ensure uniqueness (e.g., a list of unique email subscribers). While there are many ways to do this, using Python’s set or dict structures is the fastest way to handle the logic.
'''
numbers= [10, 20, 10, 30, 40, 40, 20, 50]
filtered = set(numbers)
print(sorted(filtered))

#Another method:
'''
duplicates = [10, 20, 10, 30, 40, 40, 20, 50]

# Method to remove duplicates while preserving order
unique_list = list(dict.fromkeys(duplicates))

print(f"Unique List: {unique_list}")
'''
# Dictionary keys must be unique. When Python creates this dictionary, it keeps the first time it sees “10” and ignores all later “10”s.
# Unlike a standard set(), dict.fromkeys() preserves the order in which items first appeared (as of Python 3.7+).