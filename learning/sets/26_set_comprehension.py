#Problem Statement: Write a Python program to generate a set of squares of all even numbers from 1 to 20 using a set comprehension in a single line.
#Purpose: This exercise demonstrates set comprehensions as a concise and readable alternative to building sets with loops. 
#They follow the same syntax as list comprehensions but produce a set, ensuring all resulting values are automatically deduplicated.
squares = {(i,i**2) for i in range (1,21) if i%2==0}
print(squares)

