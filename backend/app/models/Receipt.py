class Receipt:
    
    def __init__(self, receipt_no, rent, payment):
        self.__receipt_no = receipt_no
        self.__rent = rent
        self.__payment = payment

    def get_receipt_no(self):
        return self.__receipt_no

    def get_rent(self):
        return self.__rent

    def get_payment(self):
        return self.__payment