#Words longer than 6 characters from a list of words
words = ['pineaple', 'strawberry', 'banana', 'mango','watermelon']
longer = [i for i in words if len(i)>6]
print(longer)