#Write a Python program to determine how many elements are in a set without using the built-in len() function.
#This exercise strengthens your understanding of iteration and manual counting logic. While len() is convenient, building a counter loop reinforces how Python traverses collections internally and prepares you for situations where custom counting logic is required.

animals ={"cat", "dog","bird","fish"}
lenght = 0
for i in animals:
    lenght +=1
print(f"Lenght of set: {lenght}")

#we can use the built in function len() as wel
