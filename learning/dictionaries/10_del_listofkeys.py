#Problem Statement: Write a Python program to remove multiple specific keys from a dictionary in one operation.

#Purpose: Bulk key removal is useful when filtering out sensitive fields before logging, stripping unwanted metadata from API responses, or trimming a record down to only the fields your application needs.

product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}

remove = ["stock", "warehouse"]

for k in remove:
   product.pop(k, None)      
print(product)

#build a new dictionary that excludes the one to remove
print(f"Dictionary Comp:",{k: v for k, v in product.items() if k not in remove})
