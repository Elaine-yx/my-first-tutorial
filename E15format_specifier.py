# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3000.14159
price2 = -980.65
price3 = 1200.34

# f: floating point number
# print(f"Price 1 is ${price1:.1f}") 
# print(f"Price 2 is ${price2:.1f}") 
# print(f"Price 3 is ${price3:.1f}") 

# Middle
# print(f"Price 1 is ${price1:^10}") 
# <, >

print(f"Price 1 is ${price1:+,.2f}") 
