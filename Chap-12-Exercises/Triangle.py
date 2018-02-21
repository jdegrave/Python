"""
    Chapter 12, Exercise 1:  Extending the Geometric Object Class
    Author:  Jodi A. De Grave
    Date: 4/18/2016

"""
from GeometricObject import GeometricObject

import math


class Triangle (GeometricObject):
    """
        Derived/subclass/child class of GeometricObject. Extends the Geometric Object to create a triangle object.
    """
    def __init__(self, color, filled, side1=1, side2=1, side3=1):
        """
        Constructor for initializing the Triangle class
        :param color: string inherited from superclass Geometric Object
        :param filled: boolean inherited from superclass Geometric Object
        :param side1: float representing 1st side of the triangle
        :param side2: float representing 2nd side of the triangle
        :param side3: float representing 3rd side of the triangle
        :return: None
        """
        # call Geometric object's constructor to input color and filled state
        super().__init__(color, filled)
        self.__side1 = float(side1)
        self.__side2 = float(side2)
        self.__side3 = float(side3)

    def get_side1(self):
        """
        Accessor method for getting length of side 1 of triangle object
        :return: float self.__side1
        """
        return self.__side1

    def get_side2(self):
        """
        Accessor method for getting length of side 2 of triangle object
        :return: float self.__side2
        """

        return self.__side2

    def get_side3(self):
        """
        Accessor method for getting length of side 3 of triangle object
        :return: float self.__side3
        """
        return self.__side3

    def get_all_sides(self):
        """
        Accessor method for returning all 3 sides of the triangle at once and puts them into a 1-D list
        :return: sides_list, a 3-element 1D list
        """
        self.__sides_list = []
        self.__sides_list = self.__sides_list.append(self.__side1)
        self.__sides_list = self.__sides_list.append(self.__side2)
        sides_list = self.__sides_list.append(self.__side3)

        return sides_list

    def set_side1(self, side1):
        """
        Mutator method to set the length of side 1 of the triangle
        :param side1: float
        :return: None
        """
        self.__side1 = side1

    def set_side1(self, side2):
        """
        Mutator method to set the length of side 2 of the triangle
        :param side2: float
        :return: None
        """
        self.__side2 = side2

    def set_side3(self, side3):
        """
         Mutator method to set the length of side 3 of the triangle
        :param side3: float
        :return: None
        """
        self.__side3 = side3

    def get_area(self):
        """
        Heron's formula for calculating the area of a triangle
        Calls get_perimeter as the basis of the calculation
        :return: float triangle_area
        """

        s = self.get_perimeter()/2
        triangle_area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) *
                                        (s - self.__side3))
        return triangle_area

    def get_perimeter(self):
        """
        Calculate the perimeter of the triangle.
        :return:
        """
        return (self.__side1 + self.__side2 + self.__side3)

    def print_triangle(self):
        """
        Overrides the base class __str__() method (i.e. overrides Geometric Object's __str__() method)

        :return: string describing the triangle object: color, filled state, length of each side
        """
        print() # formatting purposes
        print(super().__str__() + " Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2)
                                   + " side3 = " + str(self.__side3))



