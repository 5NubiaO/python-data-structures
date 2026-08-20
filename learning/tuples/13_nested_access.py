#Write a Python program to access a specific element that is stored inside a tuple which is itself nested inside another tuple.
#Purpose: This exercise builds your understanding of nested data structures. Tuples can contain other tuples as elements, and chaining index operators is the standard way to drill down into them. This pattern appears frequently when working with coordinate grids, database records, and configuration structures.
matrix = ((1,2,3),(4,5,6),(7,8,9))
print(matrix[1][2])