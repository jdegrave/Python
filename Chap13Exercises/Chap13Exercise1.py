import os.path
import sys


def create_file(filename, text_string, overwrite_flag):
    """
    Creates a test file with some strings to search.
    :param filename: string name of the file to write to
    :param text_string:
    :return: None
    """
    if overwrite_flag:
        my_file = open(filename, "w")
        my_file.write("Line 1: What an amazing morning. What an amazing mooning.\n")
        my_file.write("Line 2: mourning manning monkey mable. Morning weather report. Sunday Morn ")
        my_file.write("Line 2 part two: afternoon is sunny. Morning coffee. morning coffee \n")
        my_file.write("Just another morning in the city. Just another slurp of coffee")
        my_file.write("Morning, Sunshine! Afternoon delight. Age-old glory.")
        my_file.close()
    else:
        my_file = open(filename, "w")
        my_file.write(text_string)
        my_file.close()


def read_file(filename):
    """
    Reads the file just created into a string
    :param filename: string
    :return: string
    """

    my_file = open(filename, "r")
    my_string = my_file.read()
    my_file.close()
    return my_string


def remove_word(filename, text_string, find_string, overwrite_flag):
    """
    Searches the string created in read_file() and replaces all occurrences with the replacement string. The existing
    file is overwritten with the new string.


    :param filename:  String
    :param text_string: String containing all data read from the file
    :param find_string: String to be replaced.
    :return: int  number of occurrences of the replacement string that was removed
    """

    replacement_string = ''
    removal_count = text_string.count(find_string)

    if removal_count == 0:
        pass
    else:
        new_string = text_string.replace(find_string, replacement_string)
        create_file(filename, new_string, overwrite_flag)
    return removal_count


def main():
    """
    This program creates a file and then writes lines of random text to it, and prompts the user for a string to remove
    from the file.
    Main calls remove_word to remove the string from the file and then displays the number of occurrences of the string
    that was removed.
    :return: None
    """
    text_string = ''
    answer_list = ['y', 'yes']
    answer = "no"
    overwrite = True

    filename = input("Enter a file name with a 'txt' extension: ")

    if os.path.isfile(filename):
        answer = str(input("File already exists. Overwrite? ")).lower().strip()
        if answer in answer_list:
            print("Overwriting " + filename + ".")
        else:
            print("Using existing file.")

    if not(os.path.isfile(filename)) or answer in answer_list:
        create_file(filename, text_string, overwrite)

    try:
        overwrite = False
        text_string = read_file(filename)
        find_string = input("Enter the string to be removed: ")
        count = remove_word(filename, text_string, find_string, overwrite)
        print("Done. Removed " + str(count) + (" occurrences" if count != 1 else " occurrence ") + " of '" +
              find_string + "'.")
    except EOFError:
        print(filename + " has no data. Please provide a file with valid data. Exiting program now.\n")
        sys.exit()


main()
