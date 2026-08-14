#Delete every instance of a specific value from a list
lista = [5,20,15,20,25,50,20]
target = 20
new = []
for i in lista:
    if i is not target:
        new.append(i)
print(f"Cleaned list: {new}")

'''wich can be written in list comprehesion as:

lista = [5,20,15,20,25,50,20]
target = 20
new = [i for i in lista if i is not target]
print(f"Cleaned list: {new}")
'''