#Given a list of intergers, iterate throught the items and count how many are even and how many are odd
numbers = [10,21,4,45,66,93,11]
even =0
odd = 0
for i in numbers:
    if i % 2 ==0:
        even +=1
    if i % 2 ==1:
        odd+=1

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
