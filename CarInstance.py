import backend.app.models.EnumClass as EClass
from backend.app.models.Car import *
car_info_dict = {
    "Car1" : {
        "brand" : EClass.CarBrand.Nissan ,
        "release_year" : 2005,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 5049,
        "gps_type" : EClass.GPSType.NoneGPS,
        "color" : "Black",
        "features" : "Automatic_seat",
        "info" : "",
        "images" : "",
        "price" : 3000,
        "location" : EClass.ThailandProvince.Bangkok,
        "type" : "City",
        "dealer_ID" : "1"
    },
    "Car2" : {
        "brand" : EClass.CarBrand.Honda,
        "release_year" : 2010,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 12654,
        "gps_type" : EClass.GPSType.NoneGPS,
        "color" : "Black",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 3500,
        "location" : EClass.ThailandProvince.Chiang_Mai,
        "type" : "City",
        "dealer_ID" : "2"   
    },
    "Car3" : {
        "brand" : EClass.CarBrand.BMW,
        "release_year" : 2009,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 9801,
        "gps_type" : EClass.GPSType.CarTrack,
        "color" : "White",
        "features" : "Bluetooth_Music",
        "info" : "",
        "images" : "",
        "price" : 4000,
        "location" : EClass.ThailandProvince.Chiang_Rai,
        "type" : "Convertible",
        "dealer_ID" : "1"
    },
    "Car4" : {
        "brand" : EClass.CarBrand.Toyota,
        "release_year" : 2020,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.EV,
        "distance" : "1500",
        "gps_type" : EClass.GPSType.Otoplug,
        "color" : "blonde",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 2500,
        "location" : EClass.ThailandProvince.Bangkok,
        "type" : "SUV",
        "dealer_ID" : "1"
    },
    "Car5" : {
        "brand" : EClass.CarBrand.Chevrolet,
        "release_year" : 2006,
        "seats" : 4,
        "doors" : 4, 
        "gear_type" : EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 15602,
        "gps_type" : EClass.GPSType.NoneGPS,
        "color" : "Yellow",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 3999,
        "location" : EClass.ThailandProvince.Bangkok,
        "type" : "SUV",
        "dealer_ID" : "1"
    },
    "Car6" : {
        "brand" : EClass.CarBrand.Ford,
        "release_year" : 2004,
        "seats" : 7,
        "doors" : 4,
        "gear_type" : EClass.GearType.Manual,
        "fuel_type" : EClass.FuelType.Diesel,
        "distance" : 25040,
        "gps_type" : EClass.GPSType.NoneGPS,
        "color" : "Dark_Blue",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 3000,
        "location" : EClass.ThailandProvince.Bangkok,
        "type" : "SUV",
        "dealer_ID" : "1"
    },
    "Car7" : {
        "brand" : EClass.CarBrand.Honda,
        "release_year" : 2011,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 9800,
        "gps_type" : EClass.GPSType.Others, 
        "color" : "Gray",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 1900,
        "location" : EClass.ThailandProvince.Bangkok,
        "type" : "City",
        "dealer_ID" : "1"
    },
    "Car8" : {
        "brand" : EClass.CarBrand.Honda, 
        "release_year" : 2012,
        "seats" : 10,
        "doors" : 4,
        "gear_type" :EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 16094,
        "gps_type" : EClass.GPSType.NoneGPS,
        "color" : "Black",
        "features" : "LED SCREEN",
        "info" : "",
        "images" : "",
        "price" : 4599,
        "location" : EClass.ThailandProvince.Bangkok,
        "type" : "City",
        "dealer_ID" : "1"
    },
    "Car9" : {
        "brand" : EClass.CarBrand.Honda, 
        "release_year" : 2005,
        "seats" : 4,
        "doors" : 2,
        "gear_type" : EClass.GearType.Manual,
        "fuel_type" : EClass.FuelType.Diesel,
        "distance" : 30071,
        "gps_type" : EClass.GPSType.Others,
        "color" : "White",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 2990,
        "location" : EClass.ThailandProvince.Bangkok,
        "type" : "City",
        "dealer_ID" : "1"
    },
    "Car10" : {
        "brand" : EClass.CarBrand.Lamborgini,
        "release_year" : 2015,
        "seats" : 2,
        "doors" : 2,
        "gear_type" : EClass.GearType.Manual,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 3540,
        "gps_type" : EClass.GPSType.NoneGPS,
        "color" : "Red",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 15000,
        "location" : EClass.ThailandProvince.Nan,
        "type" : "Convertible",
        "dealer_ID" : "1"
    },
    "Car11" : {
        "brand" : EClass.CarBrand.Toyota, 
        "release_year" : 2018,
        "seats" : 7,
        "doors" : 4,
        "gear_type" : EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 14200,
        "gps_type" : EClass.GPSType.Others,
        "color" : "Yellow",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 2600,
        "location" : EClass.ThailandProvince.Bangkok,
        "type" : "SUV",
        "dealer_ID" : "1"
    },
    "Car12" : {
        "brand" : EClass.CarBrand.Nissan,
        "release_year" : 2009,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 18005,
        "gps_type" : EClass.GPSType.Eyefleet,
        "color" : "Purple",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 2099,
        "location" : EClass.ThailandProvince.Bangkok,
        "type" : "City",
        "dealer_ID" : "1"
    },
    "Car13" : {
        "brand" : EClass.CarBrand.Audi,
        "release_year" : 2009,
        "seats" : 4,
        "doors" : 4,
        "gear_type" : EClass.GearType.Auto,
        "fuel_type" : EClass.FuelType.Benzien,
        "distance" : 18005,
        "gps_type" : EClass.GPSType.Eyefleet,
        "color" : "Purple",
        "features" : "",
        "info" : "",
        "images" : "",
        "price" : 29000,
        "location" : EClass.ThailandProvince.Nakhon_Ratchasima,
        "type" : "City",
        "dealer_ID" : "2"
    }
}

#def modify_car_info_dict_value(car_info_dict, car_id, key, new_value):
    #if car_id not in car_info_dict:
        #print(f"Car ID '{car_id}' not found in car_info_dict")
        #return
    
    #car_info_dict[car_id][key] = new_value

#modify_car_info_dict_value(car_info_dict, "Car1", "release_year", 2010)

#print(car_info_dict ,"Car1")

Car_instance_list = []
for i in car_info_dict:
    Car_instance_list.append(Car(**car_info_dict[i]))
