#Write a pyhton program to find all elements that are common to both sets
#The intersection operation is widely used in filtering, data comparison, and finding overlaps between datasets, such as identifying shared costumers, tags, or feautures across two groups
set_a ={1,2,3,4}
set_b = {3,4,5,6}
print(f"Intersection: {set_a.intersection(set_b)}")
#same as using its symbol
print(f"Intersection: {set_a&set_b}")