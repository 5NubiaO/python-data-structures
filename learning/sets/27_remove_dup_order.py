#Problem Statement: Write a Python program to remove duplicate values from a list while preserving the original order of first appearances.
#Purpose: Converting a list directly to a set removes duplicates but loses order. 
#This exercise teaches a practical pattern that combines the deduplication power of a set with the ordering properties of a list, commonly needed in data cleaning, deduplication pipelines, and maintaining insertion-ordered unique sequences.
items = [3,1,4,1,5,9,2,6,5,3,5]
items = set(items)
new = items.difference()
print(new)