import Class as C
import DealerInstance as Deal
import CarInstance as Cars


car_catalog = C.CarCatalog(name="City",type_info="City",type_image="None")

dealer = Deal.dealer_list[0] #สร้าง Dealer โดยใช้ Dealer คนแรก
#print(Cars.Car_instance_list)
#print(Cars.car_info_dict['Car1'])

dealer.create_car(Cars.car_info_dict['Car1']) #สร้าง instance รถขึ้นมาและมาเก็บไว้ใน car_list ของ Dealer

dealer.add_to_carcatalog(car_catalog, dealer.get_car_list()[0])#นำ car_list มาเก็บไว้ใน car_catalog

#print(car_catalog.get_car_list()[0].get_car_ID())
#print(dealer.get_car_list()[0].get_brand())