"""
    Chapter 14 Exercise 1 - modify Listing 14.4 to print out the keywords counted.
    This program reads a file, if it exists, and counts the occurrences of Python keywords and
    prints out the keywords (no duplicates).
"""
import os.path
import sys


def main():
    """
        Create a set of all Python keywords, prompt for a file name. Check if the file exists, if not, print error
        message and exit; otherwise, continue processing.

        Read the file and count occurrences of keywords. Print out the count, and print out a list (technically a set)
        of the unique key words in the file.
    :return: None
    """

    key_words = {"and", "as", "assert", "break", "class",
                 "continue", "def", "del", "elif", "else",
                 "except", "False", "finally", "for", "from",
                 "global", "if", "import", "in", "is", "lambda",
                 "None", "nonlocal", "not", "or", "pass", "raise",
                 "return", "True", "try", "while", "with", "yield"}

    filename = input("Enter a Python source code filename: ").strip()

    if not os.path.isfile(filename): # Check if file exists
        print("File", filename, "does not exist")
        sys.exit()

    infile = open(filename, "r") # Open files for input

    text = infile.read().split() # Read and split words from the file

    unique_keywords = set()
    count = 0
    for word in text:
        if word in key_words:
            count += 1
            unique_keywords.add(word)

    print("The number of keywords in", filename, "is", count)
    print("The unique keywords in", filename, ("is" if count <= 0 else "are"), str(unique_keywords))

main()
