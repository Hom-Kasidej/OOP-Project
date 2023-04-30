from .EnumClass import *
from .Car import Car
from .User import Dealer,Renter

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
        "color" : "Black",
        "features" : "Automatic_seat",
        "info" : "",
        "images" : "",
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
        "color" : "Black",
        "features" : "",
        "info" : "",
        "images" : "",
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
        "color" : "White",
        "features" : "Bluetooth_Music",
        "info" : "",
        "images" : "",
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
        "color" : "blonde",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 2500,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.SUV,
        "dealer_ID" : 2
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
        "color" : "Yellow",
        "features" : "",
        "info" : "",
        "images" : "",
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
        "color" : "Dark_Blue",
        "features" : "",
        "info" : "",
        "images" : "",
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
        "color" : "Gray",
        "features" : "",
        "info" : "",
        "images" : "",
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
        "color" : "Black",
        "features" : "LED SCREEN",
        "info" : "",
        "images" : "",
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
        "color" : "White",
        "features" : "",
        "info" : "",
        "images" : "",
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
        "color" : "Red",
        "features" : "",
        "info" : "",
        "images" : "",
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
        "color" : "Yellow",
        "features" : "",
        "info" : "",
        "images" : "",
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
        "color" : "Purple",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 2099,
        "location" : ThailandProvince.Bangkok,
        "type" : CarType.CITY,
        "dealer_ID" : 4
    }
}

Car_instance_list = []
for i in car_info_dict:
    Car_instance_list.append(Car(**car_info_dict[i]))

dict1 = {
    'Dealer1' : {
        'name' : 'Johnny Peepo',
        'profile_image': 'None',
        'gender' : Gender.Male,
        'birth_date' : '01/01/2001',
        'info' : 'i love cars',
        'username' : 'johnnysoodlo',
        'password' : 'johnny123'
    },
    'Dealer2' : {
        'name' : 'Somchai Hi',
        'profile_image': 'None',
        'gender' : Gender.Male,
        'birth_date' : '11/12/1974',
        'info' : 'Hi',
        'username' : 'somchai911',
        'password' : 'jgdsg1231'
    },
    'Dealer3' : {
        'name' : 'Naruto Sasuke',
        'profile_image': 'None',
        'gender' : Gender.Male,
        'birth_date' : '11/12/1950',
        'info' : 'Hi hello',
        'username' : '1qgqgqwg',
        'password' : 'aegki12124'
    },
    'Dealer4' : {
        'name' : 'Somsri Haha',
        'profile_image': 'None',
        'gender' : Gender.Female,
        'birth_date' : '20/12/1999',
        'info' : 'Hi wassup',
        'username' : 'waegweg134',
        'password' : '12412hlkk'
    }
}

dealer_instance_list = []

for dealer in dict1:
    dealer_instance_list.append(Dealer(**dict1[dealer]))


renter_info_dict = {
    "Renter1" : {
        "name" : "Sompong Payongdej",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "28/02/1987",
        "info" : "Good guy",
        "username" : "Sompong",
        "password" : "ripperisthedog"
    },
    "Renter2" : {
        "name" : "Somsej Eatgrass",
        "profile_image" : "",
        "gender" : Gender.Female,
        "birth_date" : "01/01/1999",
        "info" : "Capybaraaa",
        "username" : "GrossGrass",
        "password" : "iwantgrass555"
    },
    "Renter" : {
        "name" : "Somjett DashForward",
        "profile_image" : "",
        "gender" : Gender.Female,
        "birth_date" : "09/02/2000",
        "info" : "Get out of my way!",
        "username" : "Jett",
        "password" : "333Jettiseasytowin"
    },
     "Renter4" : {
        "name" : "Gekko keeact",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "21/07/2002",
        "info" : "Let's go my buddy",
        "username" : "Anonymous",
        "password" : "OhhoMyBuddy"
    },
    "Renter5" : {
        "name" : "MrBeast Latkrabang",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "11/11/1970",
        "info" : "Who want my money!!",
        "username" : "Beast",
        "password" : "1234567890"
    },
    "Renter6" : {
        "name" : "RestWith OOP",
        "profile_image" : "",
        "gender" : Gender.Female,
        "birth_date" : "19/03/2003",
        "info" : "OOP Project is waiting for you",
        "username" : "OOPInwZa",
        "password" : "KhorGradeANoiKrub55"
    },
    "Renter7" : {
        "name" : "Somying butchai",
        "profile_image" : "",
        "gender" : Gender.Female,
        "birth_date" : "20/09/1997",
        "info" : "I want cheap price",
        "username" : "Somying",
        "password" : "yinglowcost"
    },
    "Renter8" : {
        "name" : "Somrew Lookmo",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "05/05/1955",
        "info" : "Parents give me money :)",
        "username" : "Want bullet?",
        "password" : "666satan666"
    },
    "Renter9" : {
        "name" : "Respect Thailand",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "20/02/1969",
        "info" : "Long Live King",
        "username" : "LoveKing",
        "password" : "999KingKing"
    },
     "Renter10" : {
        "name" : "Frog obob",
        "profile_image" : "",
        "gender" : Gender.Male,
        "birth_date" : "27/12/1975",
        "info" : "Born in R9",
        "username" : "King9",
        "password" : "loveKingThailand"
    }
}

#Test 
renter_instance_list = []
for i in renter_info_dict:
    renter_instance_list.append(Renter(**renter_info_dict[i]))
