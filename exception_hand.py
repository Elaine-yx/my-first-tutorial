try:
    divisor = float(input("Enter the divisor: "))

    result = 10 / divisor
    print(result)
except ValueError:
    print("Please enter vaild input")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
finally:
    print("Finish processing")
