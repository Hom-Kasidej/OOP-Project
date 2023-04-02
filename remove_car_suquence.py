import Class as C
import DealerInstance as dealers
import CarInstance as cars

cartype = C.CarType()

carcatalog1 = C.CarCatalog(name="City",type_info="City",type_image="None")
carcatalog2 = C.CarCatalog(name="SUV",type_info="SUV",type_image="None")
carcatalog3 = C.CarCatalog(name="Van",type_info="Van",type_image="None")
carcatalog4 = C.CarCatalog(name="Convertible",type_info="Convertible",type_image="None")

"""
for car in cars.Car_instance_list:
    if(car.get_type() == "City"):
        carcatalog1.add_to_carlist(car)
    if(car.get_type() == "SUV"):
        carcatalog2.add_to_carlist(car)
    if(car.get_type() == "Van"):
        carcatalog3.add_to_carlist(car)
    if(car.get_type() == "Convertible"):
        carcatalog4.add_to_carlist(car)
"""

cartype.add_to_car_catalog(car_catalog=carcatalog1)
cartype.add_to_car_catalog(car_catalog=carcatalog2)
cartype.add_to_car_catalog(car_catalog=carcatalog3)
cartype.add_to_car_catalog(car_catalog=carcatalog4)

def print_car_cat():
    for catalog in cartype.get_car_catalogs():
        print(catalog.get_name(), end=" : ")
        for car in catalog.get_car_list():
            print(car.get_car_ID(), end=" ")
        print()

dealer1 = dealers.dealer_list[0]

dealer1.create_car(cars.car_info_dict["Car1"])
dealer1.add_to_carcatalog(carcatalog1, dealer1.get_car_list()[0])

def print_dealer_car():
    print("Dealer car's :", end=" ")
    for car in dealer1.get_car_list():
        print(car.get_car_ID(), end=" ")
    print()

print_car_cat()
print_dealer_car()
print()

dealer1.remove_car(carcatalog1, dealer1.get_car_list()[0])
dealer1.delete_car(dealer1.get_car_list()[0])

print_car_cat()
print_dealer_car()
print()
