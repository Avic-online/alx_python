def validate_password(password):
    if len(password) < 8:
        return False
    # elif password.lower():
    elif password.islower():
        return False
    elif password.isupper():
        return False
    elif password.isdigit():
        return False
    elif " " in password:
        return False
    else:
        return True
    