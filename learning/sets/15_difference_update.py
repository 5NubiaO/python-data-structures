#Problem Statement: Write a Python program to modify a set by removing all elements that are also found in another set using the difference_update() method.
#Purpose: This exercise helps you practice in-place set modification. Understanding difference_update() is useful when you need to strip out unwanted or overlapping entries from a collection without creating a new object.
a = {1,2,3,4,5}
b = {3,4,5,6,7}
a.difference_update(b)
print(a)