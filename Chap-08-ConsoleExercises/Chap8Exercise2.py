"""
    Chapter 8 Exercise 2 - Find Function

    My own implementation of the Python "find" function.

    Find returns the lowest index in the string where substring 1 starts. Returns -1 if substring 1 is not found
    in the original string

    Main calls the my_find function, which returns an integer.
    Main calls the print_my_find_results_message function to print the results of the my_find function

    @Author  Jodi A. DeGrave
    @Version 1.0.0
    @Date 4/3/2016
"""

def print_my_find_results_message(found,substring1, orig_string):
    if found == -1:
        found_var = "not in"
    else:
        found_var = "in"
    print(substring1,"is", found_var, "orig_string" )



def my_find(find_string, orig_string):
    """
    Function to find the first occurrence of a substring in a string. :
    
    :param find_string: string
    :param orig_string: string
    :return found: integer  If substring is found, returns index of the first occurence; otherwise returns -1
    """    

    found = -1
    length_find_string = len(find_string)
    length_orig_string = len(orig_string)



    # check to see if the first character is found in both the substring and the original string
    if find_string not in orig_string:
        return found

    # if the strings are the same length, the first occurrence is at index 0
    elif length_find_string - length_orig_string == 0:
        found == 0
        return found
    else:

        index_start = 0
        same = False
        i = 0
        j = 0
        restart = False
        # find the first possible occurrence of the substring

        while i < len(find_string):
            while find_string[index_start] != orig_string[j]:
                j += 1
            index_start = j
            j += 1






        return found



        return found



def main():
    the_substring, original_string = input("Enter two strings: ").split()
    found = my_find(the_substring, original_string)
    print(found)


main()
