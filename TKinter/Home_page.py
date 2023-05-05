import tkinter as tk
import datetime
from tkinter import ttk
import requests

class HomePage:
    def __init__(self, parent,serach_callback,search_carType_callback):
        self.search_callback = serach_callback
        self.search_carType_callback = search_carType_callback 
        self.parent = parent
        self.create_widgets()
        self.show()

    def create_widgets(self):
        self.title_label = tk.Label(self.parent, text="Welcome to my home page!", font=("Arial", 24))

        self.info_label = tk.Label(self.parent, text="This is a sample home page created with Tkinter.")

        provinces = ['',"Amnat Charoen",  "Ang Thong",  "Bangkok",  "Bueng Kan",  "Buri Ram",  "Chachoengsao",  "Chai Nat",  "Chaiyaphum",  "Chanthaburi",  "Chiang Mai",  "Chiang Rai",  "Chon Buri",  "Chumphon",  "Kalasin",  "Kamphaeng Phet",  "Kanchanaburi",  "Khon Kaen",  "Krabi",  "Lampang",  "Lamphun",  "Loei",  "Lopburi",  "Mae Hong Son",  "Maha Sarakham",  "Mukdahan",  "Nakhon Nayok",  "Nakhon Pathom",  "Nakhon Phanom",  "Nakhon Ratchasima",  "Nakhon Sawan",  "Nakhon Si Thammarat",  "Nan",  "Narathiwat",  "Nong Bua Lam Phu",  "Nong Khai",  "Nonthaburi",  "Pathum Thani",  "Pattani",  "Phang Nga",  "Phatthalung",  "Phayao",  "Phetchabun",  "Phetchaburi",  "Phichit",  "Phitsanulok",  "Phra Nakhon Si Ayutthaya",  "Phrae",  "Phuket",  "Prachin Buri",  "Prachuap Khiri Khan",  "Ranong",  "Ratchaburi",  "Rayong",  "Roi Et",  "Sa Kaeo",  "Sakon Nakhon",  "Samut Prakan",  "Samut Sakhon",  "Samut Songkhram",  "Saraburi",  "Satun",  "Sing Buri",  "Sisaket",  "Songkhla",  "Sukhothai",  "Suphanburi",  "Surat Thani",  "Surin",  "Tak",  "Trang",  "Trat",  "Ubon Ratchathani",  "Udon Thani",  "Uthai Thani",  "Uttaradit",  "Yala",  "Yasothon"]
        self.province_label = tk.Label(self.parent, text="Select a province:")
        self.province_var = tk.StringVar()
        self.province_var.set(provinces[0])
        self.province_optionmenu = ttk.Combobox(self.parent, textvariable=self.province_var, values=provinces)

        self.date_label = tk.Label(self.parent, text="จาก:")
        self.date_var = tk.StringVar()
        self.date_entry = tk.Entry(self.parent)

        self.date_label = tk.Label(self.parent, text="จนกระทั่ง:")
        self.date_var_2 = tk.StringVar()
        self.date2_entry = tk.Entry(self.parent)

        self.search_button = tk.Button(self.parent, text="Search", command=self.search)
        
        carTypes = ['Sedan','Coupe','City','Van']
        
        
        self.search_button1 = tk.Button(self.parent, text="Sedan", command= lambda: self.search_carType("Sedan"))
        self.search_button2 = tk.Button(self.parent, text="Coupe", command= lambda: self.search_carType("Coupe"))
        self.search_button3 = tk.Button(self.parent, text="City", command= lambda: self.search_carType("City"))
        self.search_button4 = tk.Button(self.parent, text="SUV", command= lambda: self.search_carType("SUV"))

    def show(self):
        self.title_label.pack(padx=10, pady=10)
        self.info_label.pack(padx=10, pady=10)
        self.province_label.pack(padx=10, pady=10)
        self.province_optionmenu.pack(padx=10, pady=10)
        self.date_label.pack(padx=10, pady=10)
        self.date_entry.pack(padx=10, pady=10)
        self.date_label.pack(padx=10, pady=10)
        self.date2_entry.pack(padx=10, pady=10)
        self.search_button.pack(padx=10, pady=10)
        self.search_button1.pack(padx=10, pady=10)
        self.search_button2.pack(padx=10, pady=10)
        self.search_button3.pack(padx=10, pady=10)
        self.search_button4.pack(padx=10, pady=10)

    def hide(self):
        self.title_label.pack_forget()
        self.info_label.pack_forget()
        self.province_label.pack_forget()
        self.province_optionmenu.pack_forget()
        self.date_label.pack_forget()
        self.date_entry.pack_forget()
        self.date_label.pack_forget()
        self.date2_entry.pack_forget()
        self.search_button.pack_forget()
        self.search_button1.pack_forget()
        self.search_button2.pack_forget()
        self.search_button3.pack_forget()
        self.search_button4.pack_forget()
        

    def search(self):
        selected_province = self.province_var.get()
        start_date = self.date_entry.get()
        end_date = self.date2_entry.get()    
        print(start_date)
        print(end_date)
        if selected_province == "" or start_date == "" or end_date == "":
            return
        api_endpoint = f'http://localhost:8000/search_car/{selected_province}/?start_date={start_date}&end_date={end_date}'
        response = requests.post(api_endpoint)
        if response.ok:
            car_dict = response.json()
            car_list = car_dict['Cars']
            print(car_list)
            self.search_callback(car_list)

    def search_carType(self,type):
        api_endpoint = f'http://localhost:8000/search_cartype?cartype={type}'
        response = requests.post(api_endpoint)
        if response.ok:
            car_dict = response.json()
            car_list = car_dict['Cars']
            print(car_list)
            self.search_carType_callback(car_list)

