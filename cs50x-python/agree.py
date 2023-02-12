import re

s = input("Do you agree? ")

s = s.lower()

if re.search("^y(es)?$", s):
    print("Agreed")
elif re.search("^no?$", s):
    print("Not Agreed")