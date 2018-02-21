"""
    Excercise 1: Assign Grades
    Author:  Jodi A. DeGrave
    Date:    04/14/2016

    This program takes scores entered at the console (separated by spaces) and then assigns a letter grade and prints
    the score and letter grade for each student
"""


def assign_grades(score_list):
    """
    takes the score and assigns it to a letter grade
    :param score_list: an integer
    :return: letter grade
    """
    best = 100
    if score_list >= best - 10:
        grade = "A"
    elif score_list >= best - 20:
        grade = "B"
    elif score_list >= best - 30:
        grade = "C"
    elif score_list >= best - 40:
        grade = "D"
    else:
        grade = "F"
    return grade


def main():
    raw_results = input("Enter a list of scores separated by a space: \n").split()

    # list comprehension to convert the raw_results strings to integers
    scores = [int(x) for x in raw_results]

    # for each score in the list, assign a letter grade and then print out the score and letter grade
    for i in range((len(scores))):
        letter_grade = assign_grades(scores[i])
        print("Student", i, "score is", scores[i], "and grade is", letter_grade)


main()