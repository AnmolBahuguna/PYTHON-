try:
    x = int(input("Enter number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Result is:", result)
finally:
    print("This always runs.")
