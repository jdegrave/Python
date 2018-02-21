"""
    Chapter 11 Exercise 4 - Compute the weekly hours for each employee, order in descending order of hours
    Author: Jodi A De Grave
    Date: 4/15/2016
"""


def get_hours(max_employees, max_days, week):
    """
        Prompts the user to enter the hours for day for each employee, converts the entries to a float value
        so they can be summed later.

    :param max_employees: # each employee is a row in the matrix (defined in main)
    :param max_days: # each day is a column in the matrix (defined in main)
    :param week: list of weekday names
    :return: matrix (2-D list) populated with the each employees hours
    """

    matrix = []

    print("\nEnter the hours for each day the employee worked. Enter all hours worked for all employees.")
    print("Use a", max_days, "day work week.")

    for employee in range(max_employees):
        print()   # blank row for formatting purposes
        matrix.append([])

        for day in range(max_days):
            input_string = "Enter the hours for " + week[day]+ " for Employee " + str(employee) + ": "
            raw_hours = input(input_string).split()
            hours = [float(x) for x in raw_hours]
            matrix[employee].append(hours)

    return matrix


def total_hours(m):
    """
    Calculate the total hours for each employee, and store the total and the index (identifier) for the employee
    in a new 2-D matrix
    :param m: matrix with each employees hours for each day of the week
    :return: hours_totals -
    """

    hours_totals = []
    i = 0           # index to store employee ID number
    for emp in m:
        total = 0
        hours_totals.append([])
        for hours in emp:
            total += sum(hours)
        hours_totals[i].append(total)
        hours_totals[i].append(i)
        i += 1
    return hours_totals


def sort_desc(totals_matrix):
    """
        Sorts the 2D array and then reverses it so employee with greatest number of hours is first in the list
    :param totals_matrix: 2D unsorted matrix of employee # and total hours for the week
    :return: totals_matrix  sorted in descending order
    """

    totals_matrix.sort()
    totals_matrix.reverse()

    return totals_matrix


def print_results(final_matrix):
    """
    Prints a table with headers, listing each employee's identifier and total hours for the week in descending order
    by hours
    :param final_matrix: sorted 2-D array (descending order by total hours)
    :return: None
    """
    print((format("\nEmployee #", "20s")), (format("Total Hrs", "20s")))
    for row in range(len(final_matrix)):
        column = 0
        print((format(str(final_matrix[row][(column + 1)]), ">5s")), end="\t ")
        print(format(float(final_matrix[row][column]), ">20.1f"))



def main():
    """
    Initializes:
        -- max # of week days in the week
        -- max # of employees
        -- a list called "WEEK" for the names of the week

    Main calls get_hours to create a 2D matrix of employees and their hours for each day of the week
    Main calls total_hours to create a 2D matrix with just the total hours for each employee and the employee ID #
    Main calls sort_desc to sort the total _hours matrix in descending order by total hours
    Main calls print_results to display a table showing each employee # and total hours for the week, descending order
    by total hours

    :return: None

    """

    MAX_DAYS = 7
    MAX_EMPLOYEES = 8
    WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    matrix = get_hours(MAX_EMPLOYEES, MAX_DAYS, WEEK)
    total_emp_hours = total_hours(matrix)
    sort_desc(total_emp_hours)
    print_results(total_emp_hours)


main()