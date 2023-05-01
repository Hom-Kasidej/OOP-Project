from fastapi import APIRouter
from ..models.database import dataSystem
from ..models.Review import Review
from ..models.Car import Car

router = APIRouter()

@router.get("/get_reviews/", tags=["Review"])
async def get_review():
    list = []
    for car in dataSystem.get_car_list():
        list.append(car.get_review())
    return {"Reviews" : list}

@router.post("/Cars/{Car_ID}/Review", tags=["Review"])
async def post_review(Car_ID : int,review_dict : dict,renter_id : int):
    for car in dataSystem.get_car_list():
        if car.get_car_ID() == Car_ID:
            for user in dataSystem.get_account_list():
                #print(user.get_id() , renter_id)
                if user.get_id() == renter_id: 
                    if car.create_review(review_dict,user):
                        return {"Message" : "Review created!"}
                    else:
                        return {"Message" : "Can not create review"}
    return {"Message" : f"Car with ID : {Car_ID} not found"}

@router.put("/Cars/{Car_ID}/Review/{review_ID}",tags=["Review"])
async def edit_review(Car_ID : int, review_ID : int, review_dict : dict):
    for car in dataSystem.get_car_list():
        if car.get_car_ID() == Car_ID :
            if not isinstance(car,Car):
                return {"Message" : "Can not load Car"}
            for review in car.get_review():
                if review.get_ID() == review_ID:
                    if not isinstance(review,Review):
                        return {"Message" : "Can not load Review"}
                    review.set_star(review_dict["star"])
                    review.set_info(review_dict["info"])
                    return {"Message" : f"Edit Review with id {review_ID} successfully"}
            return {"Message" : f"Dont found Review with id : {review_ID}"}
    return {"Message" : f"Dont found Car with id : {Car_ID}"}

@router.delete("/Cars/{Car_ID}/Review/{Review_ID}",tags=["Review"])
async def del_review(Car_ID : int, review_ID : int):
    for car in dataSystem.get_car_list():
        if car.get_car_ID() == Car_ID :
            if not isinstance(car,Car):
                return {"Message" : "Can not load Car"}
            for review in car.get_review():
                if review.get_ID() == review_ID:
                    if not isinstance(review,Review):
                        return {"Message" : "Can not load Review"}
                    car.del_review(review)
                    return {"Message" : f"Delete Review with id {review_ID} successfully"}
            return {"Message" : f"Dont found Review with id : {review_ID}"}
    return {"Message" : f"Dont found Car with id : {Car_ID}"}