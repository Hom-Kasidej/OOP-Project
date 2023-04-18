from fastapi import APIRouter
from ..config.database import system

router = APIRouter()

@router.get("/Users/",tags=["User"])
async def get_users():
    return {"User" : system.get_account_list()}

@router.get("/Login/",tags=["User"])
async def login(username : str, password : str):
    if system.login(username=username,password=password):
        return {"Message" : "Login successful!"}
    else:
        return {"Message" : "Login Fail"}

@router.post("/Register/",tags=["User"])
async def register(userdict : dict):
    if system.register(firstname=userdict["firstname"],lastname=userdict["lastname"],username=userdict["username"],password=userdict["password"],confirm_password=userdict["confirm_password"],account_type=userdict["account_type"]):
        return {"Message" : "Register successful!"}
    else :
        return {"Message" : "Register Fail"}