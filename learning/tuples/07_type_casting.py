#Write a Python program to convert a list into a tuple using the tuple() constructor.
#Purpose: This exercise demonstrates how to convert between mutable and immutable sequence types. Converting a list to a tuple is a common pattern when you want to protect data from accidental modification, use it as a dictionary key, or pass it to a function that expects an immutable sequence.
my_list = [10,20,30,40,50]
my_tuple= tuple(my_list)
print(my_tuple, type(my_tuple))
