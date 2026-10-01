#Write a pyhton program to calculate the total sum of all elementss in a set manually using a loop, without using the built-in function sum()
#Purpose: This exercise reinforces the accumulator patter using a loop, applied to a set instead of a list. It illustrates that iteration works uniformly
#It Streghtens your grasp of how aggregation functions work interally
numbers = {10,20,30,40,50}
total = 0
for i in numbers:
    total = total+i
print(f"Sum: {total}")
