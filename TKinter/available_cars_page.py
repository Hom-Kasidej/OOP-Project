import tkinter as tk
from tkinter import ttk
from my_package.car_frame import RenterCarFrame, DealerCarFrame

class AvailableCarPage():
    def __init__(self, master, car_info_list,select_callback,user_status,login_callback):
        self.select_callback = select_callback
        self.master = master
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self.master, borderwidth=2, relief="groove")
        self.scrollbar = tk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        
        # Configure canvas to use scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Create a frame to hold the car frames
        self.scrollable_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Create a CarFrame for each car and store it in a list
        self.car_frames = []
        for car in car_info_list:
            car_frame = RenterCarFrame(
                self.scrollable_frame,
                car["_Car__brand"],
                car["_Car__color"],
                car["_Car__type"],
                car["_Car__distance"],
                car["_Car__gear_type"],
                car["_Car__gps_type"],
                car["_Car__fuel_type"],
                car["_Car__seats"],
                car["_Car__price"],
                car["_Car__car_ID"],
                self.select_callback,
                user_status,
                login_callback
            )
            self.car_frames.append(car_frame)
        
        # Resize the scrollable frame based on the number of car frames
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    
    def show(self):
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        for car_frame in self.car_frames:
            car_frame.show()

    def hide(self):
        self.scrollbar.pack_forget()
        self.canvas.pack_forget()
    
# root = tk.Tk()
# root.title("Login/Sign-up App")
# root.geometry("800x600")
# home = AvailableCarPage(root)
# root.mainloop()