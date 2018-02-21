import math
import time

""" Chapter 2 Console Exercises 2.1 through 2.7.
    @Author:  Jodi A. DeGrave
    @Date:    2/14/2016
    @Version: 1.0.0
"""

'''
# Exercise 2.1: Convert Celsius to Fahrenheit
print("EXERCISE 2.1: Convert Celsius to Fahrenheit")
celsius_temp = eval(input("Enter a degree in Celsius (just numbers) to convert to Fahrenheit: "))
fahrenheit_temp = (9 / 5) * celsius_temp + 32
print("%.1f%s%.1f\n" % (celsius_temp," converted to Fahrenheit is: ", fahrenheit_temp))


# Exercise 2.2: Compute the area and volume of a cylinder
print("EXERCISE 2.2: Compute the area and volume of a cylinder")
radius, length = eval(input("Enter the radius and length of the cylinder, separated by commas: "))
area = radius * radius * math.pi
volume = area * length
print("%s%.2f%s" % ("The area of the cylinder is: ", area, " sq units"))
print("%s%.2f%s\n" % ("The volume of the cylinder is: ", volume, " cubic units"))



# Exercise 2.3: Convert feet into meters
print("EXERCISE 2.3: Convert feet into meters")
feet = eval(input("Enter the number of feet to convert: "))
meters = feet * 0.305
print("%.2f%s%.2f%s\n" % (feet, " ft is equivalent to ", meters, " m"))


# Exercise 2.4: Convert pounds into kilograms
print("EXERCISE 2.4: Convert pounds into kilograms")
pounds = eval(input("Enter the number of pounds to convert: "))
kilograms = pounds * 0.454
print("%.2f%s%.2f%s\n" % (pounds, " lb(s) is equivalent to ", kilograms, " kg"))



# Exercise 2.5: Calculate the total and the tip
print("EXERCISE 2.5: Calculate the total and the tip")
subtotal, tip  = eval(input("Enter the subtotal and the tip rate (as a whole number), separated by commas: "))
tip = (subtotal * tip)/100
total = subtotal + tip
print("%s%.2f%s%.2f\n" % ("The gratuity is: $", tip, " \nThe total is: $", total))


# Exercise 2.6: Sum the digits in an integer
print("EXERCISE 2.6: Sum the digits in an integer")
my_integer  = eval(input("Enter an integer between 0 and 1000: "))
original_integer = my_integer               # store the original integer value for printing later
my_sum = 0
divisor = 1000
for i in range (1,5):
    if divisor != 0:
        my_sum += (my_integer // divisor)    # extract a digit
        my_integer %= divisor                # store the remaining digits
    divisor //= 10                           # decrement the divisor by a power of 10
print("%s%d%s%d\n" % ("The sum of the digits of ", original_integer, " is: ", my_sum))


# Exercise 2.7: Find the number of years and days
print("EXERCISE 2.7: Find the number of years and days")
minutes = eval(input("Enter the number of minutes: "))
days = 24 * 60
years = 365 * days
num_of_years = minutes // years
num_of_days = ((minutes % years) // (days))
print("%d%s%d%s%d%s\n" % (minutes, " minutes is approximately ", num_of_years, " years and ", num_of_days, " day(s)"))



# Exercise 2.8: Calculate energy
# Calculate the energy using the following formula:  Q = M * (final_temp - initial_temp) * 4184 where
# Q = energy required measured in joules, and M = mass in kilograms
print("EXERCISE 2.8: Calculate the energy required to heat water from an initial temp to a final temp")
h2o_kilograms = eval(input("Enter the amount of water in kilograms: "))
initial_temperature = eval(input("Enter the initial temperature in degrees Celsius: "))
final_temperature = eval(input("Enter the final temperature in degrees Celsius: "))
q_energy = h2o_kilograms * (final_temperature - initial_temperature) * 4184
print("The energy needed is %.1f\n" % (q_energy))



# Exercise 2.9: Calculate wind chill
# Calculate wind chill using the following formula: windchill = 35.74 + 0.6215t- 35.75(v**0.16) + 0.4275t(v**0.16)
# where t = outside temperature in Fahrenheit and v = velocity in mph
print("EXERCISE 2.9: Calculate the wind chill for temps between -58 degrees Fahrenheit and 41 degrees Fahrenheit, inclusive")
outside_temperature = eval(input("Enter the outside temperature in degrees Fahrenheit: "))
velocity = eval(input("Enter a wind speed that is >= 2 mph: "))
windchill = 35.74 + (0.6215 * outside_temperature) - 35.75 * (velocity ** 0.16) + 0.4275 * outside_temperature\
    * (velocity **0.16)
print("The windchill index is %f" %(windchill))


# Exercise 2.10: Find minimum runway length
# Calculate minimum runway length using the formula:  length = v ** v / 2a where v = take off speed, a = acceleration
# speed is meters per second (m/s) and acceleration is meters per second squared (m/s**s)
print("EXERCISE 2.10: Calculate runway length")
take_off_speed, acceleration = eval(input("Enter speed in meters per second and acceleration in meters per second squared: "))
runway_length = (take_off_speed * take_off_speed) / (2 * acceleration)
print("The minimum runway length is %.3f meters" % (runway_length))


# Exercise 2.11: Initial Investment Amount
print("EXERCISE 2.11: Calculate initial deposit for a given final amount, interest rate, and time period")
final_amount = float(input("Enter the your desired final amount: "))
interest_rate = float(input("Enter the annual fixed interest rate, as a percent: "))
years = int(input("Enter the number of years to invest: "))

monthly_interest_rate = (interest_rate/100)/12
initial_deposit = (final_amount) / (1 + monthly_interest_rate) ** (years * 12)
print("Initial deposit value is: $", initial_deposit, "\n")


# Exercise 2.12: Print a table
print("EXERCISE 2.12: Print a table of powers")
print("%s%5s%8s" % ('a', 'b', 'a**b'))
for a in range(1,6):
    b = a + 1
    print("%-5d%-5d%d" % (a, b, a**b))
print("\n")


# Exercise 2.13: Reverse digits
print("EXERCISE 2.13: Reverse digits")
digits = int(input("Enter a 4-digit integer: "))
digit1 = digits//1000
digits %= 1000
digit2 = digits//100
digits %= 100
digit3 = digits//10
digits %= 10
print(digits, digit3, digit2, digit1)


# Exercise 2.14: Compute the area of a triangle using the following formulas:
# s = (side1 + side2 + side3) / 2   -   find the 1/2 perimeter
# area = sqrt(s(s-side1)(s-side2)(s(s-side3))
print("\nEXERCISE 2.14: Calculate the area of a triangle\n")
# Get coordinates
x1, y1, x2, y2, x3, y3 = eval(input("Enter three pairs of coordinates for the triangle vertices: "))

# Calculate the length of all three sides
side1 = math.sqrt(math.pow((x2 - x1),2) + (math.pow((y2 - y1), 2)))
side2 = math.sqrt(math.pow((x3 - x2),2) + (math.pow((y3 - y2), 2)))
side3 = math.sqrt(math.pow((x1 - x3),2) + (math.pow((y1 - y3), 2)))

s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))
print("The area of the triangle is %.2f square units.\n" % area)


# Exercise 2:15: Calculate the area of a hexagon
print("Exercise 2:15: Calculate the area of a hexagon")
side = eval(input("Enter the side length for the hexagon: "))
area = ((3 * (math.sqrt(3))) / 2) * math.pow(side, 2)
print("The are of the hexagon is %.4f square units.\n" % area)




# Exercise 2:16: Calculate average acceleration
print("Exercise 2:16: Calculate average acceleration given v0 (initial velocity), v1 (final velocity), and t (time)\n")
v0, v1, t = eval(input("Enter v0, v1, and t: " ))
area = (v1 - v0) / t
print("The average acceleration is", str(round(area, 4)), "units per second squared.\n")


# Exercise 2:17: Calculate BMI (Body Mass Index)
print("Exercise 2:17: Calculate BMI\n")
weight_lbs = eval(input("Enter your weight in pounds: "))
height_inches = eval(input("Enter your height in inches: "))

# convert pounds to kilograms, inches to meters
kilograms = weight_lbs * 0.45359237
meters = height_inches * 0.0254

# compute BMI
BMI = kilograms / (meters * meters)

# display BMI
print("BMI is %.4f" % BMI)

# Exercise 2:18: Find the current time from GMT
print("\nExercise 2:18: Calculate current time from GMT\n")
offset = eval(input("Enter the time zone offset to GMT: "))

# Get current time, in seconds
current_time_total_seconds = (int(time.time()))

# Get the seconds of the current time, add a leading zero if seconds are < 10
current_total_seconds = current_time_total_seconds % 60
if current_total_seconds < 10:
     current_total_seconds = str('0') + str(current_total_seconds)

# get the total current time minutes
current_total_minutes = current_time_total_seconds // 60

# get the minutes in the current hour, add a leading zero if minutes are less than 10
current_minute = current_total_minutes % 60
if current_minute < 10:
    current_minute = str('0') + str(current_minute)

# get the total current hours
total_hours = current_total_minutes // 60

# get the current hour
current_hours = total_hours % 24


print("The current time is ", "%d%s%s%s%0d" % (current_hours + offset, ":", current_minute, ":", current_total_seconds))


# Exercise 2:19: Calculate future investment via the formula:
#    final investment amount = orig invest amount * ((1 + monthly interest rate) ^ numberofmonths
print("\nExercise 2:19: Calculate future investment\n")
invest_amount = eval(input("Enter investment amount: "))
annual_interest_rate = eval(input("Enter annual interest rate: "))
monthly_interest_rate = (annual_interest_rate / 100) / 12
years = eval(input("Enter number of whole years: "))
future_investment_amount = invest_amount * (((1 + (monthly_interest_rate)) ** (years * 12)) )
print("Accumulated value is: $", "%s%.2f" % ("$", future_investment_amount))

# Exercise 2:20: Calculate the interest on the next monthly payment using the formula:
#    interest = balance * (annual interest rate / 1200)
print("\nExercise 2:20: Calculate the amount of interest in the next monthly payment \n")
balance, interest_rate = eval(input("Enter balance and input rate (e.g. 3, for 3%): "))
interest = balance * (interest_rate/1200)
print("The interest on the next payment is", "%s%.2f" % ("$", interest))


# Exercise 2:21: Compound interest:
print("\nExercise 2:21: Calculate the amount of a regular monthly investment amount with compound interest\n")
monthly_investment_amount, months, annual_interest_rate  = eval(input("Enter the monthly investment amount and the "
                                                                      "number of months, "
                                                                      "and annual interest rate (as a percentage): "))
sum = 0
monthly_interest_rate = float((annual_interest_rate / 1200))

for i in range (0, (months)):
    sum =+ (sum + monthly_investment_amount) * (1 + monthly_interest_rate)

print("After ", months, "month(s), the account value is", "%s%.2f" % ("$",sum))


# Exercise 2:22: Population projection - refactor Exercise 1.11 to prompt user for number of years to project
print('EXERCISE 2.22 Projected US population growth over the number of years user provides\n')

years = eval(input("Enter the number of years: "))

base = 312032486

# Convert 1 year to seconds; designate 1 birth, 1 death, and 1 immigrant in seconds
birth = 7
death = 13
immigrant = 45
year_seconds = 365 * 24 * 60 * 60

#Yearly additional births, deaths, and immigrants
baby_count = year_seconds // birth
body_count = year_seconds // death
immi_count = year_seconds // immigrant

#Present data in a table
print('Base population =  %.0f' % base)
print('%s %10s  %10s %15s %15s' % ('Year', 'Births', 'Deaths', 'Immigrants', 'Total Pop'))  #print header
for x in range (1, (years + 1)):
    base = base + baby_count - body_count + immi_count
    print('%2d %12d  %10d %13d %17d' % (x, baby_count, body_count, immi_count, base))
    if x == years:
        print("\nThe population in", years, "years is", base)

'''
