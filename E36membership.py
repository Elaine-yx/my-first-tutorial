# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

# string
'''
word = "APPLE"

letter = input("Guess a letter in the secret word: ").upper()

if letter not in word:
    print(f"{letter} was not found")

else:
    print(f"There is a {letter}")
'''

# set
students = {"Spongebob", "Partrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")

else:
    print(f"{student} is a student")