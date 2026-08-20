#Write a Python program to convert a tuple of characters into a single joined string.
#Purpose: This exercise shows how to bridge the gap between tuples and strings. The str.join() method is a core Python tool for assembling strings from iterable sequences, and practising it on a tuple reinforces that join() works on any iterable, not just lists.
chars = ('a','b','c')
print("".join(chars))#use method str.join()
#the separator string goes before .join(). and the tuple is passed as the argument inside it