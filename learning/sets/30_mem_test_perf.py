#Problem Statement: Write a Python program to compare the time taken to check whether an item exists in a large list versus a large set, and observe the performance difference.

#Purpose: This exercise makes the performance advantage of sets concrete and measurable. Membership testing is one of the most frequent operations in programming, and switching from a list to a set can reduce lookup time from O(n) to O(1) on average – a critical optimisation for large datasets.
import time

listt = list(range(1000000))
sett = set(range(1000000))

find = 999999

#start the time for the list
start = time.time()
result = find in listt
listt = time.time() - start

#start the time for the set
start = time.time()
result = find in sett
sett = time.time() - start

print(f"List lookup time: {listt: .10f} seconds")
print(f"Set lookup time: {sett: .10f} seconds")