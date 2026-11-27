#Problem Statement: Write a Python program that separates a list of integers into two groups, even and odd, storing each group in a dictionary with lists as values.
numbers = [1,2,3,4,5,6,7,8,9,10]
dict1 = {}
for i in numbers:
 if i%2 ==0:
  dict1.setdefault("even",[])
  dict1['even'].append(i)
 else:
  dict1.setdefault("odd",[])
  dict1['odd'].append(i) 

print(dict1)