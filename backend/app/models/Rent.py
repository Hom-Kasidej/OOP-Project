from .Receipt import Receipt
from .Payment import Payment

class Rent:
    rent_number = 1
    def __init__(self, check_in_date, check_out_date, rent_status, rent_car, location = None, payment = None, receipt = None):
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__location = location
        self.__rent_car = rent_car
        self.__rent_no = Rent.rent_number
        self.__rent_status = rent_status
        self.__payment = None
        self.__receipt = None
        Rent.rent_number += 1

    def get_check_in_date(self):
        return self.__check_in_date
    
    def get_check_out_date(self):
        return self.__check_out_date
    
    def get_location(self):
        return self.__location
    
    def get_rent_car(self):
        return self.__rent_car
    
    def get_rent_no(self):
        return self.__rent_no
    
    def get_rent_status(self):
        return self.__rent_status
    
    def get_payment(self):
        return self.__payment
    
    def get_receipt(self):
        return self.__receipt
    
    def update_rent_status(self,data):
        self.__rent_status = data

    def create_receipt(self,payment):
        new_receipt = Receipt(payment=payment)
        self.__receipt = new_receipt

    def update_payment(self,payment):
        if isinstance(payment,Payment):
            self.__payment = payment
            return True
        else:
            return False
