def main():
    height = get_height()
    for i in range(height):
        for j in range(height):
            print("#", end="")
        print()


def get_height():
    while True:
        try:
            n = int(input("Height: "))
        except ValueError:
            print("Not an integer")
        else:
            if n > 0 and n < 9:
                return n


main()