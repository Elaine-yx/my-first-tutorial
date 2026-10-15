# if _name_ == __main__: (this script can be imported OR run standalone)
#                        Functions and classes in this module can be reused
#                        without the main block of code executing

# Ex. library = Import library for functionality.
#               When running library directly, display a help page.
# Good practice (code is modular,
#                helps readability,
#                leaves no global variables,
#                avoids unintended execution)


# --------- script1.py ---------
# This file can run standalone or be imported

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()