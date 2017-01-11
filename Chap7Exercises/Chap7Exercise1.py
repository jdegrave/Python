"""
    Chapter 7 Exercise 1
    Author:  Jodi A DeGrave
    Date: 3/26/2016
"""

class Rectangle:

# Construct a rectangle object
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return  2 * self.width + 2 * self.height

    def get_area(self):
        return self.width * self.height

    def set_width_and_height (self, width, height):
        self.width = width
        self.height = height


def print_rectangle_info(rectangle_object):
    print('Width: ', format(rectangle_object.width,'5.2f'), end='\t')
    print('Height: ', format(rectangle_object.height, '5.2f'), end='\t')
    print(format('Perimeter: ', '>12s'), format(rectangle_object.get_perimeter(), '5.2f'), end='\t')
    print(format('Area: ', '>7s'), format(rectangle_object.get_area(),'5.2f'))


def main():
    rect1 = Rectangle(4, 40)
    rect2 = Rectangle(3.5, 35.7)

    rectangle_group = [rect1, rect2]

    for i in range (0, len(rectangle_group)):
        print('Rectangle', i + 1, ':', end='\t')
        print_rectangle_info(rectangle_group[i])

main()

