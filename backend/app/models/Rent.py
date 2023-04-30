class Rent:

    def __init__(self, check_in_date, check_out_date, rent_no, rent_status, rent_car, location = None, payment = None, receipt = None):
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__location = location
        self.__rent_car = rent_car
        self.__rent_no = rent_no
        self.__rent_status = rent_status
        self.__payment = payment
        self.__receipt = receipt

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
    
    def update_rent_status(self):
        pass