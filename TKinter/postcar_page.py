import tkinter as tk
import requests
from tkinter import messagebox

class PostCarPage:
    def __init__(self, master, user):
        self.master = master
        self.user = user
        self.canvas = tk.Canvas(
                self.master, borderwidth=2, relief="groove"
            )
        self.scrollbar = tk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        
        self.scrollable_frame = tk.Frame(self.canvas)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        # Define car information
        # self.img = tk.PhotoImage(file='car.png')

        # Create widgets to display and edit car information
        # self.img_label = tk.Label(self, image=self.img)
        self.brand_label = tk.Label(self.scrollable_frame, text='Brand:')
        self.brand_entry = tk.Entry(self.scrollable_frame)
        self.release_year_label = tk.Label(self.scrollable_frame, text='Release Year:')
        self.release_year_entry = tk.Entry(self.scrollable_frame)
        self.seats_label = tk.Label(self.scrollable_frame, text='Seats:')
        self.seats_entry = tk.Entry(self.scrollable_frame)
        self.doors_label = tk.Label(self.scrollable_frame, text='Doors:')
        self.doors_entry = tk.Entry(self.scrollable_frame)
        self.gear_type_label = tk.Label(self.scrollable_frame, text='Gear Type:')
        self.gear_type_entry = tk.Entry(self.scrollable_frame)
        self.fuel_type_label = tk.Label(self.scrollable_frame, text='Fuel Type:')
        self.fuel_type_entry = tk.Entry(self.scrollable_frame)
        self.distance_label = tk.Label(self.scrollable_frame, text='Distance:')
        self.distance_entry = tk.Entry(self.scrollable_frame)
        self.gps_type_label = tk.Label(self.scrollable_frame, text='GPS Type:')
        self.gps_type_entry = tk.Entry(self.scrollable_frame)
        self.color_label = tk.Label(self.scrollable_frame, text='Color:')
        self.color_entry = tk.Entry(self.scrollable_frame)
        self.features_label = tk.Label(self.scrollable_frame, text='Features:')
        self.features_entry = tk.Entry(self.scrollable_frame)
        self.info_label = tk.Label(self.scrollable_frame, text='Info:')
        self.info_entry = tk.Entry(self.scrollable_frame)
        self.price_label = tk.Label(self.scrollable_frame, text='Price:')
        self.price_entry = tk.Entry(self.scrollable_frame)
        self.location_label = tk.Label(self.scrollable_frame, text='Location:')
        self.location_entry = tk.Entry(self.scrollable_frame)
        self.cartype_label = tk.Label(self.scrollable_frame, text='Car Type:')
        self.cartype_entry = tk.Entry(self.scrollable_frame)

        # Add widgets to the layout grid
        # self.img_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
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

        # Create a button to save changes
        self.save_button = tk.Button(self.scrollable_frame, text='Submit', command=self.save_changes)
        self.save_button.pack()

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        # Resize the scrollable frame based on the number of car frames
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    
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
        self.user_id = self.user['_id']
        
        # api_endpoint = f'http://localhost:8000/Post_car/?brand={self.brand}&gear_type={self.gear_type}&fuel_type={self.fuel_type}&gps_type={self.gps_type}&color={self.color}&cartype={self.cartype}&location={self.location}'
        api_endpoint = f'http://localhost:8000/Post_car/?brand={self.brand}&gear_type={self.gear_type}&fuel_type={self.fuel_type}&gps_type={self.gps_type}&color={self.color}&cartype={self.cartype}&location={self.location}&release_year={self.release_year}&seats={self.seats}&doors={self.doors}&distance={self.distance}&features={self.features}&info={self.info}&price={self.price}&dealer_id={self.user_id}'
        
        #payload = {
        #    "release_year" : self.release_year,
        #    "seats": self.seats, 
        #    "doors": self.doors,
        #    "distance": self.distance, 
        #    "features": self.features, 
        #    "info": self.info,
        #    "price": self.price,
        #    "dealer_ID": self.user['_id']
        #}

        response = requests.post(api_endpoint)
        if response.ok:
            print(response.json())
            messagebox.showinfo("Joo", "Post laew ja")
        else:
            print("Error")
            messagebox.showerror("xd", "You got hacked!")
        # Update the GUI labels with the new values

# cardict["release_year"]
# cardict["seats"]
# cardict["doors"]
# cardict["distance"]
# cardict["features"]
# cardict["info"]
# cardict["images"]
# cardict["price"]
# cardict["dealer_ID"]
        

    def show(self):
        self.canvas.pack(side="left", fill="both", expand=True)

    def hide(self):
        self.canvas.pack_forget()
