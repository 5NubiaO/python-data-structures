#Problem Statement: Write a Python program to modify a set so that it keeps only elements that are in either set but not in both, using the symmetric_difference_update() method.
#Purpose: This exercise teaches you to isolate non-overlapping elements between two sets in place. It is useful in scenarios like finding items that exist in one dataset but not the other, such as detecting mismatches between two records.
a= {1,2,3,4,5}
b = {3,4,5,6,7}
a.symmetric_difference_update(b)
print(a)