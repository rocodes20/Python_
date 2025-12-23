info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]
uniqSubjects = set()
englishstu = []
for item in info:
   uniqSubjects.add(item[1])
   if item[1] == "English":
      englishstu.append(item[0])

print(uniqSubjects)
print(englishstu)
