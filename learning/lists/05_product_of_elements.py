#multiply every number in a list together to find the total product
factors = [2,3,5,7]
x =1
for i in factors:
  product = x*i
  x = product
print(f"Product: {product}")

'''
factors = [2, 3, 5, 7]
product = 1

for x in factors:
    product *= x

print(f"Product: {product}")
'''