#Problem Statement: Write a Python program to convert a set of words into a single string where each element is separated by a specified delimiter.

#Purpose: This exercise practises combining set data back into a human-readable string. Joining a set is commonly needed when generating comma-separated values, building display labels from tags, or serialising a set of identifiers into a single field.

tags ={"python", "set", "programming", "tutorial"}
print(" | ".join(tags))