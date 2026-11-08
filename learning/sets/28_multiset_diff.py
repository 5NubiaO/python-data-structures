'''Problem Statement: Write a Python program to find all elements that are in Set A but not present in either Set B or Set C.
Purpose: This exercise extends the two-set difference operation to multiple sets. 
It is practical in scenarios such as finding users who have not yet completed any of several onboarding steps, or items in a master list that have not been processed by any of several workers.'''

A = {1, 2, 3, 4, 5, 6, 7, 8}
B = {2, 4, 6}
C = {5, 7, 9}

A = A.difference(B,C)
print(A)