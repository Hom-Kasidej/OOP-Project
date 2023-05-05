import tkinter as tk
from tkinter import ttk
import requests

class ProfilePage:
    def __init__(self,master, user, switch_callback, postcar_callback):
        self.master = master
        self.postcar_callback = postcar_callback
        self.user = user
        self.switch_callback = switch_callback
        self.canvas= tk.Canvas(
                self.master, borderwidth=2, relief="groove"
            )
        self.scrollbar = ttk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.create_widgets()

    def create_widgets(self):

        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        

        self.profile_label = tk.Label(self.scrollable_frame, text="Profile")

        self.name_label = tk.Label(self.scrollable_frame, text="Name: {}".format(self.user["_name"]))

        self.sex_label = tk.Label(self.scrollable_frame, text="Sex:")

        self.sex_var = tk.StringVar(value=self.user["_gender"])
        self.male_radio = tk.Radiobutton(self.scrollable_frame, text="Male", variable=self.sex_var, value="Male",state="disabled")

        self.female_radio = tk.Radiobutton(self.scrollable_frame, text="Female", variable=self.sex_var, value="Female",state="disabled")

        self.note_label = tk.Label(self.scrollable_frame, text="Note:")

        self.note_text = tk.Text(self.scrollable_frame, width=30, height=10)
        if self.user['_info']:
            self.note_text.insert('end',self.user['_info'])

        self.switch_to_login_button = tk.Button(self.scrollable_frame, text="Log out", command=self.switch_callback)

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

        self.post_car_button =  tk.Button(self.scrollable_frame, text="Post car", command=self.post_car)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def show(self):
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
        self.scrollbar.pack_forget()
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
    \
    def post_car(self):
        self.postcar_callback()
        pass

# root = tk.Tk()
# root.geometry('500x600')
# root.title('Car Page')
# profile_page = ProfilePage(root)
# profile_page.pack(fill='both', expand=True)
# root.mainloop()