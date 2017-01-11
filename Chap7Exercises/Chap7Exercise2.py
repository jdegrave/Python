
class Stock:

    def __init__(self, symbol: str, name: str, previous_closing_price: float, current_price: float):
        """
        The constructor that accepts values for the fields
       :param symbol: stock symbol (4 characters max)
       :param name: Name of the stock (this is the company name that issues it)
       :param previous_closing_price: yesterdays' closing price of the stock
       :param current_price: current price of the stock
       :return: None
        """

        self.__symbol = symbol
        self.__name = name
        self.__previous_closing_price = previous_closing_price
        self.__current_price = current_price

    def get_stock_name(self):
        return self.__name

    def get_stock_symbol(self):
        return self.__symbol

    def get_stock_previous_closing_price(self):
        return self.__previous_closing_price

    def get_current_price(self):
        return self.__current_price

    def get_change_percent(self):
        change_percent = (self.__current_price - self.__previous_closing_price) / self.__previous_closing_price
        return change_percent

    def set_stock_previous_closing_price(self, previous_closing_price : float):
        self.__previous_closing_price = previous_closing_price

    def set_current_price(self, current_price):
        self.__current_price = current_price


def main():
    my_stock = Stock('INTC', 'Intel Corporation', 75, 100)
    print('The percent change in stock', my_stock.get_stock_symbol(), 'is', format(my_stock.get_change_percent(),".2f"),
          '%')

main()
