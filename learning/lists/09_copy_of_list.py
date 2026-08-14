#Create a copy of an existing list so that modifying the copy does not change the original
original = ["Apple","Banana","Cherry"]
copy = original.copy()
copy[2] = "pineaple"

print(f"Original: {original}")
print(f"Copy: {copy}")
