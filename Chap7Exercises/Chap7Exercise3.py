class Account:

    def __init__(self, id : str = 0, balance = 100, annual_interest_rate = 0):

        """

        The constructor that accepts values for the fields
       :param id: account identifier
       :param balance: account balance
       :param annual_interest_rate: annual interest rate; entered as a decimal (4.25% is 4.25)
       :return: None

        """
        self.__id = id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate


    def get_id(self):
        return self.__id

    def get_balace(self):
        return self.__balance

    def get_annual_interest_rate(self):
        return self.__annual_interest_rate

    def get_monthly_interest_rate(self, annual_interest_rate):
        monthly_interst_rate = annual_interest_rate * 100/12
        return monthly_interst_rate

    def get_monthly_interest(self):
        change_percent = (self.__previous_closing_price - self.__current_price) / self.__previous_closing_price
        if self.__previous_closing_price > self.__current_price:
            change_percent *= -1
        return change_percent

    def withdraw (self, withdrawal_amount):
        if (withdrawal_amount > self.__balance):
            print ("Withdrawal Amount exceeds balance. Withdrawal not accepted.")
        else:
            self.__balance-=withdrawal_amount
            return(self.__balance)

    def deposit (self, deposit_amount):
        self.__balance += deposit_amount
        return self.__balance



def main():
    my_stock = Stock('INTC', 'Intel Corporation', 20.5, 20.35)
    print('The percent change in stock', my_stock.get_stock_symbol(), 'is', format(my_stock.get_change_percent(),".2f"), '%')

main()