class HomePage:
    def __init__(self, parent,serach_callback,search_carType_callback):
        self.search_callback = serach_callback
        self.search_carType_callback = search_carType_callback 
        self.parent = parent
        self.create_widgets()
        self.show()

    def create_widgets(self):
        self.title_label = tk.Label(self.parent, text="Welcome to my home page!", font=("Arial", 24))

        self.info_label = tk.Label(self.parent, text="This is a sample home page created with Tkinter.")

        provinces = ['',"Amnat Charoen",  "Ang Thong",  "Bangkok",  "Bueng Kan",  "Buri Ram",  "Chachoengsao",  "Chai Nat",  "Chaiyaphum",  "Chanthaburi",  "Chiang Mai",  "Chiang Rai",  "Chon Buri",  "Chumphon",  "Kalasin",  "Kamphaeng Phet",  "Kanchanaburi",  "Khon Kaen",  "Krabi",  "Lampang",  "Lamphun",  "Loei",  "Lopburi",  "Mae Hong Son",  "Maha Sarakham",  "Mukdahan",  "Nakhon Nayok",  "Nakhon Pathom",  "Nakhon Phanom",  "Nakhon Ratchasima",  "Nakhon Sawan",  "Nakhon Si Thammarat",  "Nan",  "Narathiwat",  "Nong Bua Lam Phu",  "Nong Khai",  "Nonthaburi",  "Pathum Thani",  "Pattani",  "Phang Nga",  "Phatthalung",  "Phayao",  "Phetchabun",  "Phetchaburi",  "Phichit",  "Phitsanulok",  "Phra Nakhon Si Ayutthaya",  "Phrae",  "Phuket",  "Prachin Buri",  "Prachuap Khiri Khan",  "Ranong",  "Ratchaburi",  "Rayong",  "Roi Et",  "Sa Kaeo",  "Sakon Nakhon",  "Samut Prakan",  "Samut Sakhon",  "Samut Songkhram",  "Saraburi",  "Satun",  "Sing Buri",  "Sisaket",  "Songkhla",  "Sukhothai",  "Suphanburi",  "Surat Thani",  "Surin",  "Tak",  "Trang",  "Trat",  "Ubon Ratchathani",  "Udon Thani",  "Uthai Thani",  "Uttaradit",  "Yala",  "Yasothon"]
        self.province_label = tk.Label(self.parent, text="Select a province:")
        self.province_var = tk.StringVar()
        self.province_var.set(provinces[0])
        self.province_optionmenu = ttk.Combobox(self.parent, textvariable=self.province_var, values=provinces)

        self.date_label = tk.Label(self.parent, text="จาก:")
        self.date_var = tk.StringVar()
        self.date_entry = tk.Entry(self.parent)

        self.date_label = tk.Label(self.parent, text="จนกระทั่ง:")
        self.date_var_2 = tk.StringVar()
        self.date2_entry = tk.Entry(self.parent)

        self.search_button = tk.Button(self.parent, text="Search", command=self.search)
        
        carTypes = ['Sedan','Coupe','City','Van']
        
        
        self.search_button1 = tk.Button(self.parent, text="Sedan", command= lambda: self.search_carType("Sedan"))
        self.search_button2 = tk.Button(self.parent, text="Coupe", command= lambda: self.search_carType("Coupe"))
        self.search_button3 = tk.Button(self.parent, text="City", command= lambda: self.search_carType("City"))
        self.search_button4 = tk.Button(self.parent, text="SUV", command= lambda: self.search_carType("SUV"))

    def show(self):
        self.title_label.pack(padx=10, pady=10)
        self.info_label.pack(padx=10, pady=10)
        self.province_label.pack(padx=10, pady=10)
        self.province_optionmenu.pack(padx=10, pady=10)
        self.date_label.pack(padx=10, pady=10)
        self.date_entry.pack(padx=10, pady=10)
        self.date_label.pack(padx=10, pady=10)
        self.date2_entry.pack(padx=10, pady=10)
        self.search_button.pack(padx=10, pady=10)
        self.search_button1.pack(padx=10, pady=10)
        self.search_button2.pack(padx=10, pady=10)
        self.search_button3.pack(padx=10, pady=10)
        self.search_button4.pack(padx=10, pady=10)

    def hide(self):
        self.title_label.pack_forget()
        self.info_label.pack_forget()
        self.province_label.pack_forget()
        self.province_optionmenu.pack_forget()
        self.date_label.pack_forget()
        self.date_entry.pack_forget()
        self.date_label.pack_forget()
        self.date2_entry.pack_forget()
        self.search_button.pack_forget()
        self.search_button1.pack_forget()
        self.search_button2.pack_forget()
        self.search_button3.pack_forget()
        self.search_button4.pack_forget()
        

    def search(self):
        selected_province = self.province_var.get()
        start_date = self.date_entry.get()
        end_date = self.date2_entry.get()    
        print(start_date)
        print(end_date)
        if selected_province == "" or start_date == "" or end_date == "":
            return
        api_endpoint = f'http://localhost:8000/search_car/{selected_province}/?start_date={start_date}&end_date={end_date}'
        response = requests.post(api_endpoint)
        if response.ok:
            car_dict = response.json()
            car_list = car_dict['Cars']
            print(car_list)
            self.search_callback(car_list)

    def search_carType(self,type):
        api_endpoint = f'http://localhost:8000/search_cartype?cartype={type}'
        response = requests.post(api_endpoint)
        if response.ok:
            car_dict = response.json()
            car_list = car_dict['Cars']
            print(car_list)
            self.search_carType_callback(car_list)



# root = tk.Tk()
# root.title("Login/Sign-up App")
# root.geometry("800x600")
# home = HomePage(root)
# root.mainloop()
