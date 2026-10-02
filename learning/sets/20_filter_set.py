#Problem Statement: Write a Python program to create a new set containing only the elements from an existing set that satisfy a condition – specifically, elements divisible by 3.

#Purpose: This exercise introduces set comprehensions as a clean and readable way to filter data. The pattern mirrors list comprehensions but produces a set, which automatically eliminates any duplicate results.

numbers = {1,2,3,6,7,9,12,14,15}
divisible_3 = {x for x in numbers if x%3==0}
print(divisible_3)