class Location:
    """
       Location class finds the largest element in a 2-D list and returns its value and its index
       A 2-D matrix is required in order for this to function properly
    """
    def __init__(self, matrix):
        """
            Constructor for Location class. Calls the locate largest method and then calls calls the __str__() function
            (overriding the Python Object __str__() function) which prints out the largest element and its location in
            a string format
        :param matrix: 2-dimensional list of float values
        :return: None
        """
        self.row = None
        self.column = None
        self.max_value = None
        self.__matrix = matrix
        self.__location_index = []
        self.__temp_max = None

        self.locate_largest()
        self.__str__()

    def get_max_location_index_list(self):
        """
        Accessor method to return the location of the largest element in a 2D list
        :return: 2-element list which is the index of the largest element in the 2D list
        """
        self.__location_index.append(self.row)
        self.__location_index.append(self.column)
        return self.__location_matrix

    def get_max_value(self):
        """
        Accessor method to get the max value in the 2D list
        :return: float
        """
        return self.max_value

    def locate_largest(self):
        """
        Locates the largest element in the 2D list and identifies its index
        :return: None
        """
        for i in self.__matrix:
            self.__temp_max = max(i)
            self.__temp_column_location = i.index(self.__temp_max)
            if self.max_value is None or self.max_value < self.__temp_max:
                self.max_value = self.__temp_max
                self.column = self.__temp_column_location
                self.row = self.__matrix.index(i)

    def __str__(self):
        """
        Overrides the Python base Object class's __str__() function to print out the highest element and its index in
        a 2D list
        :return: str containing the largest element and its index
        """
        return print("The largest element is " + str(self.max_value) + " located at (" + str(self.row)
                     + "," + str(self.column) + ")")