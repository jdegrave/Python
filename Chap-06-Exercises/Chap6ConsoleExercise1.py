"""
    @Author  Jodi A DeGrave
    @Data    3/13/2016
    These are the exercises in Chapter 6
"""

def get_PentagonalNumber(n):
    """
    Compute the pentagonal numbers
    :param n: the number to compute the pentagonal numbers
    :return:  the pentagonal numbers

    """
    n = n * ((3 * n) - 1)//2
    return n


def print_pentagonal_numbers(pent_number):
    """
    Prints the pentagonal number 10 to a line
    :param pent_number: the pentagonal number to print
    :return:  none

    """
    print(format(pent_number, "10d"), end="\t")

def main():

    """
    Calls the get_pentagonal_numbers(n) function to calculate the pentagonal numbers for each number from 1 to 100
    Calls the print(pentagonal_numbers()  function to print the pentagonal numbers in a rows of 10
    :param: none
    :return: none

    """
    # Exercise 1 - Print the first 100 pentagonal numbers with 10 numbers per line
    print("EXERCISE 1: Print the 1st 100 pentagonal numbers:\n")

    max_number = 100               # max number of pentagonal numbers to calculate
    max_row_items = 10             # max number of items to print in 1 row

    for i in range(1, (max_number + 1)):
        pentagonal_number = get_PentagonalNumber(i)
        print_pentagonal_numbers(pentagonal_number)
        if i % max_row_items == 0:
            print()


main()