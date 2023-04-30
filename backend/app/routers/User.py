from fastapi import APIRouter
from ..models.database import system
from ..models.EnumClass import Gender
from ..models.User import Renter,Dealer

router = APIRouter()

@router.get("/Users/",tags=["User"])
async def get_users():
    return {"User" : system.get_account_list()}

@router.post("/User/Login/",tags=["User"])
async def login(userdict : dict):
    if system.login(username=userdict["username"],password=userdict["password"]):
        return {"Message" : "Login successful!"}
    else:
        return {"Message" : "Login Fail"}

@router.post("/User/Register/",tags=["User"])
async def register(userdict : dict):
    if system.register(firstname=userdict["firstname"],lastname=userdict["lastname"],username=userdict["username"],password=userdict["password"],confirm_password=userdict["confirm_password"],account_type=userdict["account_type"]):
        return {"Message" : "Register successful!"}
    else :
        return {"Message" : "Register Fail"}

@router.put("/User/Modify/{user_id}",tags=["User"])
async def modify(user_id : int,userdict : dict,gender : Gender):
    for user in system.get_account_list():
        if user.get_id() == user_id:
            if system.modify(user,userdict,gender):
                return {"Message" : f"User with ID : {user_id} has been modify"}
            else:
                return {"Message" : "Error can not modify User"}
    return {"Message" : f"User with ID : {user_id} not found"}

@router.post("/User/Rents",tags=["User"])
async def get_rents(user_id : int):
    user = system.get_user(user_id)
    if isinstance(user,Dealer) or isinstance(user,Renter):
        in_complete = user.get_incomplete_list()
        canceled = user.get_canceled_list()
        success= user.get_success_list()
        rent_dict = {"in_complete" : in_complete,
                     "canceled" : canceled,
                      "success" : success}
        return {"Massage":"All Rents","in_complete" : in_complete,"canceled" : canceled,"success" : success}
    return {"Massage" : "Fail to load User"}