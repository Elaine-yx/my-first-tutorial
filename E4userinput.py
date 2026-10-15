# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# age += 1
# print(f"Hello {name}")
# print(f"You are {age} years old")

# mad libs
'''
adj1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adj2 = input("Enter an adjective: ")
verb = input("Enter an verb: ")
adj3 = input("Enter an adjective: ")
print(f"Today I went to a {adj1} zoo.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adj2} and {verb}ing")
print(f"I was {adj3}")
'''

# area calculator
'''
length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))

volume = length * width * height
print(f"The area is: {volume}cm^3")
'''

# shopping cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have brought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")