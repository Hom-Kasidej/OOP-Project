from available_cars_page import AvailableCarPage
from car_page import CarPage
from Home_page import HomePage
from login_form import LoginForm
from navbar import NavigationBar
from payment_form import PaymentForm
from postcar_page import  PostCarPage
from profile_page_dealer import ProfilePage as DProfile
from profile_page_renter import ProfilePage as RProfile
from signup_form import SignupForm
import tkinter as tk
import requests

class Application:
    def __init__(self, master):
        self.master = master
        self.user = None
        self.user_type = None
        self.navbar = NavigationBar(self.master,self.show_login_page,self.logout_callback,self.show_home_page,self.show_profile_page)

        self.home_page = HomePage(self.master,self.search_car_callback,self.search_carType_callback)

        self.current_page = self.home_page

        self.login_page = LoginForm(self.master,self.login_success_callback,self.show_signup_page)

        self.sign_up_page = SignupForm(self.show_login_page)

        self.current_page.show()

    def show_page(self,page):
        self.current_page.hide()

        page.show()

        self.current_page = page

    def login_success_callback(self,user):
        self.user = user
        print(self.user)
        if self.user :
            print(self.user)
            self.navbar.show_user_info(self.user['_username'])
            self.navbar.set_login_button_state(False)
            self.navbar.show_login_button()
            self.show_page(self.home_page)
            
            if(self.user['_type'] == 'Renter'):
                self.profile_page = RProfile(self.master,user,self.logout_callback)
                print("Renter")
            elif (self.user['_type'] == 'Dealer'):
                self.profile_page = DProfile(self.master,user,self.logout_callback,self.postcar_callback)
                print("Dealer")
        return

    def logout_callback(self):
        self.user = None
        self.profile_page = None
        self.navbar.set_login_button_state(True)
        self.navbar.show_login_button()
        self.show_page(self.home_page)

    def show_home_page(self , event):
        self.show_page(self.home_page)

    def back_home(self):
        self.show_page(self.home_page)
    
    def show_login_page(self):
        self.show_page(self.login_page)
        # self.login_page.show()

    def show_profile_page(self):
        self.show_page(self.profile_page)

    def search_car_callback(self,car_list):
        if self.user:
            self.availble_car = AvailableCarPage(self.master,car_list,self.select_callback,user_status=True,login_callback=self.show_login_page)
        else:
            self.availble_car = AvailableCarPage(self.master,car_list,self.select_callback,user_status=False,login_callback=self.show_login_page)
        self.show_page(self.availble_car)

    def search_carType_callback(self,car_list):
        if self.user:
            self.availble_car = AvailableCarPage(self.master,car_list,self.select_callback,user_status=True,login_callback=self.show_login_page)
        else:
            self.availble_car = AvailableCarPage(self.master,car_list,self.select_callback,user_status=False,login_callback=self.show_login_page)
        self.show_page(self.availble_car)

    def select_callback(self,car):
        self.car_page = CarPage(self.master,car,self.choose_callback)
        self.show_page(self.car_page)
    
    def show_signup_page(self):
        self.show_page(self.sign_up_page)

    def choose_callback(self,car_id,start_date,end_date):
        print("choose!")
        if self.user:
            api_endpoint = f'http://localhost:8000/Rents/Post?user_id={self.user["_id"]}&car_id={car_id}&start_date={start_date}&end_date={end_date}'
            response = requests.post(api_endpoint)
            if response.ok:
                print(response.json())
                data_dict = response.json()
                rent_id = data_dict['Rent']['_Rent__rent_no']
                self.payment_page = PaymentForm(self.master,rent_id,self.user['_id'],self.back_home)
                self.show_page(self.payment_page)
                
        else:
            pass

    def postcar_callback(self):
        self.postcar_page = PostCarPage(self.master,self.user)
        self.show_page(self.postcar_page)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Login/Sign-up App")
    root.geometry("800x600")
    root.configure(bg="#E6FFFA")
    app = Application(root)
    root.mainloop()
