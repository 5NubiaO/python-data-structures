#Problem Statement: Write a Python program to count how many times each character appears in a given string, storing the results in a dictionary.

#Purpose: Character frequency counting is a foundational technique used in text analysis, data compression algorithms, cryptography, and natural language processing, making it an essential pattern to master early.

text = 'hello world'
count = {}
for char in text:
    count[char] = count.get(char,0) + 1 

print(count)    






