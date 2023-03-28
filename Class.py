from enum import Enum 
from datetime import datetime
class Account:

    def __init__(self):
        self.__accounts = []

    def add_to_account(self,user):
        self.__accounts.append(user)

    def get_accounts(self):
        return self.__accounts

    def check_account(self,username,password): #check if input username,password are match with created acc 
        for user in self.__accounts:
            if username == user.get_username():
                if password == user.get_password():
                    return True , user # return as tuple of logic and user instance
        return False , None 
    
class User:
    def __init__(self, name = None, profile_image = None, gender = None, birth_date = None, info = None, username = None, password = None):
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
        
    def view_car(self):
        pass

    def cancel_payment(self):
        pass

    def cancel_rent(self):
        pass
    
    def login(self, account_pool):
        while True:
            input_username = input('Enter username: ')
            input_password = input('Enter password: ')
            
            logic , returned_user = account_pool.check_account(input_username,input_password)
            if logic:
                print('Login success, ' + 'Welcome back! ' + str(type(returned_user)) + ' ' + returned_user.get_name())
                return returned_user
            print('Login failed')
    def register(self,account_pool):
        def check_empty_string(lst):
            booleans = []
            for str in lst:
                booleans.append(str != '')
            return all(booleans)
        while True:
            input_fname = input('Enter your first name: ') # input first name
            input_lname = input('Enter your last name: ')# input last name
            input_username = input('Enter username: ')
            input_password = input('Enter password: ')
            input_confirm_pass = input('Confirm password: ')
            strs = []
            strs.append(input_fname)
            strs.append(input_lname)
            strs.append(input_username)
            strs.append(input_password)
            strs.append(input_confirm_pass)
            choose = input('as Renter or Dealer? : ') #user choose to be a renter or a dealer

            if check_empty_string(strs):
                if input_password == input_confirm_pass:
                    if choose == 'Renter':
                        new_user = Renter(name= input_fname + ' ' + input_lname,username=input_username, password=input_password)
                    elif choose == 'Dealer':
                        new_user = Dealer(name= input_fname + ' ' + input_lname,username=input_username, password=input_password)
                    account_pool.add_to_account(new_user)
                    print('Register success')
                    break
                print('Password must match')
            else:
                print('PLease fill all requirements')
            


class Dealer(User):
    
    def __init__(self, name = None, profile_image = None, gender = None, birth_date = None, info = None, username = None, password = None, accept_rate = 0, respond_rate = 0, respond_time = 0):
        super().__init__(name, profile_image, gender, birth_date, info, username, password)
        self.__accept_rate = accept_rate
        self.__respond_rate = respond_rate
        self.__respond_time = respond_time
        self.__car_list = []

    def get_accept_rate(self):
        return self.__accept_rate

    def get_respond_rate(self):
        return self.__respond_rate

    def get_respond_time(self):
        return self.__respond_time

    def get_car_list(self):
        return self.__car_list


    def create_car(self):
        pass

    def add_to_carcatalog(self):
        pass

    def modify_car(self):
        pass

    def remove_car(self): #remove Car in Carcatalog
        pass

    def deleted_car(self): #remove Car in self.car_list
        pass


class Renter(User):

    def __init__(self, name = None, profile_image = None, gender = None, birth_date = None, info = None, username = None, password = None):
        super().__init__(name, profile_image, gender, birth_date, info, username, password) 
        self.__success_list = []
        self.__canceled_list = []
        self.__incomplete_list = []

    def get_success_list(self):
        return self.__success_list

    def get_canceled_list(self):
        return self.__canceled_list

    def get_incomplete_list(self):
        return self.__incomplete_list
        
    def add_to_success_list(self):
        pass

    def add_to_canceled_list(self):
        pass

    def add_to_incomplete_list(self):
        pass

    def del_in_success_list(self):
        pass
    
    def del_in_canceled_list(self):
        pass
    
    def del_in_incomplete_list(self):
        pass

    def make_rent(self,rlocation,car,check_in_date,check_out_date):
        pass


class CarType:

    def __init__(self):
        self.__car_catalogs = []

    def get_car_catalogs(self):
        return self.__car_catalogs

    def add_to_car_catalog(self,car_catalog):
        self.__car_catalogs.append(car_catalog)
    
    def search_car(self,location,start_date,end_date):
        return_car_list = []
        for car_catalog in self.__car_catalogs:
            for car in car_catalog.get_car_list():
                if(location == car.get_location() and car.check_status(start_date,end_date)):
                    return_car_list.append(car)
        return return_car_list
                
    def search_cartype(self):
        pass
    

class CarCatalog:

    def __init__(self, name, type_info, type_image):
        self.__name = name
        self.__type_info = type_info
        self.__type_image = type_image
        self.__car_list = []

    def get_name(self):
        return self.__name

    def get_type_info(self):
        return self.__type_info

    def get_type_image(self):
        return self.__type_image

    def get_car_list(self):
        return self.__car_list


    def add_to_carlist(self,car):
        self.__car_list.append(car)

    def collect_car(self,start_date,end_date):
        return_car_list = []
        for car in self.__car_list:
            if(car.check_status(start_date,end_date)):
                return_car_list.append(car)
        return return_car_list

    def find_car(self):
        pass

class Car:

    def __init__(self, brand, release_year, seats, doors, gear_type, fuel_type, distance, gps_type, color, features, info, images, price, location, type, car_ID):
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
        self.__location = location
        self.__type = type
        self.__car_ID = car_ID
        self.__carstatus = []
        self.__review = []

    def get_brand(self):
        return self.__brand

    def get_release_year(self):
        return self.__release_year

    def get_seats(self):
        return self.__seats

    def get_doors(self):
        return self.__doors

    def get_gear_type(self):
        return self.__gear_type

    def get_fuel_type(self):
        return self.__fuel_type

    def get_distance(self):
        return self.__distance

    def get_gps_type(self):
        return self.__gps_type

    def get_color(self):
        return self.__color

    def get_features(self):
        return self.__features

    def get_info(self):
        return self.__info

    def get_images(self):
        return self.__images

    def get_price(self):
        return self.__price
    
    def get_location(self):
        return self.__location
    
    def get_type(self):
        return self.__type
    
    def get_car_ID(self):
        return self.__car_ID

    def get_carstatus(self):
        return self.__carstatus

    def get_review(self):
        return self.__review

    def check_status(self,start_date,end_date):
        for carstatus in self.__carstatus:
            for rent in carstatus.get_rent_list():
                check_st = rent.get_check_in_date()
                check_ed = rent.get_check_out_date()
                date_st = datetime.strptime(check_st, '%d/%m/%Y').date()
                date_ed = datetime.strptime(check_ed, '%d/%m/%Y').date()
                date_check_st = datetime.strptime(start_date, '%d/%m/%Y').date()
                date_check_ed = datetime.strptime(end_date, '%d/%m/%Y').date()
                if((date_check_st > date_st and date_check_st < date_ed) or (date_check_ed > date_st and date_check_ed < date_ed)):
                    return False
                elif(date_check_st <= date_st and date_check_ed >= date_ed):
                    return False
        return True
    
    def add_carstatus(self,carstatus):
        self.__carstatus.append(carstatus)

class Review:
    
    def __init__(self, star, date, info, hour, minute, renter):
        self.__star = star
        self.__date = date
        self.__info = info
        self.__hour = hour
        self.__minute = minute
        self.__renter = renter

    def get_star(self):
        return self.__star

    def get_date(self):
        return self.__date

    def get_info(self):
        return self.__info

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_renter(self):
        return self.__renter

class CarStatus:
    
    def __init__(self):
        self.__rent_list = []

    def get_rent_list(self):
        return self.__rent_list

    def update_carstatus(self,rent):
        self.__rent_list.append(rent)
    
    def check_status(self):
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

    def create_payment(self,amount,date,type):
        pass

    def create_location(self):
        pass

    def create_receipt(self):
        pass

    def update_rent_status(self):
        pass

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

class Location:

    def __init__(self, car_receive, car_return):
        self.__car_receive = car_receive
        self.__car_return = car_return

    def get_car_receive(self):
        return self.__car_receive

    def get_car_return(self):
        return self.__car_return


class Payment:
    
    def __init__(self, amount, date, payment_status, payment_no,rent):
        self._amount = amount
        self._date = date 
        self._payment_status = payment_status
        self._payment_no = payment_no
        self._rent = rent

    def get_amount(self):
        return self._amount

    def get_date(self):
        return self._date

    def get_payment_status(self):
        return self._payment_status

    def get_payment_no(self):
        return self._payment_no

    def get_rent(self):
        return self._rent

    def update_payment_status(self):
        pass


