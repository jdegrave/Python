"""
    Chapter 8 Exercise 3 - Validate Password
    User enters in password. To be valid, it must meet all of the following criteria:
    - at least 8 characters
    - only letters and digits
    - at least 2 characters are digits

    Main calls the validate_password function, which returns a boolean variable.
    Main calls the print_password validation message function based on the return value of the validation function

    @Author  Jodi A. DeGrave
    @Version 1.0.0
    @Date 4/3/2016
"""

def print_passwd_val_message(validator):
    if validator == True:
        print("Valid password")
    else:
        print("Invalid password")


def validate_password(password_test):
    """
    Function to validate a password. Passwords must meet the following criteria:
     - at least 8 characters
    - only letters and digits
    - at least 2 characters are digits

    :param password_test: string
    :return is_valid: boolean
    """

    is_valid = False

    # Password must be at least 8 characters
    if len(password_test) < 8:
        pass

    # Password must be alpha or numeric characters only
    elif password_test.isalnum() == False:
        pass

    # Check for two numbers in the password
    # ord = 48 - 57
    else:
        integer_sum = 0

        for ch in password_test:
            # if ch.isdigit() == True:
            #   integer_sum += 1
            if 48 <= ord(ch) <= 57:
                integer_sum += 1

        if integer_sum >= 2:
            is_valid = True

    return is_valid



def main():
    password_entered = input("Enter a password: ").strip()
    valid_password = validate_password(password_entered)
    print_passwd_val_message(valid_password)


main()
