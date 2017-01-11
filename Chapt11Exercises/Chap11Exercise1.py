"""
    This program returns the sum of all the elements in a specified column in a matrix
    Author: Jodi A DeGrave
    Date:   4/15/2016
"""


def print_column_sum(matrix, max_columns):
    """
        Calls the sum_column function for each column in the matrix and prints the results
    :param matrix: matrix containing the columns to be summed
    :param max_columns: number of columns in the matrix
    :return: None
    """
    for i in range(max_columns):
        total = sum_column(matrix,i)
        print("Sum of the elements for column", i, "is", total)

def get_input(max_rows, max_columns,matrix):
    """
        Prompts the user to enter the numbers for each row of matrix, converts the entries to a float value
        so they can be summed later.

    :param max_rows: # of rows in the matrix (defined in main)
    :param max_columns: # of columns in the matrix (defined in main)
    :param matrix: an empty matrix created in main
    :return: matrix (2-D list) populated with the user's entries
    """

    for row in range(max_rows):
        # create a new empty row
        matrix.append([])

        # get the user's input
        input_string = "Enter a " + str(max_rows) + " x " + str(max_columns) + " matrix row for row " + str(row) + ": "

        # create the list from the string of numbers entered
        raw_values = input(input_string).split()

        # convert the string values to floats so they can be added later
        values = [float(x) for x in raw_values]

        # append the entire list the matrix
        matrix[row].extend(values)

    print()   # blank row for formatting purposes
    return matrix


def sum_column(m, column_index):
    """
    Calculates the sum of the column
    :param m: matrix containing the column to sum
    :param column_index: the index of the column to sum
    :return: total (integer)
    """

    total = 0
    for row in range(len(m)):
        total += m[row][column_index]
    return total


def main():
    """
    Main initializes the max # of rows and columns and creates an empty matrix, and calls get_input, to gather
    each row's entries. Main then calls print_column_sum to calculate the sum of each column and print the result.
    :return: None
    """

    MAX_ROWS = 3
    MAX_COLUMNS = 4
    matrix = []

    matrix = get_input(MAX_ROWS, MAX_COLUMNS, matrix)

    print_column_sum(matrix, MAX_COLUMNS)

main()