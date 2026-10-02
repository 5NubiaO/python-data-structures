#Problem Statement: Write a Python program to remove a batch of specific items from a set all at once using the difference_update() method.
#Purpose: This exercise demonstrates a practical use of difference_update() as a bulk-removal tool. Rather than looping and calling remove() repeatedly, you can pass a collection of items to discard in a single operation.
items = {10,20,30,40,50,60}
to_remove = {20,40,60}
items.difference_update(to_remove)
print(items)