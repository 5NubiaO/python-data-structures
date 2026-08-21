#Write a Python program to find all elements that are common to two different tuples.
#Purpose: This exercise introduces set intersection as a tool for comparing collections. Finding shared elements between two sequences is a core operation in data analysis, deduplication, access control (shared permissions), and any scenario where you need to identify overlap between datasets.
t1 = (1,2,3,4,5,6)
t2 = (4,5,6,7,8,9)
common =tuple(sorted(set(t1).intersection(set(t2))))
#Converts both tuples to sets and applies the intersection operator, which returns a new set containing only the values present in both. This is an O(min(n, m)) operation, making it efficient for large inputs.
print(f"Common elements set(): {common}")

#list comprehension
common_l = tuple(i for i in t1 if i in t2)
print(f"Common elements LC: {common_l}")