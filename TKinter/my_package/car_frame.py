import tkinter as tk
import requests

from enum import Enum

class CarBrand(Enum):
    Aston_martin = "Aston_martin"
    Audi = "Audi"
    BMW = "BMW"
    BYD = "BYD"
    Bentlay = "Bentlay"
    Chevrolet = "Chevrolet"
    Citroen = "Citroen"
    FOMM = "FOMM"
    Fiat = "Fiat"
    Ford = "Ford"
    GWM = "GWM"
    Honda = "Honda"
    Hyundai = "Hyundai"
    Isuzu = "Isuzu"
    Jaguar = "Jaguar"
    Jeep = "Jeep"
    Kia = "Kia"
    LDV = "LDV"
    Lamborgini = "Lamborgini"
    Land_Rover = "Land_Rover"
    Lexus = "Lexus"
    MG = "MG"
    Maserati = "Maserati"
    Mazda = "Mazda"
    Mercedes_Benz = "Mercedes_Benz"
    Mini = "Mini"
    Mitsubishi = "Mitsubishi"
    Nissan = "Nissan"
    Porsche = "Porsche"
    Rolls_Royce = "Rolls_Royce"
    Subaru = "Subaru"
    Suzuki = "Suzuki"
    Tesla = "Tesla"
    Toyota = "Toyota"
    Volvo = "Volvo"
    Other = "Other"


class GearType(Enum):
    Manual = "Manual"
    Auto = "Auto"


class FuelType(Enum):
    Benzien = "Benzien"
    Benzien_91 = "Benzien 91"
    Benzien_95 = "Benzien 95"
    Benzien_E20 = "Benzien E20"
    Benzien_E85 = "Benzien E85"
    CNG = "CNG"
    Diesel = "Diesel"
    Diesel_B10 = "Diesel B10"
    Diesel_B20 = "Diesel B20"
    Diesel_B5 = "Diesel B5"
    Diesel_B7 = "Diesel B7"
    Hybrid = "Hybrid"
    LPG = "LPG"
    NGV = "NGV"
    EV = "EV"
    Plugin_Hybrid = "Plugin Hybrid"


class GPSType(Enum):
    CarTrack = "CarTrack"
    Eyefleet = "Eyefleet"
    NoneGPS = "NoneGPS"
    Others = "Others"
    Otoplug = "Otoplug"


class Gender(Enum):
    Male = "Male"
    Female = "Female"
    Others = "Others"


class Status(Enum):
    Canceled = "Canceled"
    Pending = "Pending"
    Success = "Success"

    
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

class CarType(Enum):
    ANTIQUE = 'Antique'
    CAMPERVAN = 'Campervan'
    CITY = 'City'
    CONVERTIBLE = 'Convertible'
    COUPE = 'Coupe'
    SUV = 'SUV'
    VAN = 'Van'
    SEDAN = 'Sedan'
    OTHER = 'Other'

class CarColor(Enum):
    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"
    GOLD = "Gold"
    WHITE = "White"
    BLACK = "Black"
    GREY = "Grey"
    SILVER = "Silver"
    BROWN = "Brown"
    OTHER = "Other"

class CreditCard(Enum):
    MasterCard = "MasterCard"
    Visa = "Visa"
    JCB = "JCB"

class CashType(Enum):
    Bank = "Bank"
    Cash = "Cash"
    Promptpay = "Promptpay"





