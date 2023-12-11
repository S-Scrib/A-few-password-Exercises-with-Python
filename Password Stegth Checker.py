# Ok, going to make a password stregth checker. First, I need to import some data. Going to make  the criteria
# of 12 characters long, needs at least one upper and one lower case letter, one digit, and a special character.

import re

def validate_password(password):
    # belwo checks if the password is at least 12 characters
    if len(password) < 12:
        return False

    # Now lets make sure it has the other requirements. First is uppercase letter.
    if not re.search(r'[A-Z]', password):
        return False
    #next is lowercase letter:
    if not re.search(r'[a-z]', password):
        return False
    # next is digits:
    if not re.search(r'\d', password):
        return False
    # Lastly, special characters
    if not re.search(r'[!@#$%^&*()":{}|<>]', password):
        return False

    # now, we can define that if the password conditions are met, the password is valid:
    return True

password = input("Input your password")
is_valid = validate_password(password)

if is_valid:
    print("Valid Password")
else:
    print("Password does not meet requirements.")