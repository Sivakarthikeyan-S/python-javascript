import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)


# if len(sys.argv) < 2:
#     sys.exit("Too few arguements")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])
    
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguements")