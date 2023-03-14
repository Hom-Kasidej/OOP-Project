class Account:

    def __init__(self):
        self.accounts = []

class User:

    def __init__(self, name, profile_image, gender, birth_date, info):
        self.name = name
        self.profile_image = profile_image
        self.gender = gender
        self.birth_date = birth_date
        self.info = info

class Dealer(User):
    
    def __init__(self, name, profile_image, gender, birth_date, info, accept_rate, respond_rate, respond_time):
        super().__init__(name, profile_image, gender, birth_date, info)
        self.accept_rate = accept_rate
        self.respond_rate = respond_rate
        self.respond_time = respond_time
        self.car_list = []

class Renter(User):

    def __init__(self, name, profile_image, gender, birth_day, info):
        super().__init__(name, profile_image, gender, birth_day, info) 
        self.rent_list = []

class CarCatalog:

    def __init__(self, name, type_info, type_image):
        self.name = name
        self.type_info = type_info
        self.type_image = type_image

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

class Rent:

    def __init__(self, check_in_date, check_out_date, rent_no, rent_status, rent_car, location, payment, receipt):
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.location = location
        self.rent_car = rent_car
        self.rent_no = rent_no
        self.rent_status = rent_status
        self.payment = payment
        self.receipt = receipt

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