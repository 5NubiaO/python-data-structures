#Write a Python program to add elements from a list, a tuple, and another set into an existing set in a single .update() call.
#This exercise highlights the flexibility of .update() in accepting multiple iterables at once. It is a practical pattern when consolidating data from several heterogeneous sources into one unified set in a single step.

base = {1,2}
from_list = [3,4]
from_tuple= (5,6)
from_set= {7,8}
updated_set = base.update(set(from_list),set(from_tuple),set(from_set))
print(f"Updated set: {base}")
