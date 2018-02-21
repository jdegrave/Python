import urllib.request
import pickle

def count_letters(s):
        counts = [0] * 26
        for ch in s:
            if ch.isalpha():
                counts[ord(ch) - ord('a')] += 1
        return counts

def main():
    """
    # Open the file
    outfile = open("Presidents.txt", "w")

    # Write data to the file
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barak Obama\n")

    # Close the file
    outfile.close()


    # Open file for input
    infile = open("Presidents.txt", "r")
    print("(1) Using read():")
    print(infile.read())

    # Close file
    infile.close()

    # Open file for input
    infile = open("Presidents.txt", "r")
    print("\n(2) Using read(number):")
    s1 = infile.read(4)
    print(s1)
    s2 = infile.read(10)
    print(repr(s2))

    # Close file
    infile.close()

    # Open file for input
    infile = open("Presidents.txt", "r")
    print("\n(3) Using readline(): ")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))

    # Close file
    infile.close()

    # Open file for input
    infile = open("Presidents.txt", "r")
    print("\n(4) Using readlines()")
    print(infile.readlines())

    # Close file
    infile.close()



    url = input("Enter a URL for a file: ").split()
    infile = urllib.request.urlopen(url)
    s = infile.read().decode()  # read the content as a string

    counts = count_letters(s.lower())

    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i]) + (" time" if counts[i] == 1 else " times"))

    """

    try:
        lst = 10 * [0]
        x = lst[10]
        print("Done")
    except IndexError:
        print("Index out of bound")
    else:
        print("Nothing is wrong")
    finally:
        print("Finally we are here")
    print("Continue")

def f():
    try:
        s ="abc"
        print(s[3])
    except ZeroDivisionError:
        print("Divided by zero!")

main()