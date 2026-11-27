#Create a dictionary grouping words according to their length.

words = ["cat", "dog", "apple", "hi", "banana", "sun", "book"]
group = {}
for i in words:
    key = len(i)
    if key not in group:
        group[key] = []
    group[key].append(i) 

print('with condition:',group)     

#shorter version using setdefault
group2 ={}
for i in words:
    key = len(i)
    group2.setdefault(key,[]).append(i)

print('using setdefault():',group2)