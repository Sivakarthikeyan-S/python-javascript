def main():
    # print_column(3)
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


# def print_square(size):
#     for i in range(size):
#         for j in range(size):
#             print("#", end="")
#         print()


def print_row(width):
    print("#" * width)


def print_column(height):
    print("#\n" * height, end="")

    # for _ in range(height):
    #     print("#")

main()

#########################################################################

# for _ in range(5):
#     print("#")