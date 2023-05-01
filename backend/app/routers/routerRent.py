from fastapi import APIRouter
from ..models.database import dataSystem
from ..models.Rent import Rent
from ..models.Receipt import Receipt
from ..models.Payment import CashPayment,CreditCardPayment
from ..models.EnumClass import Status
from ..models.User import Renter
import datetime

router = APIRouter()

@router.get("/Rents",tags=["Rent"])
async def get_rents():
    return {"Rents" : dataSystem.get_rent_list()}

@router.get("/Payments",tags=["Rent"])
async def get_payments():
    return {"Payments" : dataSystem.get_payment_list()}

@router.post("/Rents/Post",tags=["Rent"])
async def make_rent(user_id : int, car_id : int,start_date : datetime.date,end_date : datetime.date):
    car = dataSystem.get_car(car_id)
    user = dataSystem.get_user(user_id)
    if not car :
        return {"Message" : "Fail to load car"}
    elif not user :
        return {"Message" : "Fail to load user"}
    else:
        if dataSystem.make_rent(check_in_date=start_date,
                            check_out_date=end_date,
                            car=car,
                            user=user) :
            return {"Massage" : "Create Rent Successfully"}
        else:
            return {"Massage" : "Create Rent Fail"}

@router.post("/Rents/{rent_id}/Payment",tags=["Rent"])
async def make_payment(paymentdict : dict,rent_id : int):
    rent = dataSystem.get_rent(rent_id=rent_id)
    if not rent :
        return {"Massage" : "Fail to load rent"} 
    if rent.get_check_in_date() == str:
        start_date = datetime.datetime.strptime(rent.get_check_in_date(), "%Y-%m-%d").date()
    else:
        start_date = rent.get_check_in_date()
    if rent.get_check_out_date() == str:
        end_date = datetime.datetime.strptime(rent.get_check_out_date(), "%Y-%m-%d").date()
    else:
        end_date = rent.get_check_out_date()
    car = rent.get_rent_car()
    duration = (end_date - start_date).days
    payment_amount = duration * car.get_price()
    if paymentdict["payment_type"] == 0: # CashPayment
        if dataSystem.create_CashPayment(paymentdict,amount=payment_amount,rent=rent):
            return {"Massage" : "Create CashPayment successfully"}
        else:
            return {"Massage" : "Can not create Payment"}
    elif paymentdict["payment_type"] == 1: # CreditCardPayment
        if dataSystem.create_CreditPayment(paymentdict,amount=payment_amount,rent=rent):
            return {"Massage" : "Create CreditCardPayment successfully"}
        else:
            return {"Massage" : "Can not create Payment"}

@router.post("/Rents/{rent_id}/RentProcess",tags=["Rent"])
async def rent_process(rent_id : int,user_id : int):
    rent = dataSystem.get_rent(rent_id)
    if not isinstance(rent,Rent) :
        return {"Massage" : "Fail to load Rent"}
    
    user = dataSystem.get_user(user_id)
    if not isinstance(user,Renter):
        return {"Massage" : "Fail to load user"}
    
    if rent.get_rent_status() == Status.Canceled:
        user.add_to_canceled_list(rent)
        user.del_in_incomplete_list(rent)
        return {"Message" : "Cancel rent Completed"}
    
    payment = rent.get_payment()

    if not isinstance(payment,CashPayment) and not isinstance(payment,CreditCardPayment):
        return {"Massage" : "Process Payment First"}

    if payment.get_payment_status() == Status.Success:
        rent.update_rent_status(Status.Success)
        rent.create_receipt(payment)
        user.del_in_incomplete_list(rent)
        user.add_to_success_list(rent)
        return {"Message" : "Rent updated!"}

    elif payment.get_payment_status() == Status.Canceled:
        rent.update_rent_status(Status.Canceled)
        user.del_in_incomplete_list(rent)
        user.add_to_canceled_list(rent)
        return {"Message" : "Rent updated!"}
    
@router.post("/Rents/{rent_id}/RentCancel",tags=["Rent"])
async def rent_cancel(rent_id : int):
    rent = dataSystem.get_rent(rent_id)
    if isinstance(rent, Rent):
        rent.update_rent_status(Status.Canceled)
        return {"Message" : "Rent canceled"}
    return {"Message" : "Can not load rent"}

@router.post("/Payments/{payment_id}/PaymentProcess",tags=["Rent"])
async def payment_process(status : Status,payment_id : int):
    payment = dataSystem.get_payment(payment_id)
    if isinstance(payment,CreditCardPayment) or isinstance(payment,CashPayment):
        payment.update_payment_status(status)
        return {"Massage" : "Payment updated!"}
    return {"Massage" : "Can not load Payment"}

@router.post("/Payments/{payment_id}/PaymentCancel",tags=["Rent"])
async def payment_cancel(payment_id : int):
    payment = dataSystem.get_payment(payment_id)
    if isinstance(payment,CreditCardPayment) or isinstance(payment,CashPayment):
        payment.update_payment_status(Status.Canceled)
        return {"Message" : "Payment canceled"}
    return {"Message" : "Can not load Payment"}

