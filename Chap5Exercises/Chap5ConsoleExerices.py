import math
import random
import time

'''
    Chapter 5 Console Exercises
    @Author Jodi A DeGrave
    @Date  3/6/2016

'''

# Exercise 5.1:  Integer fun
print("EXERCISE 5.1: Enter integers, find average, count of positive ints, and count of negative ints")
my_int = eval(input("Enter an integer. The input ends if you enter 0 (zero): "))
if my_int == 0:
    print("You quit before you started!")
    print('\n')
else:
    pos_int_count = 0
    neg_int_count = 0
    sum = 0
    average = 0

    while my_int != 0:
        sum += my_int
        if my_int > 0:
            pos_int_count += 1
        else:
            neg_int_count += 1
        my_int = eval(input("Enter an integer. The input ends if you enter 0 (zero): "))

    average = sum / (pos_int_count + neg_int_count)

    print("The number of positive integers is ", pos_int_count)
    print("The number of negative integers is ", neg_int_count)
    print("The total is ", sum)
    print("The average is ", format(average, ".2f"))
    print()


# Exercise 5.2:  10 Random addition problems
print("EXERCISE 5.2: 10 random addition problems of numbers between 1 and 15")

correct_count = 0          # Count the number of correct answers
count = 0                  # Total number of questions
NUMBER_OF_QUESTIONS = 10   # Constant of max questions

start_time = time.time()   # Get start time

while count < NUMBER_OF_QUESTIONS:
    # Generate two random numbers between 1 and 15
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)

    # Prompt the student to answer "What is the sum of number1 + number2?"
    answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

    # Grade the answer and display the result
    if number1 + number2 == answer:
        print("You are correct!\n")
        correct_count += 1
    else:
        print("Your answer is incorrect :-( \n", number1, " + ", number2, " is ", number1 + number2, "\n")

    # Increment the count of questions
    count += 1

end_time = time.time()
test_time = int(end_time - start_time)
print("Correct count is: ", correct_count, "out of", NUMBER_OF_QUESTIONS, "\nTest time is", test_time, "seconds")
