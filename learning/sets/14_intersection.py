#Problem Statement: Write a Python program to check whether two sets share any common elements using the .isdisjoint() method.
#Purpose: Knowing whether two sets are completely separate is valuable in scheduling, access control, and data deduplication tasks, where overlap between groups signals a conflict or an error that needs to be handled
set_a ={1,2,3}
set_b = {4,5,6}
print(f"Are the sets disjoint? {set_a.isdisjoint(set_b)}")
