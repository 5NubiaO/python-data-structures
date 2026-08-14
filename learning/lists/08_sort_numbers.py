#sort a list of numbers in ascending order (lowest to highest)
unsorted = [56,12,89,3,22]
unsorted.sort()
print(f"Sorted List: {unsorted}")

unsorted[::-1]
print(f"Sorted (slicing): {unsorted}")

unsorted.reverse()
print(f"Sorted Descending (reversed): {unsorted}")

