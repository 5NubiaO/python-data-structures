#Write a Python program to reverse the order of elements in a tuple.
#Purpose: This exercise shows how to reverse a tuple even though tuples have no built-in .reverse() method (unlike lists). You will practice using slice notation with a step value, which is a widely used Python idiom for reversing any sequence.
items = (1,2,3,4,5)
print(items[::-1])