class CashPayment(Payment):

    def __init__(self, cash_type, amount, date, payment_status, payment_no,  rent_Rent, receipt):
        super().__init__(amount, date, payment_status, payment_no,  rent_Rent, receipt)
        self.__cash_type = cash_type

    def get_cash_type(self):
        return self.__cash_type

class CreditCardPayment(Payment):

    def __init__(self, Credit_Card_type, card_name, card_number, card_CVC, card_exp, amount, date, payment_status, payment_no,  rent_Rent, receipt):
        super().__init__(amount, date, payment_status, payment_no,  rent_Rent, receipt)
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


class Gender(Enum):
    Male = 1
    Female = 2
    Others = 3

class Status(Enum):
    Canceled = 1
    Pending = 2
    Success = 3

class ThailandProvince(Enum):
    Amnat_Charoen = "Amnat Charoen"
    Ang_Thong = "Ang Thong"
    Bangkok = "Bangkok"
    Bueng_Kan = "Bueng Kan"
    Buri_Ram = "Buri Ram"
    Chachoengsao = "Chachoengsao"
    Chai_Nat = "Chai Nat"
    Chaiyaphum = "Chaiyaphum"
    Chanthaburi = "Chanthaburi"
    Chiang_Mai = "Chiang Mai"
    Chiang_Rai = "Chiang Rai"
    Chon_Buri = "Chon Buri"
    Chumphon = "Chumphon"
    Kalasin = "Kalasin"
    Kamphaeng_Phet = "Kamphaeng Phet"
    Kanchanaburi = "Kanchanaburi"
    Khon_Kaen = "Khon Kaen"
    Krabi = "Krabi"
    Lampang = "Lampang"
    Lamphun = "Lamphun"
    Loei = "Loei"
    Lopburi = "Lopburi"
    Mae_Hong_Son = "Mae Hong Son"
    Maha_Sarakham = "Maha Sarakham"
    Mukdahan = "Mukdahan"
    Nakhon_Nayok = "Nakhon Nayok"
    Nakhon_Pathom = "Nakhon Pathom"
    Nakhon_Phanom = "Nakhon Phanom"
    Nakhon_Ratchasima = "Nakhon Ratchasima"
    Nakhon_Sawan = "Nakhon Sawan"
    Nakhon_Si_Thammarat = "Nakhon Si Thammarat"
    Nan = "Nan"
    Narathiwat = "Narathiwat"
    Nong_Bua_Lam_Phu = "Nong Bua Lam Phu"
    Nong_Khai = "Nong Khai"
    Nonthaburi = "Nonthaburi"
    Pathum_Thani = "Pathum Thani"
    Pattani = "Pattani"
    Phang_Nga = "Phang Nga"
    Phatthalung = "Phatthalung"
    Phayao = "Phayao"
    Phetchabun = "Phetchabun"
    Phetchaburi = "Phetchaburi"
    Phichit = "Phichit"
    Phitsanulok = "Phitsanulok"
    Phra_Nakhon_Si_Ayutthaya = "Phra Nakhon Si Ayutthaya"
    Phrae = "Phrae"
    Phuket = "Phuket"
    Prachin_Buri = "Prachin Buri"
    Prachuap_Khiri_Khan = "Prachuap Khiri Khan"
    Ranong = "Ranong"
    Ratchaburi = "Ratchaburi"
    Rayong = "Rayong"
    Roi_Et = "Roi Et"
    Sa_Kaeo = "Sa Kaeo"
    Sakon_Nakhon = "Sakon Nakhon"
    Samut_Prakan = "Samut Prakan"
    Samut_Sakhon = "Samut Sakhon"
    Samut_Songkhram = "Samut Songkhram"
    Saraburi = "Saraburi"
    Satun = "Satun"
    Sing_Buri = "Sing Buri"
    Sisaket = "Sisaket"
    Songkhla = "Songkhla"
    Sukhothai = "Sukhothai"
    Suphan_Buri = "Suphan Buri"
    Surat_Thani = "Surat Thani"
    Surin = "Surin"
    Tak = "Tak"
    Trang = "Trang"
    Trat = "Trat"
    Ubon_Ratchathani = "Ubon Ratchathani"
    Udon_Thani = "Udon Thani"
    Uthai_Thani = "Uthai Thani"
    Uttaradit = "Uttaradit"
    Yala = "Yala"
    Yasothon = "Yasothon"