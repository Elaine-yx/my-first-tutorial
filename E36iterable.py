# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5]

# numbers = (1, 2, 3, 4, 5)

# for number in numbers:
#     print(number, end=" - ")

# fruits = {"apple", "orange", "banana", "coconut"}
# #'set' object is not reversible
# for fruit in fruits:
#     print(fruit)

# name = "Elaine Xie"

# for character in name:
#     print(character, end=" ")

my_dictionary = {"A": 1, "B": 2, "C": 3}

# # print key
# for key in my_dictionary:
#     print(key)

# # print value
# for value in my_dictionary.values():
#     print(value)

# print items
for key, value in my_dictionary.items():
    print(f"{key} = {value}")