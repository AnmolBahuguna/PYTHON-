def is_palindrome(text):
    if text == text[::-1]:
        print(  f"'{text}'is a palindrome.")
    else:
        print(  f"'{text}'is not a palindrome.")

# Example usage
is_palindrome("madam")
is_palindrome("hello")
