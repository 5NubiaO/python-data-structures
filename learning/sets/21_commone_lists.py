#Problem Statement: Write a Python program to find the common elements between two lists by converting them to sets and using the intersection operation.

#Purpose: This exercise shows how sets can solve a practical problem more elegantly than nested loops. Converting lists to sets before intersecting them removes duplicates and enables fast lookup, making the approach both concise and efficient.
list1 = [1,2,3,4,5,3,2]
list2 = [3,4,5,6,7,4,5]
print(set(list1).intersection(set(list2)))
