import os.path
import random
import sys


def random_word_generator(filename):
    """
    This selects a random word from a file containing a list of 250 words.
    :param filename: string Contains 250 words in a list
    :return: str  the selected word
    """
    random_word_file = open(filename, "r")
    all_words = random_word_file.read().split()
    word = random.choice(all_words)
    return word


def play_hangman(true_word):
    """
    Creates a string of asterisks to hide the word

    Checks the player's guess for the following cases and provides and displays an appropriate response:
     - multiple characters - counts as a missed guess
     - non alpha characters - counts as a missed guess
     - previously guessed and not in word - counts as a missed guess
     - new guess and not in word - counts as a missed guess
     - previously guessed and in word -
     - new guess and in word - rebuilds the string replacing asterisks with the letter of the correct guess

    :param true_word:
    :return: none
    """

    guess_word = len(true_word) * '*'
    test_string = len(true_word) * ['*']     # list to generate placement of correct guesses
    used_letters = []
    wrong_guesses = 0

    print("The word is '" + true_word + "'")  # Convenience measure for instructor's evaluaton

    while guess_word != true_word:

        is_wrong = True
        is_used_letter = False

        letter = input("Guess a letter in the word " + str(guess_word) + ": ").lower().strip()

        if letter.isalpha() == False or len(letter) != 1:
            print("Yikes! This is not a letter, or it has too many characters, or both. \n")

        elif letter not in used_letters and letter not in true_word:
            print("Letter '" + letter + "' isn't in the word.\n")
            is_used_letter = True

        elif letter not in used_letters and letter in true_word:
            is_wrong = False
            is_used_letter = True
            guess_word = ""

            #  My original way:
            #  for i in range(len(true_word)):
            #     if true_word[i] == letter:
            #         test_string[i] = letter
            #     guess_word += test_string[i]
            #
            #  Preferred way is shown below

            i = 0
            for ch in true_word:
                if true_word[i] == letter:
                    test_string[i] = letter
                guess_word += test_string[i]
                i += 1

        elif letter in used_letters and letter in true_word:
            is_wrong = False
            print("\nYou already guessed '" + letter + "'.  All occurrences are already shown in the word.")

        else:
            print("\nYou already guessed '" + letter + "' and it wasn't in the word.\n")

        if is_wrong:
            wrong_guesses += 1

        if is_used_letter:
            used_letters.append(letter)

    print("\nYou got it! The word is " + true_word + ". You missed " + str(wrong_guesses) +
          (" time.\n" if wrong_guesses == 1 else " times.\n"))


def main():
    """
    This is a programmatic version of the Hangman game. The player is continually prompted to play the game until
    he or she responds with 'n' or 'no' (case in-sensitive). The word to guess is randomly selected from a
    file containing 250 words.

    Main checks to ensure the file exists, and that the file has data before beginning the game.

    :return: None
    """
    stop = False
    filename = "Words.txt"
    yes_list = ["y", "yes"]
    no_list = ["n", "no"]

    while not stop:
        start_stop = str(input("Ready to play hangman?  ")).lower().strip()

        if start_stop in yes_list:

            if os.path.isfile(filename):
                try:
                    the_word = random_word_generator(filename)
                except Exception:
                    print(filename + " has no data. No words to fetch. Please provide a file with valid data."
                                     " Quitting Hangman game.\n")
                    sys.exit()
                else:
                    play_hangman(the_word)

            else:
                print("File name is incorrect or not found. Check the spelling of the file name in main(). "
                      "Exiting Hangman game.")
                sys.exit()

        elif start_stop in no_list:
            stop = True
            print("\nAlrighty, then! Later, Doodles!")

        else:
            print("\nSorry, but I don't understand your response '" + start_stop + "'. Please indicate 'Yes' or 'No' "
                  "if you want to play the game or not.\n")

main()