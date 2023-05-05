from .EnumClass import CarBrand, GearType, FuelType, GPSType,ThailandProvince,CarType,CarColor,Gender
from .Car import Car
from .User import Dealer,Renter
from passlib.context import CryptContext

car_info_dict = {
    "Car1" : {
        "brand" : CarBrand.Nissan ,
        "release_year" : 2005,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : GearType.Auto,
        "fuel_type" : FuelType.Benzien,
        "distance" : 5049,
        "gps_type" : GPSType.NoneGPS,
        "color" : CarColor.BLACK,
        "features" : "Automatic_seat",
        "info" : "",
        "price" : 3000,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.CITY,
        "dealer_ID" : 1
    },
    "Car2" : {
        "brand" : CarBrand.Honda,
        "release_year" : 2010,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : GearType.Auto,
        "fuel_type" : FuelType.Benzien,
        "distance" : 12654,
        "gps_type" : GPSType.NoneGPS,
        "color" : CarColor.BLACK,
        "features" : "",
        "info" : "",
        "price" : 3500,
        "location" : ThailandProvince.Chiang_Mai,
        "type" : CarType.CITY,
        "dealer_ID" : 1
    },
    "Car3" : {
        "brand" : CarBrand.BMW,
        "release_year" : 2009,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : GearType.Auto,
        "fuel_type" : FuelType.Benzien,
        "distance" : 9801,
        "gps_type" : GPSType.CarTrack,
        "color" : CarColor.BLACK,
        "features" : "Bluetooth_Music",
        "info" : "",
        "price" : 4000,
        "location" : ThailandProvince.Chiang_Rai,
        "type" : CarType.CONVERTIBLE,
        "dealer_ID" : 1
    },
    "Car4" : {
        "brand" : CarBrand.Toyota,
        "release_year" : 2020,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : GearType.Auto,
        "fuel_type" : FuelType.EV,
        "distance" : "1500",
        "gps_type" : GPSType.Otoplug,
        "color" : CarColor.BLACK,
        "features" : "",
        "info" : "",
        "price" : 2500,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.SUV,
        "dealer_ID" : 1
    },
    "Car5" : {
        "brand" : CarBrand.Chevrolet,
        "release_year" : 2006,
        "seats" : 4,
        "doors" : 4, 
        "gear_type" : GearType.Auto,
        "fuel_type" : FuelType.Benzien,
        "distance" : 15602,
        "gps_type" : GPSType.NoneGPS,
        "color" : CarColor.BLACK,
        "features" : "",
        "info" : "",
        "price" : 3999,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.SUV,
        "dealer_ID" : 2
    },
    "Car6" : {
        "brand" : CarBrand.Ford,
        "release_year" : 2004,
        "seats" : 7,
        "doors" : 4,
        "gear_type" : GearType.Manual,
        "fuel_type" : FuelType.Diesel,
        "distance" : 25040,
        "gps_type" : GPSType.NoneGPS,
        "color" : CarColor.BLACK,
        "features" : "",
        "info" : "",
        "price" : 3000,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.SUV,
        "dealer_ID" : 2
    },
    "Car7" : {
        "brand" : CarBrand.Honda,
        "release_year" : 2011,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : GearType.Auto,
        "fuel_type" : FuelType.Benzien,
        "distance" : 9800,
        "gps_type" : GPSType.Others, 
        "color" : CarColor.BLACK,
        "features" : "",
        "info" : "",
        "price" : 1900,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.CITY,
        "dealer_ID" : 2
    },
    "Car8" : {
        "brand" : CarBrand.Honda, 
        "release_year" : 2012,
        "seats" : 10,
        "doors" : 4,
        "gear_type" : GearType.Auto,
        "fuel_type" : FuelType.Benzien,
        "distance" : 16094,
        "gps_type" : GPSType.NoneGPS,
        "color" : CarColor.BLACK,
        "features" : "LED SCREEN",
        "info" : "",
        "price" : 4599,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.CITY,
        "dealer_ID" : 3
    },
    "Car9" : {
        "brand" : CarBrand.Honda, 
        "release_year" : 2005,
        "seats" : 4,
        "doors" : 2,
        "gear_type" : GearType.Manual,
        "fuel_type" : FuelType.Diesel,
        "distance" : 30071,
        "gps_type" : GPSType.Others,
        "color" : CarColor.BLACK,
        "features" : "",
        "info" : "",
        "price" : 2990,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.CITY,
        "dealer_ID" : 3
    },
    "Car10" : {
        "brand" : CarBrand.Lamborgini,
        "release_year" : 2015,
        "seats" : 2,
        "doors" : 2,
        "gear_type" : GearType.Manual,
        "fuel_type" : FuelType.Benzien,
        "distance" : 3540,
        "gps_type" : GPSType.NoneGPS,
        "color" : CarColor.BLACK,
        "features" : "",
        "info" : "",
        "price" : 15000,
        "location" : ThailandProvince.Nan,
        "type" : CarType.CONVERTIBLE,
        "dealer_ID" : 3
    },
    "Car11" : {
        "brand" : CarBrand.Toyota, 
        "release_year" : 2018,
        "seats" : 7,
        "doors" : 4,
        "gear_type" : GearType.Auto,
        "fuel_type" : FuelType.Benzien,
        "distance" : 14200,
        "gps_type" : GPSType.Others,
        "color" : CarColor.BLACK,
        "features" : "",
        "info" : "",
        "price" : 2600,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.SUV,
        "dealer_ID" : 4
    },
    
    "Car12" : {
        "brand" : CarBrand.Nissan,
        "release_year" : 2009,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : GearType.Auto,
        "fuel_type" : FuelType.Benzien,
        "distance" : 18005,
        "gps_type" : GPSType.Eyefleet,
        "color" : CarColor.BLACK,
        "features" : "",
        "info" : "",
        "price" : 2099,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.CITY,
        "dealer_ID" : 4
    }
}

