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