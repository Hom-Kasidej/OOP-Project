from fastapi import FastAPI
import CarInstance as c
from Class import *

app = FastAPI()
system = System()
for car in c.Car_instance_list:
    system.add_car(car)
@app.get("/car/{car_id}")
async def view_car(car_id:str):
    for car in system.get_car_list():
        if car_id == car.get_car_ID():
            temp = {}
            temp['brand'] = car.get_brand()
            temp['car_id'] = car.get_car_ID()
            
            return {"data": temp}