Car_instance_list = []
for i in car_info_dict:
    Car_instance_list.append(Car(**car_info_dict[i]))

dealer_info_dict = {
    'Dealer1' : {
        'name' : 'Johnny Peepo',
        'profile_image': 'None',
        'gender' : Gender.Male,
        'birth_date' : '01/01/2001',
        'info' : 'i love cars',
        'username' : 'd',
        'password' : 'd'
    },
    'Dealer2' : {
        'name' : 'Somchai Hi',
        'profile_image': 'None',
        'gender' : Gender.Male,
        'birth_date' : '11/12/1974',
        'info' : 'Hi',
        'username' : 'somchai911',
        'password' : '$2b$12$bUl3StqydVqSy6YEpuXRsOGtXOu9xzp53PnYtCNS1vp7lKisLH6Z6'
    },
    'Dealer3' : {
        'name' : 'Naruto Sasuke',
        'profile_image': 'None',
        'gender' : Gender.Male,
        'birth_date' : '11/12/1950',
        'info' : 'Hi hello',
        'username' : '1qgqgqwg',
        'password' : '$2b$12$c172wlneb/Eeoh9OUizkx./Nb5b7K5uxBLxqmp2gLIJ/N81roxxoS'
    },
    'Dealer4' : {
        'name' : 'Somsri Haha',
        'profile_image': 'None',
        'gender' : Gender.Female,
        'birth_date' : '20/12/1999',
        'info' : 'Hi wassup',
        'username' : 'waegweg134',
        'password' : '$2b$12$4JIjPOvzhTa6eVJUl9zpy.fbby6RHuAIsBNcBYWgAtGO1qVIUfeNO'
    }
}

dealer_instance_list = []

for dealer in dealer_info_dict:
    dealer_instance_list.append(Dealer(**dealer_info_dict[dealer]))


renter_info_dict = {
    "Renter1" : {
        "name" : "Sompong Payongdej",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "28/02/1987",
        "info" : "Good guy",
        "username" : "r",
        "password" : "r"
    },
    "Renter2" : {
        "name" : "Somsej Eatgrass",
        "profile_image" : "",
        "gender" : Gender.Female,
        "birth_date" : "01/01/1999",
        "info" : "Capybaraaa",
        "username" : "GrossGrass",
        "password" : "$2b$12$1Sh7SzzO.yvbP2h9o2wyRelIUKNOASyHuP9qwnY8IgJBMi52kmlzq"
    },
    "Renter" : {
        "name" : "Somjett DashForward",
        "profile_image" : "",
        "gender" : Gender.Female,
        "birth_date" : "09/02/2000",
        "info" : "Get out of my way!",
        "username" : "Jett",
        "password" : "$2b$12$KBOJD0c/M2ycufJcUvILjua9a83YN6a/glnDTedpIandezi2qoI8."
    },
     "Renter4" : {
        "name" : "Gekko keeact",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "21/07/2002",
        "info" : "Let's go my buddy",
        "username" : "Anonymous",
        "password" : "$2b$12$FIYYawWoIu7gpdgZAhjPSuPJL8zTFu7i4.ytmj/8.NlF50aDQTEWO"
    },
    "Renter5" : {
        "name" : "MrBeast Latkrabang",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "11/11/1970",
        "info" : "Who want my money!!",
        "username" : "Beast",
        "password" : "$2b$12$7yQOeQgGX2/H8ks6uRPoWuOGVi9ezMi4l8cEImIHnwEvjKlSzKxQa"
    },
    "Renter6" : {
        "name" : "RestWith OOP",
        "profile_image" : "",
        "gender" : Gender.Female,
        "birth_date" : "19/03/2003",
        "info" : "OOP Project is waiting for you",
        "username" : "OOPInwZa",
        "password" : "$2b$12$pSQc5sV4VkrLDBuN09YfmeLCNQTKXgviIyZfaU7nvl3cf5nU0uGtC"
    },
    "Renter7" : {
        "name" : "Somying butchai",
        "profile_image" : "",
        "gender" : Gender.Female,
        "birth_date" : "20/09/1997",
        "info" : "I want cheap price",
        "username" : "Somying",
        "password" : "$2b$12$KSVK1p51Gz603RxpU.Dpn.h8UgJE00dwxfZsMzIkWFgoYO93zp3Ei"
    },
    "Renter8" : {
        "name" : "Somrew Lookmo",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "05/05/1955",
        "info" : "Parents give me money :)",
        "username" : "Want bullet?",
        "password" : "$2b$12$cpqcZ6ny4wfAM8BFDM4Wtea51UjN22Q9js7nQ92Xru6ZoAIXx1.qy"
    },
    "Renter9" : {
        "name" : "Respect Thailand",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "20/02/1969",
        "info" : "Long Live King",
        "username" : "LoveKing",
        "password" : "$2b$12$S2yMjvkJuUld3fgxjYMo5ObrLF3mWms8PGthsBgR0KaAB8GR9id32"
    },
     "Renter10" : {
        "name" : "Frog obob",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "27/12/1975",
        "info" : "Born in R9",
        "username" : "King9",
        "password" : "$2b$12$n/yimqbzMpyRN36H9/jPnusY84MG0k3CxXi9ZfEiJZB4lbGTSS.wm"
    }
}

#Test 
renter_instance_list = []
for i in renter_info_dict:
    renter_instance_list.append(Renter(**renter_info_dict[i]))
