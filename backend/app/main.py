<<<<<<< HEAD
from fastapi import FastAPI
from .routers import routerCar,routerRent, routerReview, routerUser

app = FastAPI()

app.include_router(routerCar.router)

app.include_router(routerUser.router)

app.include_router(routerReview.router)

app.include_router(routerRent.router)

@app.get("/")
async def read_root():
    return {"message" : "Main!"}
=======
from fastapi import FastAPI
from .routers import Car,User,Review,Rent

app = FastAPI()

app.include_router(Car.router)

app.include_router(User.router)

app.include_router(Review.router)

app.include_router(Rent.router)

@app.get("/")
async def read_root():
>>>>>>> 6f9dff719ffe9a6648f12355d7bc8791ddafbb6a
