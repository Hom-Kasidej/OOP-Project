from typing import Optional 
from fastapi import FastAPI
from pydantic import BaseModel

import Class as C
import CarInstance as Cars
import EnumClass as EClass


class CarModel(BaseModel):
    brand : EClass.CarBrand
    release_year : int
    seats : int
    doors : int 
    gear_type : EClass.GearType 
    fuel_type : EClass.FuelType
    distance : int
    gps_type : EClass.GPSType
    color :  str
    features : str 
    info : str
    images : str 
    price : int
    location : EClass.ThailandProvince
    type : str
    




app = FastAPI()
system = C.System()

carlist = []
for car in Cars.Car_instance_list:
    system.add_car(car) 

@app.get("/get-all-car/")
async def get_all_car():
    return {
        "data" : system.get_car_list()
    }

@app.put("/car")
async def modify_car(car_ID : str,car : CarModel):
     for thecar in system.get_car_list():
         if  thecar.get_car_ID() == car_ID:
             thecar.set_brand(car.brand)
             thecar.set_release_year(car.release_year)
             thecar.set_seats(car.seats)
             thecar.set_doors(car.doors)
             thecar.set_gear_type(car.gear_type)
             thecar.set_fuel_type(car.fuel_type)
             thecar.set_distance(car.distance)
             thecar.set_gps_type(car.gps_type)
             thecar.set_color(car.color)
             thecar.set_features(car.features)
             thecar.set_info(car.info)
             thecar.set_images(car.images)
             thecar.set_price(car.price)
             thecar.set_location(car.location)
             thecar.set_type(car.type)
     return system.get_car_list()

# @app.post("/post-car/{car_name}")
# def post_car(car_name: str, car : Car):
#     if car_name in car_list:
#         return {"cannot do that" : "car name already exists"}
    
#     car_list[car_name] = car
#     return car_list[car_name]