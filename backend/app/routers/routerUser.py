import sys
sys.path.insert(0,'/backend/app/models')
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..models.database import dataSystem
from ..models.EnumClass import Gender
from ..models.User import Renter,Dealer
from jose import JWTError,  jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel


SECRET_KEY = "9ced490b93249e3823d2e248b18b9a2b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    username : str or None = None

class BaseModelUser(BaseModel):
    username : str
    name : str or None = None
    profile_image : str or None = None
    gender : Gender or None = None
    birth_date : str or None = None
    info : str or None = None
    disabled : bool or None = None

class UserInDB(BaseModelUser):
    hashed_password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Users/login-token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username : str):
    for user in dataSystem.get_account_list():
        if user.get_username() == username:
            return user
    return False
        
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password,user.get_password()):
        return False
    
    return user

def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else: 
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,detail="Could not validate creddentials", headers={"WWW-Autheticate" : "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception
    
    user = get_user(username=token_data.username)
    if user is None:
        raise credential_exception
    
    return user

async def get_current_active_user(curent_user: UserInDB = Depends(get_current_user)):
    if curent_user.get_disabled():
        raise HTTPException(status_code=400,detail="Inactive user")
    
    return curent_user


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

@router.post("/Users/login-token", response_model=Token)
async def login_for_access_token(from_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(from_data.username,from_data.password)
    if not user :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Autheticate" : "Bearer"})

    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub" : user.get_username()},expires_delta=access_token_expire)
    return {"access_token" : access_token, "token_type" : "bearer"}

@router.get("/Users/me/")
async def read_users_me(current_user: BaseModelUser = Depends(get_current_active_user)):
    return {"user" : current_user}

@router.get("/Users/me/info")
async def read_user_info(current_user: BaseModelUser = Depends(get_current_active_user)):
    return [{"info" : current_user.get_info(), "owner" : current_user}]