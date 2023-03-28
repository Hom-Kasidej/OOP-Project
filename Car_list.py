import Class as C
import DealerInstance as Deal
import CarInstance as Cars

dealer = Deal.dealer_list[0] #สร้าง Dealer โดยใช้ Dealer คนแรก
#print(Cars.Car_instance_list)
#print(Cars.car_info_dict['Car1'])

dealer.create_car(Cars.car_info_dict['Car1']) #สร้าง instance รถขึ้นมาและมาเก็บไว้ใน car_list ของ Dealer

#print(dealer.get_car_list()[0].get_brand())