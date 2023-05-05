from .EnumClass import ThailandProvince,Status
from .User import Dealer,Renter
from .Car import Car
from .Rent import Rent
from .Payment import CashPayment,CreditCardPayment
import datetime

class System:
    def __init__(self):
        self.__car_list = []
        self.__account_list = []
        self.__rent_list = []
        self.__payment_list = []

    def add_rent(self,rent):
        self.__rent_list.append(rent)

    def cancel_rent(self,target_rent):
        for rent in self.__rent_list:
            if target_rent == rent:
                self.__rent_list.remove(rent)
                return
        return
    
    def get_rent_list(self):
        return self.__rent_list

    def add_account(self,user):
        try :
            self.__account_list.append(user)
            return True
        except :
            return False

    def check_account(self,username,password):
        for user in self.__account_list:
            if username == user.get_username():
                if password == user.get_password():
                    return True , user # return as tuple of logic and user instance
        return False , None 

    def add_car(self,car):
        try :
            self.__car_list.append(car)
            return True
        except :
            return False

    def get_account_list(self):
        return self.__account_list

    def search_car(self,location,start_date,end_date):
        return_car_list = []
        for target_car in self.__car_list:
            car_rent_list = []
            for rent in self.__rent_list:
                if rent.get_rent_car() == target_car:
                    if rent.get_rent_status() != Status.Canceled:
                        car_rent_list.append(rent)
            if(location == target_car.get_location() and target_car.check_status(start_date,end_date,car_rent_list)):
                return_car_list.append(target_car)
        return return_car_list
                
    def search_cartype(self,cartype,start_date = datetime.datetime.now().date(),end_date = datetime.datetime.now().date() + datetime.timedelta(days=3),location : ThailandProvince = ThailandProvince.Bangkok):
        return_car_list = []
        for target_car in self.__car_list:
            if(target_car.get_type() != cartype):
                continue
            else:
                car_rent_list = []
                for rent in self.__rent_list:
                    if rent.get_rent_car() == target_car:
                        if rent.get_rent_status() != Status.Canceled:
                            car_rent_list.append(rent)
                if(location == target_car.get_location() and target_car.check_status(start_date,end_date,car_rent_list)):
                    return_car_list.append(target_car)
        return return_car_list
    
    def get_car_list(self):
        return self.__car_list
    
    def del_car(self,target_car_id):
        try :
            print("Try")
            for target_car in self.__car_list:
                if target_car.get_car_ID() == target_car_id:
                    self.__car_list.remove(target_car)
                    return True
        except :
            return False    
    
    def make_rent(self,check_in_date,check_out_date,car,user):
        # try :
            if not isinstance(user,Renter):
                return False
            
            new_rent = Rent(check_in_date,check_out_date,Status.Pending,car,car.get_location())
            self.__rent_list.append(new_rent)
            user.add_to_incomplete_list(rent=new_rent)
            return new_rent
        # except :
            # return False

    def register(self, firstname, lastname, username, password, confirm_password, account_type):
        def check_username(username):
            if len(username) < 8:
                return True 
            return False

        if check_username(username=username): # if username not pass privacy return False
            return False

        def check_password(password, confirm_password):
            def has_number(string):
                return any(char.isdigit() for char in string)

            def has_special_char(string):
                special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
                for char in special_chars:
                    if char in string:
                        return True
                return False
            
            if(password != confirm_password):
                return True # return if password not eqaul to confirm_password
            
            if(len(password) < 8):
                return True # return if length of password is less than 8
            
            if(not has_number(password)):
                return True # return if password not has number
            
            if(not has_special_char(password)):
                return True # return if password not has special_char
            
            return False
        
        if check_password(password=password,confirm_password=confirm_password): # if password not match requirement 
            return False 

        if account_type == 'R':
            new_user = Renter(name= firstname + ' ' + lastname,username=username, password=password)
        elif account_type == 'D':
            new_user = Dealer(name= firstname + ' ' + lastname,username=username, password=password)
        self.add_account(new_user)
        return True

    def login(self, username, password):
        logic , returned_user = self.check_account(username=username,password=password)
        if logic:
            # print('Login success, ' + 'Welcome back! ' + str(type(returned_user)) + ' ' + returned_user.get_name())
            return returned_user
        return False
    
    def modify(self,user,userdict,gender):
        try :
            user.set_name(userdict["name"])
            user.set_profile_image(userdict["profile_image"])
            user.set_gender(gender)
            user.set_birth_date(userdict["birth_date"])
            user.set_info(userdict["info"])
            user.set_username(userdict["username"])
            user.set_password(userdict["password"])
            return True
        except :
            return False

    def get_car(self,target_car_ID):
        for car in self.__car_list:
            if car.get_car_ID() == target_car_ID:
                return car
        return False
    
    def get_user(self,target_user_ID):
        for user in self.__account_list:
            if user.get_id() == target_user_ID:
                return user
        return False
    
    def get_rent(self,rent_id):
        for rent in self.__rent_list:
            if rent.get_rent_no() == rent_id:
                return rent
        return False
    
    def add_payment(self,payment):
        try :
            self.__payment_list.append(payment)
            return True
        except :
            return False
    def get_payment(self,payment_id):
        for payment in self.__payment_list:
            if payment.get_payment_no() == payment_id:
                return payment
        return False
    
    def get_payment_list(self):
        return self.__payment_list
    
    def create_CashPayment(self,card_dictinfo,amount,rent):
        try :
            new_payment = CashPayment(cash_type=card_dictinfo["cash_type"]
                                      ,amount=amount
                                      ,date=card_dictinfo["date"]
                                      ,payment_status=Status.Pending)
            self.add_payment(new_payment) 
            rent.update_payment(new_payment)
            return new_payment
        except :
            return False

    def create_CreditPayment(self,card_dictinfo,amount,rent):
        try:    
            if not isinstance(rent,Rent):
                return False
            new_payment = CreditCardPayment(Credit_Card_type=card_dictinfo["card_type"]
                                            ,card_name=card_dictinfo["card_name"]
                                            ,card_number=card_dictinfo["card_number"]
                                            ,card_CVC=card_dictinfo["card_CVC"]
                                            ,card_exp=card_dictinfo["card_exp"]
                                            ,amount=amount
                                            ,date=card_dictinfo["date"]
                                            ,payment_status=Status.Pending)
            self.add_payment(new_payment) 
            rent.update_payment(new_payment)
            return new_payment
        except :
            return False
        
    def get_username(self,username):
        for user in self.__account_list:
            if user.get_username() == username:
                return user
        return False