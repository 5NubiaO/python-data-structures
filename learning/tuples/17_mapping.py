#Write a Python program to apply a square function to every item in a tuple using map(), and also demonstrate the equivalent generator expression approach.
#Purpose: This exercise introduces the functional programming concept of mapping a transformation over a sequence. The map() function and its comprehension equivalent appear regularly in data transformation, preprocessing pipelines, and mathematical computations.

#list comprehension
numbers = (1,2,3,4,5,6)
square = tuple(i**2 for i in numbers)
print(f"List Comprehension: {square}")

#using map 
#map() requieres: map(function, iterable, ...)
#function = the transformation logic to aply to each element
#iterable = one or more sequences (lits, tuples, strings) to process

#lambda function
square_map =tuple(map(lambda x:x**2, numbers)) #use lambda function wich aply the logic for squares
print(f"Using map(lambda): {square_map}")

#making a function
def square(i):
    return i**2
squared_map = tuple(map(square, numbers))
print("Using map():", squared_map)