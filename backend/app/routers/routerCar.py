import sys
sys.path.insert(1,"backend\\app\\models")
sys.path.insert(2,"backend\\app\\database")
from fastapi import APIRouter
from ..models.database import dataSystem
from ..models.EnumClass import ThailandProvince, CarType, CarBrand, GearType, FuelType, GPSType, CarColor
from ..models.Car import Car
import datetime

router = APIRouter()

@router.get("/Car",tags=["Car"])
async def get_cars():
    return {"Cars" : dataSystem.get_car_list()}

@router.post("/search_car/{location}/",tags=["Car"])
async def search_car(location : ThailandProvince,start_date : datetime.date = datetime.datetime.now().date(),end_date : datetime.date =   datetime.datetime.now().date() + datetime.timedelta(days=3) ):
    return {"Cars" : dataSystem.search_car(start_date=start_date,end_date=end_date,location=location)}

@router.post("/search_cartype",tags=["Car"])
async def search_cartype(cartype : CarType):
    return {"Cars" : dataSystem.search_cartype(cartype=cartype)}

@router.post("/Post_car/",tags=["Car"])
async def post_car(brand : CarBrand, gear_type : GearType, fuel_type : FuelType, gps_type : GPSType, color : CarColor, cartype : CarType, location : ThailandProvince,
                   release_year : int,seats : int, doors: int, distance : int, features : str,info : str,price : int,dealer_id : int):
    # for car in dataSystem.get_car_list():
    #     if car.get_car_ID() == :
    #         return {"Car ID already exists"}
    if ( dataSystem.add_car(Car(brand=brand
                           , release_year = release_year
                           , seats = seats
                           , doors = doors
                           , gear_type = gear_type
                           , fuel_type = fuel_type
                           , distance = distance
                           , gps_type = gps_type
                           , color = color
                           , features = features
                           , info = info
                           , price = price
                           , location = location
                           , type = cartype
                           , dealer_ID = dealer_id))):
        return {"Message" : "Car posted"}
    return {"Message" : "Post car failed"}

@router.delete("/Cars/{target_car_id}",tags=["Car"])
async def delete_car(target_car_id : int):
    if dataSystem.del_car(target_car_id=target_car_id):
        return {"Message" : f"Car with id : {target_car_id} has been deleted"}
    else :
        return {"Message" : f"Car with id : {target_car_id} not found"}

@router.post("/View_car/{target_car_id}",tags=["Car"])
async def get_car(target_car_id : int):
    if (dataSystem.get_car(target_car_id)) :
        return {"Car" : dataSystem.get_car(target_car_id)}
    else:
        return {"Car": f"Car with ID : {target_car_id} no found!"}