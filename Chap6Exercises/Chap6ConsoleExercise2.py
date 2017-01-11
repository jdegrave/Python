"""
    @Author  Jodi A DeGrave
    @Data    3/13/2016
    These are the exercises in Chapter 6
"""


def sum_digits(n):

    """
    Adds the digits of an integer. Limit is what python and/or the computer can hold
    :param n: the integer whose digits will be summed
    :return my_sum:  the sum of the integer's digit

    """

    my_sum = 0
    total_digits = number_length(n)        # get the length of the integer to determine divisor
    divisor = 10 ** (total_digits - 1)     # subtract 1 from total_digits to have exact number of loops
    for i in range(1, (total_digits + 1)):
        if divisor != 0:
            my_sum += (n // divisor)    # extract a digit
            n %= divisor                # store the remaining digits
        divisor //= 10               # decrement the divisor by a power of 10
    return my_sum


def number_length(num):
    """
    This finds the number of digits that comprise any given integer
    :param num: the integer
    :return number_of_digits:  the number of digits  in the integer
    """
    number_of_digits = len(str(num))
    return number_of_digits


def main():

    """
    Sum the digits of an integer of any length - any length that the hardware and python will allow
    :param: none
    :return: none

    """
    # Exercise 2.6: Sum the digits in an integer
    print("\nEXERCISE 2: Sum the digits in an integer\n")
    my_integer = eval(input("Enter an integer: "))
    my_sum = sum_digits(my_integer)
    print("%s%d%s%d\n" % ("The sum of the digits of ", my_integer, " is ", my_sum))


main()