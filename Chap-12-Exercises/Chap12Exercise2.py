from Location import Location


def build_2D_matrix(matrix, rows, columns):
    """
    Prompts the user to enter each row element in the 2D list
    :param matrix: empty matrix which will hold the 2D list
    :param rows: the number of rows in the 2D matrix
    :param columns: the number of columns in the 2D matrix
    :return: 2D matrix of floats
    """


    for i in range (rows):
        matrix.append([])
        raw_list = input("Enter " + str(columns) + " elements as floats for row " + str(i) + ": ").split()
        new_list = [float(x) for x in raw_list]
        matrix[i].extend(new_list)

    return matrix


def main():
    """
    This program prompts the user to create a 2D matrix and then finds the largest element and its index in
    the 2D list.
    It uses the Location class to perform the search for the largest element and its index
    :return: None
    """
    matrix = []

    # get size of matrix and build it with user-provided data
    rows, columns = eval(input("Enter the number of rows and columns in the 2-D list, separated by commas: "))
    matrix = build_2D_matrix(matrix, rows, columns)
    Location(matrix)

main()





