import tkinter as tk


class PostCarPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Define car information
        # self.img = tk.PhotoImage(file='car.png')
        self.brand = 'Toyota'
        self.release_year = '2019'
        self.seats = '5'
        self.doors = '4'
        self.gear_type = 'Automatic'
        self.fuel_type = 'Petrol'
        self.distance = '20,000 km'
        self.gps_type = 'Built-in'
        self.color = 'White'
        self.features = ['Air Conditioning', 'Bluetooth', 'Backup Camera', 'Cruise Control']
        self.info = 'Excellent condition, no accidents'
        self.price = '$15,000'
        self.location = 'New York, NY'
        self.cartype = 'Sedan'
        self.dealer_ID = '123456'

        self.create_widgets()
    
    def create_widgets(self):
        # Create widgets to display and edit car information
        # self.img_label = tk.Label(self, image=self.img)
        self.brand_label = tk.Label(self, text='Brand:')
        self.brand_entry = tk.Entry(self)
        self.brand_entry.insert(0, self.brand)
        self.release_year_label = tk.Label(self, text='Release Year:')
        self.release_year_entry = tk.Entry(self)
        self.release_year_entry.insert(0, self.release_year)
        self.seats_label = tk.Label(self, text='Seats:')
        self.seats_entry = tk.Entry(self)
        self.seats_entry.insert(0, self.seats)
        self.doors_label = tk.Label(self, text='Doors:')
        self.doors_entry = tk.Entry(self)
        self.doors_entry.insert(0, self.doors)
        self.gear_type_label = tk.Label(self, text='Gear Type:')
        self.gear_type_entry = tk.Entry(self)
        self.gear_type_entry.insert(0, self.gear_type)
        self.fuel_type_label = tk.Label(self, text='Fuel Type:')
        self.fuel_type_entry = tk.Entry(self)
        self.fuel_type_entry.insert(0, self.fuel_type)
        self.distance_label = tk.Label(self, text='Distance:')
        self.distance_entry = tk.Entry(self)
        self.distance_entry.insert(0, self.distance)
        self.gps_type_label = tk.Label(self, text='GPS Type:')
        self.gps_type_entry = tk.Entry(self)
        self.gps_type_entry.insert(0, self.gps_type)
        self.color_label = tk.Label(self, text='Color:')
        self.color_entry = tk.Entry(self)
        self.color_entry.insert(0, self.color)
        self.features_label = tk.Label(self, text='Features:')
        self.features_entry = tk.Entry(self)
        self.features_entry.insert(0, ', '.join(self.features))
        self.info_label = tk.Label(self, text='Info:')
        self.info_entry = tk.Entry(self)
        self.info_entry.insert(0, self.info)
        self.price_label = tk.Label(self, text='Price:')
        self.price_entry = tk.Entry(self)
        self.price_entry.insert(0, self.price)
        self.location_label = tk.Label(self, text='Location:')
        self.location_entry = tk.Entry(self)
        self.location_entry.insert(0, self.location)
        self.cartype_label = tk.Label(self, text='Car Type:')
        self.cartype_entry = tk.Entry(self)
        self.cartype_entry.insert(0, self.cartype)
        self.dealer_ID_label = tk.Label(self, text='Dealer ID:')
        self.dealer_ID_entry = tk.Entry(self)
        self.dealer_ID_entry.insert(0, self.dealer_ID)

        # Add widgets to the layout grid
        # self.img_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # self.brand_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        # self.brand_entry.grid(row=1, column=1, sticky='e', padx=10, pady=5)
        # self.release_year_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        # self.release_year_entry.grid(row=2, column=1, sticky='e', padx=10, pady=5)
        # self.seats_label.grid(row=3, column=0, sticky='w', padx=10, pady=5)
        # self.seats_entry.grid(row=3, column=1, sticky='e', padx=10, pady=5)
        # self.doors_label.grid(row=4, column=0, sticky='w', padx=10, pady=5)
        # self.doors_entry.grid(row=4, column=1, sticky='e', padx=10, pady=5)
        # self.gear_type_label.grid(row=5, column=0, sticky='w', padx=10, pady=5)
        # self.gear_type_entry.grid(row=5, column=1, sticky='e', padx=10, pady=5)
        # self.fuel_type_label.grid(row=6, column=0, sticky='w', padx=10, pady=5)
        # self.fuel_type_entry.grid(row=6, column=1, sticky='e', padx=10, pady=5)
        # self.distance_label.grid(row=7, column=0, sticky='w', padx=10, pady=5)
        # self.distance_entry.grid(row=7, column=1, sticky='e', padx=10, pady=5)
        # self.gps_type_label.grid(row=8, column=0, sticky='w', padx=10, pady=5)
        # self.gps_type_entry.grid(row=8, column=1, sticky='e', padx=10, pady=5)
        # self.color_label.grid(row=9, column=0, sticky='w', padx=10, pady=5)
        # self.color_entry.grid(row=9, column=1, sticky='e', padx=10, pady=5)
        # self.features_label.grid(row=10, column=0, sticky='w', padx=10, pady=5)
        # self.features_entry.grid(row=10, column=1, sticky='e', padx=10, pady=5)
        # self.info_label.grid(row=11, column=0, sticky='w', padx=10, pady=5)
        # self.info_entry.grid(row=11, column=1, sticky='e', padx=10, pady=5)
        # self.price_label.grid(row=12, column=0, sticky='w', padx=10, pady=5)
        # self.price_entry.grid(row=12, column=1, sticky='e', padx=10, pady=5)
        # self.location_label.grid(row=13, column=0, sticky='w', padx=10, pady=5)
        # self.location_entry.grid(row=13, column=1, sticky='e', padx=10, pady=5)
        # self.cartype_label.grid(row=14, column=0, sticky='w', padx=10, pady=5)
        # self.cartype_entry.grid(row=14, column=1, sticky='e', padx=10, pady=5)
        # self.dealer_ID_label.grid(row=15, column=0, sticky='w', padx=10, pady=5)
        # self.dealer_ID_entry.grid(row=15, column=1, sticky='e', padx=10, pady=5)

        # Create a button to save changes
        self.save_button = tk.Button(self, text='Submit', command=self.save_changes)
        # self.save_button.grid(row=16, column=1, sticky='e', padx=10, pady=20)


    def save_changes(self):
        """
        Save changes made to the car information.
        """
        # Update the car information with the values in the text fields
        self.brand = self.brand_entry.get()
        self.release_year = int(self.release_year_entry.get())
        self.seats = int(self.seats_entry.get())
        self.doors = int(self.doors_entry.get())
        self.gear_type = self.gear_type_entry.get()
        self.fuel_type = self.fuel_type_entry.get()
        self.distance = float(self.distance_entry.get())
        self.gps_type = self.gps_type_entry.get()
        self.color = self.color_entry.get()
        self.features = self.features_entry.get()
        self.info = self.info_entry.get()
        self.price = float(self.price_entry.get())
        self.location = self.location_entry.get()
        self.cartype = self.cartype_entry.get()
        self.dealer_ID = self.dealer_ID_entry.get()

        # Update the GUI labels with the new values
        self.brand_label.config(text='Brand: ' + self.brand)
        self.release_year_label.config(text='Release year: ' + str(self.release_year))
        self.seats_label.config(text='Seats: ' + str(self.seats))
        self.doors_label.config(text='Doors: ' + str(self.doors))
        self.gear_type_label.config(text='Gear type: ' + self.gear_type)
        self.fuel_type_label.config(text='Fuel type: ' + self.fuel_type)
        self.distance_label.config(text='Distance: ' + str(self.distance) )
        self.gps_type_label.config(text='GPS type: ' + self.gps_type)
        self.color_label.config(text='Color: ' + self.color)
        self.features_label.config(text='Features: ' + self.features)
        self.info_label.config(text='Info: ' + self.info)
        self.price_label.config(text='Price: ' + str(self.price))
        self.location_label.config(text='Location: ' + self.location)
        self.cartype_label.config(text='Car type: ' + self.cartype)
        self.dealer_ID_label.config(text='Dealer ID: ' + self.dealer_ID)

    def show(self):
        self.brand_label.pack()
        self.brand_entry.pack()
        self.release_year_label.pack()
        self.release_year_entry.pack()
        self.seats_label.pack()
        self.seats_entry.pack()
        self.doors_label.pack()
        self.doors_entry.pack()
        self.gear_type_label.pack()
        self.gear_type_entry.pack()
        self.fuel_type_label.pack()
        self.fuel_type_entry.pack()
        self.distance_label.pack()
        self.distance_entry.pack()
        self.gps_type_label.pack()
        self.gps_type_entry.pack()
        self.color_label.pack()
        self.color_entry.pack()
        self.features_label.pack()
        self.features_entry.pack()
        self.info_label.pack()
        self.info_entry.pack()
        self.price_label.pack()
        self.price_entry.pack()
        self.location_label.pack()
        self.location_entry.pack()
        self.cartype_label.pack()
        self.cartype_entry.pack()
        self.dealer_ID_label.pack()
        self.dealer_ID_entry.pack()

    def hide(self):
        self.brand_label.grid_forget()
        self.brand_entry.grid_forget()
        self.release_year_label.grid_forget()
        self.release_year_entry.grid_forget()
        self.seats_label.grid_forget()
        self.seats_entry.grid_forget()
        self.doors_label.grid_forget()
        self.doors_entry.grid_forget()
        self.gear_type_label.grid_forget()
        self.gear_type_entry.grid_forget()
        self.fuel_type_label.grid_forget()
        self.fuel_type_entry.grid_forget()
        self.distance_label.grid_forget()
        self.distance_entry.grid_forget()
        self.gps_type_label.grid_forget()
        self.gps_type_entry.grid_forget()
        self.color_label.grid_forget()
        self.color_entry.grid_forget()
        self.features_label.grid_forget()
        self.features_entry.grid_forget()
        self.info_label.grid_forget()
        self.info_entry.grid_forget()
        self.price_label.grid_forget()
        self.price_entry.grid_forget()
        self.location_label.grid_forget()
        self.location_entry.grid_forget()
        self.cartype_label.grid_forget()
        self.cartype_entry.grid_forget()
        self.dealer_ID_label.grid_forget()
        self.dealer_ID_entry.grid_forget()

# root = tk.Tk()
# root.geometry('500x600')
# root.title('Car Page')
# car_page = PostCarPage(root)
# car_page.pack(fill='both', expand=True)
# root.mainloop()