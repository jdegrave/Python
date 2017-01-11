"""
    Excercise 2: Reverse the numbers entered
    Author:  Jodi A. DeGrave
    Date:    04/14/2016

    This program takes a series of numbers entered at the console (separated by spaces) and then prints the numbers in
    reverse order. Because all input is by default a string, this program converts the strings to integers
"""


def main():
    raw_number_list = input("Enter a series of integers: ").split()

    # create a list comprehension that converts the elements from strings to integers
    number_list = [int(x) for x in raw_number_list]

    # reverse the list and then print the list
    number_list.reverse()
    print(number_list)

main()