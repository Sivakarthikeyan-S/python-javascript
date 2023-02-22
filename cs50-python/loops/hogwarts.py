students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" : ")


#########################################################################################

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(f"{student} : {students[student]}")


# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

#########################################################################################

# students = ["Hermione", "Harry", "Ron"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# for i in range(len(students)):
#     print(f"{i + 1}: {students[i]}")

# for student in students:
#     print(student)