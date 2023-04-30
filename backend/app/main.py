from fastapi import FastAPI
from .routers import Car,User,Review,Rent

app = FastAPI()

app.include_router(Car.router)

app.include_router(User.router)

app.include_router(Review.router)

app.include_router(Rent.router)

@app.get("/")
async def read_root():
    return {"message" : "Main!"}