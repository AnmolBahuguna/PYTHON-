def is_palindrome(number):
    # Convert number to string for easy comparison111
    original = str(number)
    reversed_num = original[::-1]
    
    if original == reversed_num:
        return True
    else:
        return False

# Input from user
num = int(input("Enter a number: "))

# Function call
if is_palindrome(num):
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
