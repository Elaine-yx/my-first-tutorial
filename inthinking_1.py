# Task 1: Basic Variable Declaration and Asssignment
age = 15
name = "ELaine"

print(age)
print(name)

# Task 2: Data Type Conversion
price = 12.24
integer_price = int(price)

print(price)
print(integer_price)

# Task 3: Global and Local Variables
global_count = 0
def increment_count():
    global global_count
    global_count += 1

increment_count()
increment_count()

print(global_count)

