def is_palindrome(s):
    return s == s[::-1]

# Test cases
print(is_palindrome('radar'))  # True
print(is_palindrome('hello'))  # False