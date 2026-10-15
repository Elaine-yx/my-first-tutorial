# --------- script2.py ---------
# This file should run only standalone

from E42script1 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

print("This is script2")
favorite_food("sushi")
favorite_drink("coffee")
print('Goodbye!')