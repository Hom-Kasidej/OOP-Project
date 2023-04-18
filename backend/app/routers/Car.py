from fastapi import APIRouter
from ..config.database import system
from ..models.EnumClass import ThailandProvince,CarType
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
async def post_car(cardict : dict):
    return {"Message" : "status"}

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