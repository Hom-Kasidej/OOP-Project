import tkinter as tk
from tkinter import ttk
import requests

class ProfilePage:
    def __init__(self,master, user, switch_callback, postcar_callback):
        self.master = master
        self.postcar_callback = postcar_callback
        self.user = user
        self.switch_callback = switch_callback
        self.canvas= tk.Frame(self.master)
        self.create_widgets()

    def create_widgets(self):
        self.profile_label = tk.Label(self.canvas, text="Profile")

        self.name_label = tk.Label(self.canvas, text="Name: {}".format(self.user["_name"]))

        self.sex_label = tk.Label(self.canvas, text="Sex:")

        self.sex_var = tk.StringVar(value=self.user["_gender"])
        self.male_radio = tk.Radiobutton(self.canvas, text="Male", variable=self.sex_var, value="Male",state="disabled")

        self.female_radio = tk.Radiobutton(self.canvas, text="Female", variable=self.sex_var, value="Female",state="disabled")

        self.note_label = tk.Label(self.canvas, text="Note:")

        self.note_text = tk.Text(self.canvas, width=30, height=10)
        if self.user['_info']:
            self.note_text.insert('end',self.user['_info'])

        self.switch_to_login_button = tk.Button(self.canvas, text="Log out", command=self.switch_callback)

        self.button_list = []

        self.cars = []
        api_endpoint = 'http://localhost:8000/Car'

        response = requests.get(api_endpoint)
        if response.ok:
            cars = response.json()
            car_list = cars['Cars']
            for car in car_list:
                if car['_Car__dealer_ID'] == self.user['_id']:
                    self.cars.append(car)

        num_car = len(self.cars)

        self.post_car_button =  tk.Button(self.canvas, text="Post car", command=self.post_car)

    def show(self):
        # self.scrollbar.pack(padx=10,pady=10,side="right",fill='y')
        self.canvas.pack(padx=10,pady=10,fill="x")
        self.profile_label.pack(padx=10,pady=10,anchor=tk.W)
        self.name_label.pack(padx=10,pady=10,anchor=tk.W)
        self.sex_label.pack(padx=10,pady=10,anchor=tk.W)
        self.male_radio.pack(padx=10,pady=10,anchor=tk.W)
        self.female_radio.pack(padx=10,pady=10,anchor=tk.W)
        self.note_label.pack(padx=10,pady=10,anchor=tk.W)
        self.note_text.pack(padx=10,pady=10,anchor=tk.W)
        self.switch_to_login_button.pack(padx=10,pady=10,anchor=tk.W)
        self.post_car_button.pack(padx=10,pady=10,anchor=tk.W)

    def hide(self):
        # self.scrollbar.pack_forget()
        self.canvas.pack_forget()
        self.profile_label.pack_forget()
        self.name_label.pack_forget()
        self.sex_label.pack_forget()
        self.male_radio.pack_forget()
        self.female_radio.pack_forget()
        self.note_label.pack_forget()
        self.note_text.pack_forget()
        self.switch_to_login_button.pack_forget()
        self.post_car_button.pack_forget()
    
    def post_car(self):
        self.postcar_callback()
        p

# root = tk.Tk()
# root.geometry('500x600')
# root.title('Car Page')
# profile_page = ProfilePage(root)
# profile_page.pack(fill='both', expand=True)
# root.mainloop()