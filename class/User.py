from .Car import Car

class User:
    def __init__(self, name = None, profile_image = None, gender = None, birth_date = None, info = None, username = None, password = None, ID = None):
        self._name = name
        self._profile_image = profile_image
        self._gender = gender
        self._birth_date = birth_date
        self._info = info
        self._username = username
        self._password = password
        self._ID = ID

    def get_name(self):
        return self._name
    
    def set_name(self,data):
        self._name = data

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
    
            
class Dealer(User):
    
    def __init__(self, name, username, password, profile_image = None, gender = None, birth_date = None, info = None, user_ID = None, accept_rate : float = 0 , respond_rate : float = 0, respond_time : float = 0):
        super().__init__(name, profile_image, gender, birth_date, info, username, password, user_ID)
        self.__accept_rate = accept_rate
        self.__respond_rate = respond_rate
        self.__respond_time = respond_time

    def get_accept_rate(self):
        return self.__accept_rate

    def get_respond_rate(self):
        return self.__respond_rate

    def get_respond_time(self):
        return self.__respond_time

    def get_car_list(self):
        return self.__car_list

    def create_car(self,system,info_dict): #สร้าง instance รถขึ้นมาและมาเก็บไว้ใน car_list ของ Dealer
        try : 
            system.add_car(Car(**info_dict))
            return True
        except :
            return False

    def modify_car(self):
        pass

    def delete_car(self,system, target_car): #remove Car in self.car_list
        try : 
            if target_car in system.get_car_lisst():
                system.del_car(target_car)
                return True
        except :
            return False         

class Renter(User):

    def __init__(self, name, username, password, profile_image = None, gender = None, birth_date = None, info = None, user_ID = None):
        super().__init__(name, profile_image, gender, birth_date, info, username, password, user_ID) 
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

class Admin(User):
    def __init__(self, name=None, profile_image=None, gender=None, birth_date=None, info=None, username=None, password=None, ID=None):
        super().__init__(name, profile_image, gender, birth_date, info, username, password, ID)