#Problem Statement: Write a Python program to create a frozenset, demonstrate that set operations work on it, and confirm that any attempt to modify it raises a TypeError.
#Purpose: This exercise introduces immutability in the context of sets. A frozenset can be used as a dictionary key or stored inside another set, making it valuable when you need a hashable, read-only collection, such as representing a fixed combination of permissions or configuration flags.

fs = frozenset([1,2,3,4,5])
print(f"frozenset: {fs}")
print(f"Intersection with {3,4,5,6}:{fs.intersection({3,4,5,6})}")
try:
    print(fs.add(4))
except AttributeError as e:
    print(f"Error:, {e}")