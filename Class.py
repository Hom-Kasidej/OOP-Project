from enum import Enum 
class Account:

    def __init__(self):
        self.__accounts = []

    def add_to_account(self,user):
        self.__accounts.append(user)

    def get_accounts(self):
        return self.__accounts

    def check_account():
        pass

class User:

    def __init__(self, name, profile_image, gender, birth_date, info, username, password):
        self._name = name
        self._profile_image = profile_image
        self._gender = gender
        self._birth_date = birth_date
        self._info = info
        self._username = username
        self._password = password

    def get_name(self):
        return self._name

    def get_profile_image(self):
        return self._profile_image

    def get_gender(self):
        return self._gender

    def get_birth_date(self):
        return self._birth_date

    def get_info(self):
        return self._info

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password
        
    def view_car():
        pass

    def search_car():
        pass

    def search_cartype():
        pass

class Dealer(User):
    
    def __init__(self, name, profile_image, gender, birth_date, info, username, password, accept_rate = 0, respond_rate = 0, respond_time = 0):
        super().__init__(name, profile_image, gender, birth_date, info, username, password)
        self.__accept_rate = accept_rate
        self.__respond_rate = respond_rate
        self.__respond_time = respond_time
        self.__car_list = []


        def create_car():
            pass

        def add_to_carcatalog():
            pass

        def modify_car():
            pass

        def remove_car(self):
            pass

        def deleted_car():
            pass

class Renter(User):

    def __init__(self, name, profile_image, gender, birth_day, info, username, password):
        super().__init__(name, profile_image, gender, birth_day, info, username, password) 
        self.__rent_list = []
        self.__success_list = []
        self.__canceled_list = []
        self.__incomplete_list = []

    def cancel_payment():
        pass

    def cancel_rent():
        pass

    def add_to_success_list():
        pass

    def add_to_canceled_list():
        pass

    def add_to_incomplete_list():
        pass

    def del_in_success_list():
        pass
    
    def del_in_canceled_list():
        pass
    
    def del_in_incomplete_list():
        pass

    def make_rent(self,rlocation,car,check_in_date,check_out_date):
        pass


class CarType:

    def __init__(self):
        self.__car_catalogs = []

        self.add_to_car_catalog("Antique")
        self.add_to_car_catalog("Campervan")
        self.add_to_car_catalog("City")
        self.add_to_car_catalog("Convertible")
        self.add_to_car_catalog("Coupe")
        self.add_to_car_catalog("SUV")
        self.add_to_car_catalog("Van")
        self.add_to_car_catalog("Sedan")
        self.add_to_car_catalog("Utility")
        self.add_to_car_catalog("Other")

    def add_to_car_catalog(self,car_catalog):
        self.__car_catalogs.append(car_catalog)
    
    def search_car():
        pass

    def search_cartype():
        pass
    

class CarCatalog:

    def __init__(self, name, type_info, type_image):
        self.__name = name
        self.__type_info = type_info
        self.__type_image = type_image
        self.__car_list = []

    def add_to_carlist(self,car):
        self.__car_list.append(car)

    def collect_car(self,start_date,end_date):
        return_car_list = []
        for car in self.__car_list:
            if(car.check_status(start_date,end_date)):
                return_car_list.append(car)
        return car

    def search_car():
        pass


class Car:

    def __init__(self, brand, release_year, seats, doors, gear_type, fuel_type, distance, gps_type, color, features, info, images, price, carstatus, review):
        self.__brand = brand 
        self.__release_year = release_year 
        self.__seats = seats 
        self.__doors = doors 
        self.__gear_type = gear_type 
        self.__fuel_type = fuel_type 
        self.__distance = distance 
        self.__gps_type = gps_type 
        self.__color = color 
        self.__features = features 
        self.__info = info 
        self.__images = images 
        self.__price = price 
        self.__carstatus = carstatus
        self.__review = review

    def check_status(self,start_date,end_date):
        for rent in self.__carstatus.get_rent_list():
            if(rent.get_check_in_date() > start_date or rent.get_check_out_date < end_date):
                return False
        return True

class Review:
    
    def __init__(self, star, date, info, hour, minute, renter):
        self.__star = star
        self.__date = date
        self.__info = info
        self.__hour = hour
        self.__minute = minute
        self.__renter = renter

class CarStatus:
    
    def __init__(self):
        self.__rent_list = []

    def get_rent_list(self):
        return self.__rent_list

    def update_carstatus(self,rent):
        pass
    
    def check_status():
        pass

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

    def create_payment(self,amount,date,type):
        pass

    def create_receipt():
        pass

    def update_rent_status():
        pass



class Receipt:
    
    def __init__(self, receipt_no, rent, payment):
        self.__receipt_no = receipt_no
        self.__rent = rent
        self.__payment = payment

class Location:

    def __init__(self, car_receive, car_return):
        self.__car_receive = car_receive
        self.__car_return = car_return

class Payment:
    
    def __init__(self, amount, date, payment_status, payment_no,rent):
        self._amount = amount
        self._date = date 
        self._payment_status = payment_status
        self._payment_no = payment_no
        self._rent = rent

    def update_payment_status():
        pass


class CashPayment(Payment):

    def __init__(self, cash_type, amount, date, payment_status, payment_no,  rent_Rent, receipt):
        super().__init__(amount, date, payment_status, payment_no,  rent_Rent, receipt)
        self.__cash_type = cash_type

class CreditCardPayment(Payment):

    def __init__(self, Credit_Card_type, card_name, card_number, card_CVC, card_exp, amount, date, payment_status, payment_no,  rent_Rent, receipt):
        super().__init__(amount, date, payment_status, payment_no,  rent_Rent, receipt)
        self.__creditcard_type = Credit_Card_type
        self.__card_name = card_name
        self.__card_number = card_number
        self.__card_CVC = card_CVC
        self.__card_exp = card_exp

class CarBrand(Enum):
    Aston_martin = 1
    Audi = 2
    BMW = 3
    BYD = 4
    Bentlay = 5
    Chevrolet = 6
    Citroen = 7
    FOMM = 8
    Fiat = 9
    Ford = 10
    GWM = 11
    Honda = 12
    Hyundai = 13
    Isuzu = 14
    Jaguar = 15
    Jeep = 16
    Kia = 17
    LDV = 18
    Lamborgini = 19
    Land_Rover = 20
    Lexus = 21
    MG = 22
    Maserati = 23
    Mazda = 24
    Mercedes_Benz = 25
    Mini = 26
    Mitsubishi = 27
    Nissan = 28
    Porsche = 29
    Rolls_Royce = 30
    Subaru = 31
    Suzuki = 32
    Tesla = 33
    Toyota = 34
    Volvo = 35
    Other = 36
class GearType(Enum):
    Manual = 1
    Auto = 2

class FuelType(Enum):
    Benzien = 1
    Benzien_91 = 2
    Benzien_95 = 3
    Benzien_E20 = 4
    Benzien_E85 = 5
    CNG = 6
    Diesel = 7
    Diesel_B10 = 8
    Diesel_B20 = 9
    Diesel_B5 = 10
    Diesel_B7 = 11
    Hybrid = 12
    LPG = 13
    NGV = 14
    EV = 15
    Plugin_Hybird = 16

class GPSType(Enum):
    CarTrack = 1
    Eyefleet = 2
    NoneGPS = 3
    Others = 4
    Otoplug = 5