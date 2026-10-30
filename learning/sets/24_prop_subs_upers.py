#Problem Statement: Write a Python program to check whether one set is a proper subset and another is a proper superset using the < and > operators.

#Purpose: This exercise clarifies the difference between regular and proper subset/superset relationships. Understanding strict comparisons is useful when validating permissions, checking feature flag hierarchies, or verifying that one group of items is strictly contained within another.

a = {1,2,3}
b = {1,2,3,4,5}

print(f"'a' is a proper subset of 'b': {a<b}")
print(f"'b' is a proper superset of 'a': {b>a}")
print(f"'a' is a proper subset of 'a': {a<a}")