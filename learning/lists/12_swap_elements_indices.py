#Write a Script to swap the positions of two elements in a list based on their indeces
original = [23,65,19,90]
#syntaxis list[a],list[b] = list[b], list[a]
original[0], original[2] = original[2], original[0]
print(f"Swapped: {original}")