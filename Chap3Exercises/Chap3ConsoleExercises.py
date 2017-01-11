import math

"""
    Chapter 3 Exercises
    @author  Jodi A. DeGrave
    @version 1.0.0
    @date    2/28/2016
"""


# Exercise 3.1
print("EXERCISE 3.1: Calculate the area of a pentagon \n")
length = float(input("Enter the length from the center of the pentagon to a vertex: "))
# Calculate the length of a side
side = 2 * (length) * (math.sin(math.pi/5))
area = ((3 * (math.sqrt(3))/2) * (math.pow(side, 2)))
print("The area of the pentagon is: " + str(round(area,2)) + " square units \n")


# Exercise 3.2  Calculate the distance of the great circle. User enters longitue and latitude in degrees
# however, Python trig functions use radians, so have to convert to radians
print("EXERCISE 3.2: Calculate the distance of a great circle \n")

# Read in the coordinates of two points
point_a_latitude, point_a_longitude = eval(input("Enter the latitude and longitude for Point A in degrees: "))
point_b_latitude, point_b_longitude = eval(input("Enter the latitude and longitude for Point B in degrees: "))

RADIUS = 6371.01  # average radius of the earth in km


# Convert degrees to radians in order to use the math library trig functions
point_a_latitude = math.radians(point_a_latitude)
point_a_longitude = math.radians(point_a_longitude)
point_b_latitude = math.radians(point_b_latitude)
point_b_longitude = math.radians(point_b_longitude)

# Calculate great circle distance
distance = RADIUS * (math.acos(math.sin(point_a_latitude) * math.sin(point_b_latitude) +
                               math.cos(point_a_latitude) * math.cos(point_b_latitude) *
                               math.cos((point_a_longitude - point_b_longitude))))


#Calculate great circle distance - alternate formula
'''
distance_latitude = point_b_latitude - point_a_latitude
distance_longitude = point_b_longitude - point_a_longitude

a = math.sin(distance_latitude/2) * math.sin(distance_latitude/2) + \
    math.cos(point_a_latitude) * math.cos(point_b_latitude) * \
    math.sin(distance_longitude/2) * math.sin(distance_longitude/2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
distance = RADIUS * c
'''
print("The great circle distance between the two points is " + str(distance) + " km.")