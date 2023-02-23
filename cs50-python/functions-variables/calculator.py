# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# z = (x / y)

# print(f"{z:.2f}")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    print("x cubed is", cube(x))


def square(n):
    return pow(n, 2)


def cube(n):
    return pow(n, 3)


main()