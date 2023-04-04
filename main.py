from Class import *
import DealerInstance as dealers
import CarInstance as cars
import RenterInstance as renters

cartype = System()

for car in cars.Car_instance_list:
    cartype.add_car(car)

car1 = cars.Car_instance_list[0]
car2 = cars.Car_instance_list[1]
car3 = cars.Car_instance_list[4]

rent1 = Rent(check_in_date = "2023-03-21", check_out_date = "2023-03-24", rent_no = 1, rent_status = EClass.Status.Success, rent_car = car1, location = EClass.ThailandProvince.Bangkok, payment = None, receipt = None)
rent2 = Rent(check_in_date = "2023-03-26", check_out_date = "2023-03-29", rent_no = 1, rent_status = EClass.Status.Success, rent_car = car1, location = EClass.ThailandProvince.Bangkok, payment = None, receipt = None)
rent3 = Rent(check_in_date = "2023-03-26", check_out_date = "2023-03-29", rent_no = 1, rent_status = EClass.Status.Success, rent_car = car2, location = EClass.ThailandProvince.Bangkok, payment = None, receipt = None)
rent4 = Rent(check_in_date = "2023-03-26", check_out_date = "2023-03-29", rent_no = 1, rent_status = EClass.Status.Success, rent_car = car3, location = EClass.ThailandProvince.Bangkok, payment = None, receipt = None)

car1.add_carstatus(rent=rent1)
car1.add_carstatus(rent=rent2)
car2.add_carstatus(rent=rent3)
car3.add_carstatus(rent=rent4)

start_date = str(datetime.datetime.now().date())
end_date = str(datetime.datetime.now().date() + datetime.timedelta(days=3))
location = EClass.ThailandProvince.Bangkok

list = cartype.search_car(location=location,start_date=start_date,end_date=end_date)

for car in list:
    print(car)

list2 = cartype.search_cartype("SUV")

print()

for car in list2:
    print(car)
