#Problem Statement: Write a Python program to check whether one set is a subset of another and whether one set is a superset of another using .issubset() and .issuperset().
#Purpose: Subset and Superset checks are essentian in access control systems, tag-based filtering, and data validation scenarios where you need to confirm that one group of items is entirely contained within another
set_a= {1,2,3}
set_b = {1,2,3,4,5}

print(f"Is set_a a subset of set_b? {set_a.issubset(set_b)}")
print(f"Is set_b a superset of set_a? {set_b.issuperset(set_a)}")