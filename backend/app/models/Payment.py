class Payment:
    payment_no = 1
    def __init__(self, amount, date, payment_status):
        self._amount = amount
        self._date = date 
        self._payment_status = payment_status
        self._payment_no = Payment.payment_no
        Payment.payment_no += 1

    def get_amount(self):
        return self._amount

    def get_date(self):
        return self._date

    def get_payment_status(self):
        return self._payment_status

    def get_payment_no(self):
        return self._payment_no


    def update_payment_status(self,data):
        self._payment_status = data

class CashPayment(Payment):

    def __init__(self, cash_type, amount, date, payment_status):
        super().__init__(amount, date, payment_status)
        self.__cash_type = cash_type

    def get_cash_type(self):
        return self.__cash_type

class CreditCardPayment(Payment):

    def __init__(self, Credit_Card_type, card_name, card_number, card_CVC, card_exp, amount, date, payment_status):
        super().__init__(amount, date, payment_status)
        self.__creditcard_type = Credit_Card_type
        self.__card_name = card_name
        self.__card_number = card_number
        self.__card_CVC = card_CVC
        self.__card_exp = card_exp 
        

    def get_creditcard_type(self):
        return self.__creditcard_type

    def get_card_name(self):
        return self.__card_name

    def get_card_number(self):
        return self.__card_number

    def get_card_CVC(self):
        return self.__card_CVC

    def get_card_exp(self):
        return self.__card_exp