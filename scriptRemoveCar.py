import Class as C
import DealerInstance as dealers
import CarInstance as cars

###########################################################

catalog = C.System()

dealer1 = dealers.dealer_instance_list[0]
dealer2 = dealers.dealer_instance_list[1]

i = 0
for car in cars.Car_instance_list:
    if i != 12:
        catalog.add_car(car)
    i += 1

###########################################################

def print_all():
    print("Catalog : ", end="")
    for car in catalog.get_car_list():
        print(f"{car.get_car_ID()}({car.get_dealer_ID()})", end=" ")
    print()

    print("Dealer 1's catalog : ", end="")
    for car in catalog.get_car_list():
        if car.get_dealer_ID() == dealer1.get_ID():
            print(f"{car.get_car_ID()}", end=" ")
    print()

    print("Dealer 2's catalog : ", end="")
    for car in catalog.get_car_list():
        if car.get_dealer_ID() == dealer2.get_ID():
            print(f"{car.get_car_ID()}", end=" ")
    print()

###########################################################

print_all()

dealer1.remove_car(catalog, catalog.get_car_list()[4])
print_all()

dealer2.remove_car(catalog, catalog.get_car_list()[0])
print_all()

dealer2.post_car(catalog, cars.car_info_dict["Car13"])
print_all()