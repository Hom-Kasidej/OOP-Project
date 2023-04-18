import Class as C
import DealerInstance as Deal
import CarInstance as Cars


car_catalog = C.CarCatalog()

dealer = Deal.dealer_instance_list[0] #สร้าง Dealer โดยใช้ Dealer คนแรก

dealer.post_car(Cars.car_info_dict['Car1'],car_catalog) #post_car ทำการสร้าง instance รถ แล้วใส่ไว้ใน car_catalog
dealer.post_car(Cars.car_info_dict['Car2'],car_catalog)

print(car_catalog.get_car_list())