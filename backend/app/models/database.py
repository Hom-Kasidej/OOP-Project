from .System import System
from .Rent import Rent
from .EnumClass import Status
from .User import Renter
from .instance import dealer_instance_list as dealers,renter_instance_list as renters
from .instance import Car_instance_list as cars
dataSystem = System()

for dealer in dealers:
    dataSystem.add_account(dealer)

for renter in renters:
    dataSystem.add_account(renter)

for car in cars:
    dataSystem.add_car(car)