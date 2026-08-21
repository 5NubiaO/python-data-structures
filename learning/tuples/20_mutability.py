#Create a tuple that contains a list as one of its elements. Modify the list in place and observe that the tuple’s identity stays the same while its contents appear to change.
#Purpose: This exercise uncovers one of Python’s most instructive subtleties: a tuple is immutable in the sense that its references cannot be reassigned, but if a reference points to a mutable object such as a list, that object itself can still be changed. Understanding this distinction is essential for writing predictable, bug-free code.
t = (1,2,[3,4,5])
print(f"Before: {t}")
print(f"Tuple id before: {id(t)}")  #returns the unique memory adress of the tuple object
t[2].append(99)
print(f"After: {t}")
print(f"Tuple id before: {id(t)}")
print(f"Same Object? {id(t) == id(t)}") #this is only to verify tuple immutability: the tuple’s references cannot be rebound. 
