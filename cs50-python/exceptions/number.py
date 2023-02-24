def main():
    x = get_int("What's x?")
    print(f"x is {x}")
    
    
def get_int(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            pass
main()