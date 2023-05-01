from .Car import Car

class User:
    ID = 1

    def __init__(self, name = None, profile_image = None, gender = None, birth_date = None, info = None, username = None, password = None):
        self._name = name
        self._profile_image = profile_image
        self._gender = gender
        self._birth_date = birth_date
        self._info = info
        self._username = username
        self._password = password
        self._id = User.ID
        self._disabled = False
        User.ID += 1

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
    
    def get_id(self):
        return self._id        
    
    def get_disabled(self):
        return self._dis

    def set_name(self,data):
        self._name = data

    def set_profile_image(self,data):
        self._profile_image = data

    def set_gender(self,data):
        self._gender = data

    def set_birth_date(self,data):
        self._birth_date = data

    def set_info(self,data):
        self._info = data

    def set_username(self,data):
        self._username = data

    def set_password(self,data):
        self._password = data

            
class Dealer(User):
    def __init__(self, name, username, password, profile_image = None, gender = None, birth_date = None, info = None, accept_rate : float = 0 , respond_rate : float = 0, respond_time : float = 0):
        super().__init__(name, profile_image, gender, birth_date, info, username, password )
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

    def create_car(self,system, info_dict): #สร้าง instance รถขึ้นมาและมาเก็บไว้ใน car_list ของ Dealer
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
    def __init__(self, name, username, password, profile_image = None, gender = None, birth_date = None, info = None):
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
        
    def add_to_success_list(self,rent):
        self.__success_list.append(rent)

    def add_to_canceled_list(self,rent):
        self.__canceled_list.append(rent)

    def add_to_incomplete_list(self,rent):
        self.__incomplete_list.append(rent)

    def del_in_success_list(self,target_rent):
        for rent in self.__success_list:
            if rent == target_rent:
                self.__success_list.remove(rent)
    
    def del_in_canceled_list(self,target_rent):
        for rent in self.__canceled_list:
            if rent == target_rent:
                self.__canceled_list.remove(rent)
    
    def del_in_incomplete_list(self,target_rent):
        for rent in self.__incomplete_list:
            if rent == target_rent:
                self.__incomplete_list.remove(rent)

class Admin(User):
    def __init__(self, name=None, profile_image=None, gender=None, birth_date=None, info=None, username=None, password=None, ID=None):
        super().__init__(name, profile_image, gender, birth_date, info, username, password, ID)