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