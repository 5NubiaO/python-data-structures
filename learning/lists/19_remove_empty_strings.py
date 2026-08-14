#Take a list of strings that contains empty entries (" ") and remove them to keep only the valid text
names = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for n in names:
    if "" in names:
        names.remove("")

print(names)

#Method using filter with none
'''
names = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# ilter(None, ...) removes all "Falsy" values (empty strings, 0, None)
cleaned_names = list(filter(None, names))
print(f"Cleaned Names: {cleaned_names}")
'''