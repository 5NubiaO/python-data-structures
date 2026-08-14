#In a list of strings, identify wich string hast the most characters
words = ["PHP","Exercises", "Backend", "Python"]
lenght = []
for i in words:
    leng_letter = (len(i))
    lenght.append(leng_letter)
biggest = max(lenght)
position = lenght.index(biggest)
word = words[position]    
print(f"Longest: {word}")

'''there's an easier approach too

words = ["PHP","Exercises", "Backend", "Python"]
longest = max(words, key = len)
print(f"Longest: {longest}")

'''