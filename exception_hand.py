try:
    divisor = float(input("Enter the divisor: "))

    result = 10 / divisor
    print(result)
except ValueError:
    print("Please enter vaild input")
finally:
    print("Finish processing")