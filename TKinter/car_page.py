import tkinter as tk

class CarPage(tk.Frame):
    def __init__(self, master, car_data, choose_callback):
        super().__init__(master)
        self.master = master
        self.car_data = car_data
        self.choose_callback = choose_callback
        self.create_widgets()

    def create_widgets(self):
        # Create car information and picture
        self.car_label = tk.Label(self, text="Car information", font=("TkDefaultFont", 20))

        # Create labels for car data
        self.car_brand_label = tk.Label(self, text=f"Car brand: {self.car_data['_Car__brand']}")
        self.release_year_label = tk.Label(self, text=f"Car release year: {self.car_data['_Car__release_year']}")
        self.seats_label = tk.Label(self, text=f"Car seats: {self.car_data['_Car__seats']}")
        self.doors_label = tk.Label(self, text=f"Car doors: {self.car_data['_Car__doors']}")
        self.gear_type_label = tk.Label(self, text=f"Car gear type: {self.car_data['_Car__gear_type']}")
        self.fuel_type_label = tk.Label(self, text=f"Car fuel type: {self.car_data['_Car__fuel_type']}")
        self.distance_label = tk.Label(self, text=f"Car distance: {self.car_data['_Car__distance']}")
        self.gps_type_label = tk.Label(self, text=f"Car GPS type: {self.car_data['_Car__gps_type']}")
        self.color_label = tk.Label(self, text=f"Car color: {self.car_data['_Car__color']}")
        self.features_label = tk.Label(self, text=f"Car features: {self.car_data['_Car__features']}")
        self.info_label = tk.Label(self, text=f"Car information: {self.car_data['_Car__info']}")

        # Create entry widgets for user information
        self.start_date_label = tk.Label(self, text="Start date:")
        self.start_date_entry = tk.Entry(self)
        self.end_date_label = tk.Label(self, text="End date:")
        self.end_date_entry = tk.Entry(self)
        # self.first_name_label = tk.Label(self, text="First name:")
        # self.first_name_entry = tk.Entry(self)
        # self.last_name_label = tk.Label(self, text="Last name:")
        # self.last_name_entry = tk.Entry(self)

        # Create button to choose car
        self.car_button = tk.Button(self, text="Choose", command=self.choose)

        # Pack all widgets
        self.car_label.pack()
        self.car_brand_label.pack()
        self.release_year_label.pack()
        self.seats_label.pack()
        self.doors_label.pack()
        self.gear_type_label.pack()
        self.fuel_type_label.pack()
        self.distance_label.pack()
        self.gps_type_label.pack()
        self.color_label.pack()
        self.features_label.pack()
        self.info_label.pack()
        self.start_date_label.pack()
        self.start_date_entry.pack()
        self.end_date_label.pack()
        self.end_date_entry.pack()
        # self.first_name_label.pack()
        # self.first_name_entry.pack()
        # self.last_name_label.pack()
        # self.last_name_entry.pack()
        self.car_button.pack()

        self.hide()

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()
    
    def choose(self):
        car_id = self.car_data['_Car__car_ID']
        start_date = self.start_date_entry.get()
        end_date  = self.end_date_entry.get()
        self.choose_callback(car_id,start_date,end_date)




# root = tk.Tk()
# root.title("Login/Sign-up App")
# root.geometry("800x600")
# root.configure(bg="#E6FFFA")
# app = CarPage(root)
# root.mainloop()