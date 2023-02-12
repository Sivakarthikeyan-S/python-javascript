import sys

names = ["Siva", "Guru", "Gowtham", "Nambi", "Sankar", "Karthi"]

name = input("Name: ")

if name.capitalize() in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)