from fastapi import APIRouter
from ..config.database import system
from ..models.EnumClass import ThailandProvince, CarType, CarBrand, GearType, FuelType, GPSType, CarColor
from ..models.Car import Car
import datetime

router = APIRouter()

@router.get("/Car",tags=["Car"])
async def get_cars():
    return {"Cars" : system.get_car_list()}

@router.get("/search_car/{location}/",tags=["Car"])
async def search_car(location : ThailandProvince,start_date : datetime.date = datetime.datetime.now().date(),end_date : datetime.date =   datetime.datetime.now().date() + datetime.timedelta(days=3) ):
    return {"Cars" : system.search_car(start_date=start_date,end_date=end_date,location=location)}

@router.get("/search_cartype",tags=["Car"])
async def search_cartype(cartype : CarType):
    return {"Cars" : system.search_cartype(cartype=cartype)}

@router.post("/Post_car/",tags=["Car"])
async def post_car(brand : CarBrand, gear_type : GearType, fuel_type : FuelType, gps_type : GPSType, color : CarColor, cartype : CarType, location : ThailandProvince, cardict : dict):
    # for car in system.get_car_list():
    #     if car.get_car_ID() == :
    #         return {"Car ID already exists"}
    if ( system.add_car(Car(brand=brand
                           , release_year = cardict["release_year"]
                           , seats = cardict["seats"]
                           , doors = cardict["doors"]
                           , gear_type = gear_type
                           , fuel_type = fuel_type
                           , distance = cardict["distance"]
                           , gps_type = gps_type
                           , color = color
                           , features = cardict["features"]
                           , info = cardict["info"]
                           , images = cardict["images"]
                           , price = cardict["price"]
                           , location = location
                           , type = cartype
                           , dealer_ID = cardict["dealer_ID"]))):
        return {"Message" : "Car posted"}
    return {"Message" : "Post car failed"}

@router.delete("/Cars/{target_car_id}",tags=["Car"])
async def delete_car(target_car_id):
    if system.del_car(target_car_id=target_car_id):
        return {"Message" : f"Car with id : {target_car_id} has been deleted"}
    else :
        return {"Message" : f"Car with id : {target_car_id} not found"}

@router.get("/View_car/{target_car_id}",tags=["Car"])
async def get_car(target_car_id : int):
    if (system.get_car(target_car_id)) :
        return {"Car" : system.get_car(target_car_id)}
    else:
        return {"Car": f"Car with ID : {target_car_id} no found!"}