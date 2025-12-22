def password_checker(password):
    if len(password) < 8:
        return "Password too short"
    elif not any(char.isdigit() for char in password):
        return "Password must contain a number"
    elif not any(char.isupper() for char in password):
        return "Password must contain an uppercase letter"
    elif not any(char.islower() for char in password):
        return "Password must contain a lowercase letter"
    elif not any(char in "!@#$%^&*()_+" for char in password):
        return "Password must contain a special character"
    else:
        return "Password is valid"