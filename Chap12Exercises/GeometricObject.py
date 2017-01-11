"""
    Chapter 12, Exercise 1:  Extending the Geometric Object Class
    Author:  Jodi A. De Grave
    Date: 4/18/2016

"""


class GeometricObject:
    """
        GeometricObject is the base class/superclass/parent class. Triangle class is the derived class/subclass/child
        class that extends the GeometricObject class.
    """
    def __init__(self, color="green", filled=True):
        """
            Constructor. Initializes basic attributes that are common to all subclasses.

        :param color: string green is the default color of the geometric object (inherited by subclasses)
        :param filled: boolean indicating if the geometric object is filled - True is the default
        :return: None
        """
        self.__color = color
        self.__filled = filled

    def get_color(self):
        """
            Accessor method for color of geometric object
        :return: self.__color - a string
        """
        return self.__color

    def set_color(self, color):
        """
            Mutator method for setting color for geometric object
        :param color:
        :return: None
        """
        self.__color = color

    def is_filled(self):
        """
            Accessor method for returning filled/nonfilled state of geometric object

        :return: self.__filled boolean ("True" = filled, "False" = unfilled
        """
        return self.__filled

    def set_filled(self, filled):
        """
            Mutator method to set the filled/unfilled state of the geometric object
        :param filled: boolean True = filled, False = unfilled
        :return: None
        """
        self.__filled = filled

    def __str__(self):
            """
                Description of the geometric object. Technically, this overrides Python's "object" class  __str__()
                method.
            :return: string describing the color and filled state (uses self.__color and self.__filled)
            """
            return "color: " + self.__color + " and filled: " + str(self.__filled)
