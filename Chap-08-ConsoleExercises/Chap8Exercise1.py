"""
    Chapter 8 Exercise 1 - Validate SSN
    User enters in a Social Security Number (SSN) in the format ddd-dd-dddd
    Function validates if it is in the correct format

    @Author  Jodi A. DeGrave
    @Version 1.0.0
    @Date 4/3/2016
"""

def print_results_message(is_valid):
    if is_valid:
        print("Valid SSN")
    else:
        print("Invalid SSN")


def validate_SSN(SSN_test):
    """
    Function to validate a social security number (SSN). SSN is considered valid if user breaks format (i.e., omits
    dashes) and enters 9 digits, no white space. Otherwise, the SSN entered must be in the format ddd-dd-dddd, where
    "d" is a digit

    :param SSN_test: string the user entered
    :return is_valid_SSN: boolean
    """

    is_valid_SSN = False

    # if user breaks format but enters 9 digits, SSN is counted as valid
    if len(SSN_test) == 9 and SSN_test.isdigit():
        is_valid_SSN = True


    # otherwise, if the length is not 11 characters, and there aren't at least 2 dashes, entry immediately fails
    elif len(SSN_test) != 11 or (SSN_test.count("-") != 2):
        pass

    # if the dashes are in the wrong place, entry fails
    elif (SSN_test[3] != "-") and (SSN_test[6] != "-"):
        pass

    # dashes are correct, but all other characters must be numbers
    else:
        valid_SSN1 = (SSN_test[0 : 3]).isdigit()
        valid_SSN2 = (SSN_test[4 : 6]).isdigit()
        valid_SSN3 = (SSN_test[7 : ]).isdigit()
        if (valid_SSN1 and valid_SSN2 and valid_SSN3):
            is_valid_SSN = True
        else:
            is_valid_SSN = False

    return is_valid_SSN


def main():
    SSN_entered = input("Enter a Social Security Number (SSN) in the format 'ddd-dd-dddd': ").strip()
    valid_SSN = validate_SSN(SSN_entered)
    print_results_message(valid_SSN)

main()

