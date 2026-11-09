#Problem Statement: Write a Python program to demonstrate that a set can store tuples as elements but cannot store lists, and explain why this difference exists.
#Purpose: This exercise builds a concrete understanding of hashability, the property that determines which types can live inside a set or be used as dictionary keys. Knowing why lists are rejected and tuples are accepted prevents common bugs when working with collections of compound values.
set_tuples = {(1,2), (3,4), (5,6)}
print(type(set_tuples))

try: set_list ={[1,2],[3,4],[5,6]}
except TypeError as e: 
    print("Error: ",e)

'''
Tuples are hashable because they are immutable
Lists aren't hashable because they can be modified after creation
-Wich would invalitade any hash-based lookup'''    