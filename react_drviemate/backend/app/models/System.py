from ..models.EnumClass import ThailandProvince
from ..models.User import Dealer,Renter
import datetime

class System:
    def __init__(self):
        self.__car_list = []
        self.__account_list = []
        self.__rent_list = []

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
        print(self.__account_list)
        return self.__account_list

    def search_car(self,location,start_date,end_date):
        return_car_list = []
        for target_car in self.__car_list:
            car_rent_list = []
            for rent in self.__rent_list:
                if rent.get_rent_car() == target_car:
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
                        car_rent_list.append(rent)
                if(location == target_car.get_location() and target_car.check_status(start_date,end_date,car_rent_list)):
                    return_car_list.append(target_car)
        return return_car_list
    
    def get_car_list(self):
        return self.__car_list
    
    def del_car(self,target_car_id):
        try:
            for target_car in self.__car_list:
                print(target_car.get_car_ID())
                if target_car.get_car_ID() == target_car_id:
                    self.__car_list.remove(target_car)
                    return True
        except:
            return False    
    
    def make_rent(self,rlocation,car,check_in_date,check_out_date):
        pass
    
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
    
    def modify_car(self, car, cardict, brand, gear_type, fuel_type, gps_type, color, location, type):
        try:
            car.set_brand(brand)
            car.set_release_year(cardict["release_year"])
            car.set_seats(cardict["seats"])
            car.set_doors(cardict["doors"])
            car.set_gear_type(gear_type)
            car.set_fuel_type(fuel_type)
            car.set_distance(cardict["distance"])
            car.set_gps_type(gps_type)
            car.set_color(color)
            car.set_features(cardict["features"])
            car.set_info(cardict["info"])
            car.set_images(cardict["images"])
            car.set_price(cardict["price"])
            car.set_location(location)
            car.set_type(type)
            return True
        except:
            return False