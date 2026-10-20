# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]


# doubles = [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]

# print(squares)


# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruit_chars)


# numbers = [1, -2, 3, -4, 5, -6]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_num = [num for num in numbers if num % 2 == 0]
# odd_num = [num for num in numbers if num % 2 == 1]

# print(even_num)


grades = [85, 43, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)