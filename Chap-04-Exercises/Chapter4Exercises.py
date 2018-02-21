import math
import random

''' Chapter 4 Console Exercises
    @Author:  Jodi A. DeGrave
    @Date:  3/6/2016
'''

# Exercise 4.1: Quadratic equation finding the number of roots
print("EXERCISE 4.1: Quadratic equation - find the roots\n")
a, b, c = eval(input("Enter three numbers: "))
discriminant = (b * b) - (4 * a * c)
if discriminant < 0:
    print("The equation has no real roots")
elif discriminant == 0:
    root1 = (-b + math.sqrt(discriminant))/(2 * a)
    print("The root is ", str(root1))
else:
    root1 = (-b + math.sqrt(discriminant))/(2 * a)
    root2 = (-b - math.sqrt(discriminant))/(2 * a)
    print("The roots are " + str(root1) + " and " + str(root2))
print()


# Exercise 4.2: Game: Add three numbers
print("EXERCISE 4.2: Game - add three numbers\n")

# Generate three random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " + " + str(number2) + " + " + str(number3) + "? "))

# Display result
print(number1, "+", number2, "+", number3, "=", answer, "is", number1 + number2 + number3 == answer)
