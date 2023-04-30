from ..config.EnumClass import ThailandProvince
from .User import *
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
        try :
            for target_car in self.__car_list():
                if target_car.get_car_ID() == target_car_id:
                    self.__car_list.remove(target_car)
                    return True
            return False
        except :
            return False     

    def make_rent(self,rlocation,car,check_in_date,check_out_date):
        pass

    def login(self, username, password):
        logic , returned_user = self.check_account(username=username,password=password)
        if logic:
            print('Login success, ' + 'Welcome back! ' + str(type(returned_user)) + ' ' + returned_user.get_name())
            return returned_user
        print('Login failed')
    
    def register(self):
        Bfname = True
        Blname = True
        Busername = True
        Bpassword = True
        Bconfirmpass = True
        IsCancel = True
        while Bfname or Blname or Busername or Bpassword or Bconfirmpass or IsCancel:
            if(Bfname):
                input_fname = input('Enter your first name: ') # input first name
                if(input_fname != ""):
                    Bfname = False
                
            if(Blname):
                input_lname = input('Enter your last name: ')# input last name
                if(input_lname != ""):
                    Blname = False

            if(Busername):
                input_username = input('Enter username: ')
                if(input_username != ""):
                    Busername = False
                
            if(Bpassword):
                input_password = input('Enter password: ')
                if(input_password != ""):
                    Bpassword = False

            if(Bconfirmpass):
                input_confirm_pass = input('Confirm password: ')
                if input_password == input_confirm_pass:
                    if(input_confirm_pass != ""):
                        Bconfirmpass = False

            choose = input('type R for Renter or D for Dealer? : ') #user choose to be a renter or a dealer

            if(Bfname or Blname or Busername or Bpassword or Bconfirmpass):
                print('PLease fill all requirements')

        if choose == 'R':
            new_user = Renter(name= input_fname + ' ' + input_lname,username=input_username, password=input_password)
        elif choose == 'D':
            new_user = Dealer(name= input_fname + ' ' + input_lname,username=input_username, password=input_password)
        self.add_account(new_user)
        print('Register success')