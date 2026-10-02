#Problem Statement: Write a Python program to remove and return an arbitrary element from a set using pop(), and handle the KeyError that occurs when the set is empty.
#Purpose: This exercise familiarises you with the pop() method and its unpredictable nature on sets. It also practices defensive programming using try/except blocks to handle runtime errors gracefully.
s = {100,200,300}
empty = set()

print(s.pop())
print(s)
try:
    print(empty.pop())
except: 
    print("Error: I cannot pop an empty set")    