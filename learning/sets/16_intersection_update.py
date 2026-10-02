#Problem Statement: Write a python program to modify a set so that it keeps only the elements that are also found in another set using the intersection_update() method
#Purpose: This exercise reinforces in-place filtering of a set to its shared elements. It is commonly used when recoinciling two collections and retaining only the data that appears in both, such as matching user IDs or common tags
a = {1,2,3,4,5}
b = {3,4,5,6,7}
a.intersection_update(b)
print(a)