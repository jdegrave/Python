import math

# Python Chapter 1 Exercises
# Contains code for Exercises 1-11 (non-turtle)
# Author: Jodi A. DeGrave
# Date:   2/6/2015


# Exercise 1.1 - Print three statements
print('EXERCISE 1.1: \n')
print('Welcome to Python')
print('Welcome to Computer Science')
print('Programming is fun \n')

# Exercise 1.2 - Display "Welcome to Python" 5 times
print ('EXERCISE 1.2: Display a statement 5 times \n')
phrase = 'Welcome to Python \n' * 5
print(phrase)

# Exercise 1.3 Display a pattern that says "FUN" using the letters
print('EXERCISE 1.3: Display a pattern \n')
print('FFFFFFF   U     U   NN    NN')
print('FF        U     U   NNN   NN')
print('FFFFFFF   U     U   NN N  NN')
print('FF         U   U    NN  N NN')
print('FF          UUU     NN   NNN \n')

# Exercise 1.4 Print a table of squares and cubes for values 1 through 4
print('EXERCISE 1.4: Print a table of squares and cubes for values 1 thru 4 \n')
print ('%2s %5s %5s' % ('a', 'a^2','a^3'))
for a in range (1, 5):
    print ('%2d %5d %5d' % (a, a*a, a*a*a))
print('\n')


# Exercise 1.5 Compute and display the result of 9.5 X 4.5 - 2.5 X 3 / 45.5 - 3.5
print ('EXERCISE 1.5: Compute a formula \n')
print(((9.5 * 4.5) - (2.5 * 3)) / (45.5 - 3.5), '\n')

# Exercise 1.6 Compute addition of numbers in a series
print ('EXERCISE 1.6: Sum the integers between 1 and 9, inclusive \n')
sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
print ('Sum = %d' % sum)
print()

# Exercise 1.7 Using two different levels of precision for the approximation of the value of pi, compute 4 X pi
print ('EXERCISE 1.7: Approximate pi using two different levels of precision \n')
pi5 = 3 * (1 - 1/3 + 1/5 + 1/7 + 1/9 - 1/11)


pi7 = 3 * (1 - 1/3 + 1/5 + 1/7 + 1/9 - 1/11 + 1/13 - 1/15)
print('The value of pi is approximately: ', pi5)
print('The value of pi is approximately: ', pi7, '\n')

# Exercise 1.8 Calculate the area and circumference of a circle
print('EXERCISE 1.8: Calculate the area and circumference of a circle \n')
radius = 5.5
print('The area of a circle with radius = 5.5: ', (radius * radius * math.pi))
print('The circumference of a circle with radius = 5.5: ', (2 * radius * math.pi), '\n')

#Exercise 1.9 Calclulate the area and perimeter of a rectangle
print('EXERCISE 1.9: Calculate the area and perimeter of a rectangle \n')
width = 4.5
length = 7.9
area = width * length
perimeter = (2 * width) + (2 * length)
print('Area of a rectangle with width %.1f and length %.1f = %.2f' % (width, length, area))
print('Perimeter of rectangle width %.1f & length %.1f = %.2f' % (width, length, perimeter))
print()

#Exercise 1.10 Convert runners speed from kmph to mph
print('EXERCISE 1.10: Convert a runner\'s speed from km per hour to mile per hour \n')
kilometers = 14
minutes = 45
seconds = 30
miles = kilometers/1.6         # 1.6 is conversion factore between miles and kilometers
time = minutes * 60 + seconds  #convert everything to seconds
rate = (miles / time) * 60 * 60
print('The runner\'s average speed is %.2f miles per hour (mph).' % (rate))
print()

#Exercise 1.11 Project US population over the next 5 years
print('EXERCISE 1.11 Projected US population growth over the next 5 years \n')
base = 312032486
#Convert 1 year to seconds; designate 1 birth, 1 death, and 1 immigrant in seconds
birth = 7
death = 13
immigrant = 45
year_seconds = 365 * 24 * 60 * 60

#Yearly additional births, deaths, and immigrants
babycount = year_seconds // birth
bodycount = year_seconds // death
immicount = year_seconds // immigrant

#Present data in a table
print('Base population =  %.0f' % base)
print('%s %10s  %10s %15s %15s' % ('Year', 'Births', 'Deaths', 'Immigrants', 'Total Pop'))  #print header
for x in range (1, 6):
    base = base + babycount - bodycount + immicount
    print('%2d %12d  %10d %13d %17d' % (x, babycount, bodycount, immicount, base))
