#Write a Python program to check whether a set is empty using conditional logic, and print an appropriate message based on the result.
#Purpose: This exercise builds awareness of how Python evaluates collections as truthy or falsy values. Knowing how to check for emptiness reliably prevents bugs in data pipelines, loops, and validation routines where an empty set should trigger a different code path.
data = set()
if not data:
    print("The set is empty")
else:
    print("The set is not empty")    
       