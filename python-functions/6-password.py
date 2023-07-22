def validate_password(password):
    if len(password) > 8:
        lower = upper = digit = special = False

        for i in password:
            if i.islower():
                lower = True
            if i.isupper():
                upper = True
            if i.isdigit():
                digit = True
            if i.isalnum():
                special = True
        return lower and upper and digit and special
    else:
        return False
