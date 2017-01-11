class HongSaw:

    def __init__(self, low=0, high=0):
        self.__low = low
        self.__high = high

        if self.__high < self.__low:
            self.__high, self.__low = self.__low, self.__high

        self.__create_list()

    def __create_list(self):
        self.__h_list = []
        if self.__high - self.__low != 0:
            a = self.__low
            while a <= self.__high:
                self.__h_list.append(a)
                a += 1
        else:
            self.__h_list.append(self.__low)

    def hong_saw_list_print(self):

        print("\nThis creates a list and performs the Hong Saw check on the list.")

        for i in range (len(self.__h_list)):
            if (self.__h_list[i] % 3 == 0) and (self.__h_list[i] % 5 == 0):
                print("Hong Saw")
            elif (self.__h_list[i] % 3 == 0):
                print("Hong")
            elif(self.__h_list[i] % 5 == 0):
                print("Saw")
            else:
                print(self.__h_list[i])

    def hong_saw_check_and_print(self):
        """
        Checks the remainder when divided by 15, 3, and 5, respectively and prints "Hong Saw", "Hong", "Saw",
        respectively.

        :return: None
        """
        print()
        i = self.__low

        while i <= self.__high:
            if (i % 3 == 0) and (i % 5 == 0):
                print("Hong Saw")
            elif (i % 3 == 0):
                print("Hong")
            elif(i % 5 == 0):
                print("Saw")
            else:
                print(i)
            i += 1


def main():
    """
    Set up program. Get input.
    :return: None
    """

    low, high = eval(input("Enter in two integers, separated by commas: "))
    hong_saw = HongSaw(low,high)
    hong_saw.hong_saw_check_and_print()
    hong_saw.hong_saw_list_print()



main()
