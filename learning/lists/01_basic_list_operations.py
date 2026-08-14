#Write a Script to perform the following threre operations:
#1. access the third element of a list 
#2. list lemght: print the total number of items
#3. check if the list is empty

lista = [10,20,30,40,50]
print('Third element: ',lista[2])
print('Lenght of list: ',len(lista))
'''empty = False
if len(lista) == 0: 
    empty = True
print('Is the list empty? ', empty)    '''

empty = len(lista)==0
print('Is the list empty?', empty)