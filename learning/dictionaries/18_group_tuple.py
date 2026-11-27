#Group by grades
students = [
    ("Ana", 90),
    ("Luis", 75),
    ("Maria", 90),
    ("Pedro", 80),
    ("Sofia", 75),
    ("Carlos", 90)
]
group = {}
for i in students:
  group.setdefault(i[1],[]).append(i[0])

print(group)
