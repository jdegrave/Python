import os.path
import sys

"""
    Chapter 14 Exercise 3 - modify Listing 14.4 and Exercise 1 to print out the count of each Ptyhon keyword.
    This program reads a file, if it exists, and counts the occurrences of each Python keyword in it and
    prints out the keywords, occurrence count for each, and total of all keyword occurrences in the file

    NOTE: This program does not differentiate between source code and comments - so if a keyword is in the comment
    it is counted.
"""


def check_word(key_words, unique_keywords, text):
    """
        Checks file against keyword list, adds the word to the list and counts occurrences
    :param unique_keywords: dictionary to store keyword and occurrence count
    :param text: the text of the source file
    :return: dictionary  Updated dictionary containing all keywords in file and the number of occurrence for each
    """

    for word in text:
        if word in key_words:
            if word in unique_keywords:
                unique_keywords[word] += 1
            else:
                unique_keywords[word] = 1
    return unique_keywords


def total_and_print(unique_keywords, filename):
    """
        Totals all occurrences of keywords and prints each keyword and its count of occurrences
    :param unique_keywords: dictionary  - contains keywords and count of occurrences
    :param filename: string  - filename of source file in which keywords were counted
    :return: None
    """

    keyword_list = list(unique_keywords.items())
    keyword_list.sort()
    total = 0
    for i in range(len(keyword_list)):
        print((format(str(keyword_list[i][0]), "10s")), "\t", format(str(keyword_list[i][1]), ">2s"))
        total += keyword_list[i][1]
    print("\nTotal occurrences of keywords in", filename, "is", str(total))


def main():
    """
        Create a set of all Python keywords, prompt for a file name. Check if the file exists, if not, print error
        message and exit; otherwise, continue processing.

        Read the file and count occurrences of keywords. Print out the kewywords found in the file, the count for each,
        and total number of occurrences overall
        .
    :return: None

        NOTE:  No distincton is made between commented text and source file text. Therefore, if a keyword occurs in a
        comment, it's counted.
    """
    unique_keywords = dict()
    key_words = {"and", "as", "assert", "break", "class",
                 "continue", "def", "del", "elif", "else",
                 "except", "False", "finally", "for", "from",
                 "global", "if", "import", "in", "is", "lambda",
                 "None", "nonlocal", "not", "or", "pass", "raise",
                 "return", "True", "try", "while", "with", "yield"}

    # Prompt for filename
    filename = input("Enter a Python source code filename: ").strip()
    print()

    # Check if file exists - if not, exit; otherwise, open and read file
    if not os.path.isfile(filename): # Check if file exists
        print("File", filename, "does not exist")
        sys.exit()
    else:
        infile = open(filename, "r") # Open files for input
        text = infile.read().split() # Read and split words from the file

    # check source code text against keywords and count occurrences of each keyword
    unique_keywords = check_word(key_words, unique_keywords, text)

    # total all keywords and print results
    total_and_print(unique_keywords, filename)

main()
