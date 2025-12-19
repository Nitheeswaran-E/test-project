def is_even(number):
    return number % 2 == 0

# Example usage
if __name__ == "__main__":
    test_number = 4
    if is_even(test_number):
        print(f"{test_number} is even.")
    else:
        print(f"{test_number} is odd.")