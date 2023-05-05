import sys
sys.path.insert(0,'/backend/app/models')
from ..models.database import dataSystem
from fastapi import APIRouter, Depends, HTTPException, status
from ..models.database import dataSystem as system
from ..models.EnumClass import Gender
from ..models.User import Renter,Dealer

router = APIRouter()

@router.get("/Users/",tags=["User"])
async def get_users():
    return {"User" : dataSystem.get_account_list()}

@router.post("/User/Register/",tags=["User"])
async def register(userdict : dict):
    if dataSystem.register(firstname=userdict["firstname"],lastname=userdict["lastname"],username=userdict["username"],password=userdict["password"],confirm_password=userdict["confirm_password"],account_type=userdict["account_type"]):
        return {"Message" : "Register successful!"}
    else :
        return {"Message" : "Register Fail"}

@router.put("/User/Modify/{user_id}",tags=["User"])
async def modify(user_id : int,userdict : dict,gender : Gender):
    for user in dataSystem.get_account_list():
        if user.get_id() == user_id:
            if dataSystem.modify(user,userdict,gender):
                return {"Message" : f"User with ID : {user_id} has been modify"}
            else:
                return {"Message" : "Error can not modify User"}
    return {"Message" : f"User with ID : {user_id} not found"}

@router.post("/User/Rents",tags=["User"])
async def get_rents(user_id : int):
    user = dataSystem.get_user(user_id)
    if isinstance(user,Dealer) or isinstance(user,Renter):
        in_complete = user.get_incomplete_list()
        canceled = user.get_canceled_list()
        success= user.get_success_list()
        rent_dict = {"in_complete" : in_complete,
                     "canceled" : canceled,
                      "success" : success}
        return {"Massage":"All Rents","in_complete" : in_complete,"canceled" : canceled,"success" : success}
    return {"Massage" : "Fail to load User"}

@router.post("/User/Login/",tags=["User"])
async def login(data : dict):
    if system.login(username=data['username'],password=data['password']):
        return {'status' : 'ok',    
                "Message" : "Login successful!",
                'user' : system.get_username(data["username"])}
    else:
        return {"Message" : "Login Fail"}