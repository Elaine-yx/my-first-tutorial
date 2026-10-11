# *args    = allows you to pass multiple non_key argument
# **kwargs = allows you to pass multiple keyword-argument
#            * unpacking operator
#                     1. positional 2. default 3. keyword 4. ARBITRARY

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add(1))