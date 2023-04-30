import datetime

class Car:

    car_id = 1

    def __init__(self, brand, release_year, seats, doors, gear_type, fuel_type, distance, gps_type, color, features, info, images, price, location, type, dealer_ID):
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
        self.__car_ID = Car.car_id
        self.__dealer_ID = dealer_ID
        self.__review = []
        Car.car_id += 1
    
    def __str__(self):
        return str(self.__car_ID) + " " + str(self.__brand) + " " + str(self.__type)

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

    def get_review(self):
        return self.__review

    def check_status(self,start_date,end_date,rent_list):
        for rent in rent_list:
            check_st = rent.get_check_in_date()
            check_ed = rent.get_check_out_date()
            date_st = datetime.datetime.strptime(check_st, '%Y-%m-%d').date()
            date_ed = datetime.datetime.strptime(check_ed, '%Y-%m-%d').date()
            if type(start_date) == str: 
                date_check_st = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            else:
                date_check_st = start_date 
            if type(end_date) == str:
                date_check_ed = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            else:
                date_check_ed = end_date
            if((date_check_st > date_st and date_check_st < date_ed) or (date_check_ed > date_st and date_check_ed < date_ed)):
                return False
            elif(date_check_st <= date_st and date_check_ed >= date_ed):
                return False
        return True

    def add_carstatus(self,rent):
        self.__carstatus.update_carstatus(rent=rent)