from .System import System
from .Rent import Rent
from .EnumClass import Status
from .User import Renter
from .instance import dealer_instance_list as dealers,renter_instance_list as renters
from .instance import Car_instance_list as cars
system = System()

for dealer in dealers:
    system.add_account(dealer)

for renter in renters:
    system.add_account(renter)

for car in cars:
    system.add_car(car)


new_rent = Rent(check_in_date="2023-12-10",check_out_date="2023-12-31",rent_status=Status.Pending,rent_car=cars[0],location=cars[0].get_location())

rent_user = system.get_user(14)

system.add_rent(new_rent)
if isinstance(rent_user,Renter):
    rent_user.add_to_incomplete_list(new_rent)
