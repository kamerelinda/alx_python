def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
        # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
    lower = upper = digit = False

    for i in password:
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
        if i.isdigit():
            digit = True
        # If all required character types are found, break the loop to save unnecessary iterations
        if lower and upper and digit:
            break
    if not (lower and upper and digit):
        return False
        # Check if the password contains spaces
    if " " in password:
        return False
    return True
