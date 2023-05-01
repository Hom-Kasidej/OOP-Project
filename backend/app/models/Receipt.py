class Receipt:
    receipt_number = 1
    def __init__(self, payment):
        self.__receipt_no = Receipt.receipt_number
        self.__payment = payment
        Receipt.receipt_number += 1

    def get_receipt_no(self):
        return self.__receipt_no

    def get_payment(self):
        return self.__payment