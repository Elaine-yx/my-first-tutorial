# collection = single "variable" used to store multiple values
#   List = [] ordered and changeale. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

'''
# list
fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(fruit[::2])
# print(len(fruits))

# print("apple" in fruits)
# for fruit in fruits:
#     print(fruit)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))


print(fruits)
# print(fruits[0])
# for fruit in fruits:
#     print(fruit)

'''

'''
# set
fruits = {"apple", "orange", "banana", "coconut"}

# fruits.add("pineapple")
# fruits.remove("apple")
fruits.pop()

print(fruits)
'''

# tuple
fruits = ("apple", "orange", "banana", "coconut")

print(fruits.index("apple"))
print(fruits.count("coconut"))