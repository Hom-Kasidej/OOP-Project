from fastapi import FastAPI
from .routers import Car,User

app = FastAPI()

app.include_router(Car.router)

app.include_router(User.router)


@app.get("/")
async def read_root():
    return {"message" : "Main!"}