# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

print("1", "2", "3", "4")
for x in range(1, 11):
    print(x, end=" ")

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", "John", "James")