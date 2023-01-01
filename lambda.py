dev = [
    {"language": "Javascript", "database": "MongoDB"},
    {"language": "Python", "database": "Django"},
    {"language": "C", "database": "SQL"}
]

# def f(dev):
#     return dev["language"]

# dev.sort(key=f)

dev.sort(key=lambda lang: lang["language"])

print(dev)