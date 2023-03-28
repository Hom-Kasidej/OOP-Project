import Class as C
import DealerInstance as dealers
import CarInstance as cars
import RenterInstance as renters

cartype = C.CarType()

carcatalog1 = C.CarCatalog(name="City",type_info="City",type_image="None")
carcatalog2 = C.CarCatalog(name="SUV",type_info="SUV",type_image="None")
carcatalog3 = C.CarCatalog(name="Van",type_info="Van",type_image="None")
carcatalog4 = C.CarCatalog(name="Convertible",type_info="Convertible",type_image="None")

for car in cars.Car_instance_list:
    if(car.get_type() == "City"):
        carcatalog1.add_to_carlist(car)
    if(car.get_type() == "SUV"):
        carcatalog2.add_to_carlist(car)
    if(car.get_type() == "Van"):
        carcatalog3.add_to_carlist(car)
    if(car.get_type() == "Convertible"):
        carcatalog4.add_to_carlist(car)


cartype.add_to_car_catalog(car_catalog=carcatalog1)
cartype.add_to_car_catalog(car_catalog=carcatalog2)
cartype.add_to_car_catalog(car_catalog=carcatalog3)
cartype.add_to_car_catalog(car_catalog=carcatalog4)


car1 = cars.Car_instance_list[0]
car2 = cars.Car_instance_list[1]
car3 = cars.Car_instance_list[4]

car_status = C.CarStatus()
car_status2 = C.CarStatus()
car_status3 = C.CarStatus()

rent1 = C.Rent(check_in_date = "2023-03-21", check_out_date = "2023-03-24", rent_no = 1, rent_status = C.EClass.Status.Success, rent_car = car1, location = "Bangkok", payment = None, receipt = None)
rent2 = C.Rent(check_in_date = "2023-03-26", check_out_date = "2023-03-29", rent_no = 1, rent_status = C.EClass.Status.Success, rent_car = car1, location = "Bangkok", payment = None, receipt = None)
rent3 = C.Rent(check_in_date = "2023-03-26", check_out_date = "2023-03-29", rent_no = 1, rent_status = C.EClass.Status.Success, rent_car = car2, location = "Bangkok", payment = None, receipt = None)
rent4 = C.Rent(check_in_date = "2023-03-26", check_out_date = "2023-03-29", rent_no = 1, rent_status = C.EClass.Status.Success, rent_car = car3, location = "Bangkok", payment = None, receipt = None)

car_status.update_carstatus(rent=rent1)
car_status.update_carstatus(rent=rent2)
car_status2.update_carstatus(rent=rent3)
car_status3.update_carstatus(rent=rent4)

car1.add_carstatus(car_status)
car2.add_carstatus(car_status2)
car3.add_carstatus(car_status3)

start_date = str(C.datetime.datetime.now().date())
end_date = str(C.datetime.datetime.now().date() + C.datetime.timedelta(days=3))
location = C.EClass.ThailandProvince.Bangkok

list = cartype.search_car(location=location,start_date=start_date,end_date=end_date)

for car in list:
    print(car.get_type())

list2 = cartype.search_cartype("City")

print()

for car in list2:
    print(car.get_type())
