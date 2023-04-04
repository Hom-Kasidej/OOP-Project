from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from Class import *
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

car_list = cars.car_info_dict
app = FastAPI()

@app.post("/post-car/{car_name}")
def post_car(car_name: str, car : Car):
    if car_name in car_list:
        return {"I NGO" : "car name already existss"}
    
    car_list[car_name] = car
    return car_list[car_name]

@app.get("/get-all-car/")
def get_all_car():
    return car_list

@app.get("/get-car/{car_name}")
def get_car(car_name : str):
    if car_name in car_list:
        return car_list[car_name]
    return {"Car name not exists"}

@app.delete("/delete-car/{car_name}")
def delete_car(car_name : str):
    if car_name in car_list:
        del car_list[car_name]
        return {"Delete successfull"}
    return {"Car name not exists"}