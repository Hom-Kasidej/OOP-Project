class Account:

    def __init__(self):
        self.accounts = []

    def add_to_account():
        pass

    def check_account():
        pass



class User:

    def __init__(self, name, profile_image, gender, birth_date, info, username, password):
        self.name = name
        self.profile_image = profile_image
        self.gender = gender
        self.birth_date = birth_date
        self.info = info
        self.username = username
        self.password = password

    def view_car():
        pass

    def search_car():
        pass

    def search_cartype():
        pass

class Dealer(User):
    
    def __init__(self, name, profile_image, gender, birth_date, info, username, password, accept_rate, respond_rate, respond_time):
        super().__init__(name, profile_image, gender, birth_date, info, username, password)
        self.accept_rate = accept_rate
        self.respond_rate = respond_rate
        self.respond_time = respond_time
        self.car_list = []

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
        self.rent_list = []
        self.success_list = []
        self.canceled_list = []
        self.incomplete_list = []

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
        self.car_catalogs = []

    def add_to_cartype(self,car_catalog):
        pass
    
    def search_car():
        pass

    def search_cartype():
        pass

class CarCatalog:

    def __init__(self, name, type_info, type_image):
        self.name = name
        self.type_info = type_info
        self.type_image = type_image
        self.car_list = []

    def add_to_carlist():
        pass

    def collect_car(self):
        pass

    def search_car():
        pass


class Car:

    def __init__(self, brand, gen, release_year, seats, doors, gear_type, fuel_type, distance, gps_type, color, features, info, images, price, carstatus, review):
        self.brand = brand 
        self.gen = gen 
        self.release_year = release_year 
        self.seats = seats 
        self.doors = doors 
        self.gear_type = gear_type 
        self.fuel_type = fuel_type 
        self.distance = distance 
        self.gps_type = gps_type 
        self.color = color 
        self.features = features 
        self.info = info 
        self.images = images 
        self.price = price 
        self.carstatus = carstatus
        self.review = review

class Review:
    
    def __init__(self, star, date, info, hour, minute, renter):
        self.star = star
        self.date = date
        self.info = info
        self.hour = hour
        self.minute = minute
        self.renter = renter

class CarStatus:
    
    def __init__(self):
        self.rent_list = []

    def update_carstatus(self,rent):
        pass

class Rent:

    def __init__(self, check_in_date, check_out_date, rent_no, rent_status, rent_car, location = None, payment = None, receipt = None):
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.location = location
        self.rent_car = rent_car
        self.rent_no = rent_no
        self.rent_status = rent_status
        self.payment = payment
        self.receipt = receipt

    def create_payment(self,amount,date,type):
        pass

    def create_receipt():
        pass

    def update_rent_status():
        pass



class Receipt:
    
    def __init__(self, receipt_no, rent, payment):
        self.receipt_no = receipt_no
        self.rent = rent
        self.payment = payment

class Location:

    def __init__(self, car_receive, car_return):
        self.car_receive = car_receive
        self.car_return = car_return

class Payment:
    
    def __init__(self, amount, date, payment_status, payment_no,rent):
        self.amount = amount
        self.date = date 
        self.payment_status = payment_status
        self.payment_no =payment_no
        self.rent = rent

    def update_payment_status():
        pass


class CashPayment(Payment):

    def __init__(self, cash_type, amount, date, payment_status, payment_no,  rent_Rent, receipt):
        super().__init__(amount, date, payment_status, payment_no,  rent_Rent, receipt)
        self.cash_type = cash_type

class CreditCardPayment(Payment):

    def __init__(self, Credit_Card_type, card_name, card_number, card_CVC, card_exp, amount, date, payment_status, payment_no,  rent_Rent, receipt):
        super().__init__(amount, date, payment_status, payment_no,  rent_Rent, receipt)
        self.Credit_Card_type = Credit_Card_type
        self.card_name = card_name
        self.card_number = card_number
        self.card_CVC = card_CVC
        self.card_exp = card_exp