def main():
    hello()
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()

# # Ask user for their name
# name = input("What's your name? ").strip().title()

# # Split user's name into first name and last name
# first, last =  name.split(" ")

# print(f"hello, {first}")

# # Say hello to user
# print(f"hello, {name}")

# print("hello, "+name)
# print("hello, ", end="")
# print(name)
# print("hello,",name, sep=" ")

# Remove whitespace from string and capitalize user's name
# name = name.strip().capitalize()