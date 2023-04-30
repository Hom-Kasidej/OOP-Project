from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import Class
import EnumClass as EClass
import CarInstance as cars
import DealerInstance as dealers

class Car(BaseModel):
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

system = Class.System()

for i in range(len(cars.Car_instance_list)):
    system.add_car(cars.Car_instance_list[i])

@app.post("/post-car/{car_id}")
def post_car(car_id: int, car : Car):
    for car in system.get_car_list():
        if car_id == car.get_car_ID():
            return {"car ID already exists"}
    
    system.add_car(car)
    return {"Post successfull"}

@app.get("/get-all-car/")
def get_all_car():
    return system.get_car_list()

@app.get("/get-car/{car_id}")
def get_car(car_id : int):
    for car in system.get_car_list():
        if car_id == car.get_car_ID():
            return car
    return {"Car ID not exists"}

@app.delete("/delete-car/{car_id}")
def delete_car(car_id : int):
    for car in system.get_car_list():
        if car_id == car.get_car_ID():
            system.remove(car)
            return {"Delete successfull"}
    return {"Car ID not exists"}