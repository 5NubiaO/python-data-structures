#given a list of numbers, create a new list where each number is replaced by its square(n^2) using a single line of code
numbers = [1,2,3,4,5]
squares = [x**2 for x in numbers]
print(squares)