class CarFrame:
    def __init__(
        self,
        parent,
        car_brand,
        car_color,
        car_type,
        distance,
        gear_type,
        gps_type,
        fuel_type,
        seats,
        price,
        id
    ):

        self.parent = parent
        self.car_brand = car_brand
        self.car_color = car_color
        self.car_type = car_type
        self.distance = distance
        self.gear_type = gear_type
        self.gps_type = gps_type
        self.fuel_type = fuel_type
        self.seats = seats
        self.price = price
        self.id = id

    def create_widgets(self):

        # Load image and create PhotoImage object
        # with open(image_path, "rb") as f:
        #     image_data = f.read()
        # self.car_image = tk.PhotoImage(data=image_data)
        # self.resize_image = self.car_image.subsample(
        #     self.car_image.width() // 150, self.car_image.height() // 150
        # )

        # Create widgets
        # self.label_car_image = tk.Label(parent, image=self.resize_image)
        self.label_car_brand = tk.Label(self.parent, text=self.car_brand, font=("Arial", 20))
        self.label_car_color = tk.Label(self.parent, text=self.car_color, font=("Arial", 18))
        self.label_car_type = tk.Label(self.parent, text="Car type : " + str(self.car_type))
        self.label_distance = tk.Label(self.parent, text="Distance : " + str(self.distance))
        self.label_gear_type = tk.Label(self.parent, text="Gear type : " + str(self.gear_type))
        self.label_gps_type = tk.Label(self.parent, text="GPS type : " + str(self.gps_type))
        self.label_fuel_type = tk.Label(self.parent, text="Fuel type : " + str(self.fuel_type))
        self.label_seats = tk.Label(self.parent, text="Seats : " + str(self.seats))
        self.price_per_day = tk.Label(self.parent,text=str(self.price) + "THB/day",font=("Arial", 15))

        # Pack widgets
        # self.label_car_image.pack(side=tk.TOP)

    def show(self):
        self.label_car_brand.pack(side=tk.TOP, anchor="w")
        self.label_car_color.pack(side=tk.TOP, anchor="w")
        self.label_car_type.pack(side=tk.TOP, anchor="w")
        self.label_distance.pack(side=tk.TOP, anchor="w")
        self.label_gear_type.pack(side=tk.TOP, anchor="w")
        self.label_gps_type.pack(side=tk.TOP, anchor="w")
        self.label_fuel_type.pack(side=tk.TOP, anchor="w")
        self.label_seats.pack(side=tk.TOP, anchor="w")
        self.price_per_day.pack(side=tk.TOP, anchor="w")

    def hide(self):
        self.label_car_brand.pack_forget()
        self.label_car_type.pack_forget()
        self.label_distance.pack_forget()
        self.label_gear_type.pack_forget()
        self.label_gps_type.pack_forget()
        self.label_fuel_type.pack_forget()
        self.label_seats.pack_forget()
        self.price_per_day.pack_forget()


class RenterCarFrame(CarFrame):

    def __init__(self,
        parent,
        car_brand,
        car_color,
        car_type,
        distance,
        gear_type,
        gps_type,
        fuel_type,
        seats,
        price,
        id,
        select_callback,
        user_status,
        login_callback,
        status = Status.Pending,
    ):
        super().__init__(
        parent,
        car_brand,
        car_color,
        car_type,
        distance,
        gear_type,
        gps_type,
        fuel_type,
        seats,
        price,
        id
        )
        self.select_callback = select_callback
        self.login_callback = login_callback
        self.user_status = user_status
        self.status = status
        self.create_widgets()
        self.create_rent_button()
        self.show()
    

    def login(self):
        self.login_callback()

    def create_rent_button(self):
        if self.user_status:
            self.rent_button = tk.Button(self.parent, text="จองตอนนี้", font=("Arial", 10), bg="light blue",command=self.select_car)
        else:
            self.rent_button = tk.Button(self.parent, text="จองตอนนี้", font=("Arial", 10), bg="light blue",command=self.login)
    def show(self):
        super().show()
        self.rent_button.pack(side=tk.TOP, pady=2)

    def select_car(self):
        api_endpoint = f'http://localhost:8000/View_car/{self.id}'
        response = requests.post(api_endpoint)
        if response.ok:
            data_dict = response.json()
            car = data_dict['Car']
            self.select_callback(car)

class DealerCarFrame(CarFrame):

    def __init__(self,
        parent,
        car_brand,
        car_color,
        car_type,
        distance,
        gear_type,
        gps_type,
        fuel_type,
        seats,
        price,
        id,
        status = Status.Pending
    ):
        super().__init__(
        parent,
        car_brand,
        car_color,
        car_type,
        distance,
        gear_type,
        gps_type,
        fuel_type,
        seats,
        price,
        id
        )
        self.status = status
        self.create_widgets()
        self.create_status_widget()
        self.show()

    def create_status_widget(self):

        #Create widgets and Define status color depending on status 
        if (self.status == Status.Pending):
            self.label_status = tk.Label(self.parent, text="PENDING", font=("Arial", 18))
            self.label_status.configure(fg="grey")
        
        if (self.status == Status.Success):
            self.label_status = tk.Label(self.parent, text="SUCCESSFUL", font=("Arial", 18))
            self.label_status.configure(fg="green")
        
        if (self.status == Status.Canceled):
            self.label_status = tk.Label(self.parent, text="CANCELED", font=("Arial", 18))
            self.label_status.configure(fg="red")

    def show(self):
        super().show()
        self.label_status.pack(side=tk.TOP, pady=5)

