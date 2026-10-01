#write a python program to find all elements that are in either Set A or Set B, but not in both
#The symmetric difference is useful when you need to identify what is exclusive to each group, such as finding products carried by one store but not the other, or detecting changes between two versions of a dataset.
set_a = {1,2,3,4}
set_b = {3,4,5,2}
print(f"Symmetric difference: {set_a ^ set_b}")
