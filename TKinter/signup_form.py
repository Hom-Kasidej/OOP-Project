import tkinter as tk
from tkinter import messagebox
import requests
class SignupForm:
    def __init__(self, switch_callback):
        self.switch_callback = switch_callback
        self.create_widgets()
        self.hide()

    def create_widgets(self):
        # Create the sign-up frame
        self.signup_frame = tk.Frame(width=400, height=400)
        # self.signup_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create the widgets for the sign-up frame
        signup_label = tk.Label(self.signup_frame, text="Sign-up")
        signup_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        firstname_label = tk.Label(self.signup_frame, text="First Name:")
        firstname_label.grid(row=1, column=0, padx=10, pady=10)

        self.firstname_entry = tk.Entry(self.signup_frame)
        self.firstname_entry.grid(row=1, column=1, padx=10, pady=10)

        lastname_label = tk.Label(self.signup_frame, text="Last Name:")
        lastname_label.grid(row=2, column=0, padx=10, pady=10)

        self.lastname_entry = tk.Entry(self.signup_frame)
        self.lastname_entry.grid(row=2, column=1, padx=10, pady=10)

        username_label = tk.Label(self.signup_frame, text="Username:")
        username_label.grid(row=3, column=0, padx=10, pady=10)

        self.username_entry = tk.Entry(self.signup_frame)
        self.username_entry.grid(row=3, column=1, padx=10, pady=10)

        password_label = tk.Label(self.signup_frame, text="Password:")
        password_label.grid(row=4, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(self.signup_frame)
        self.password_entry.grid(row=4, column=1, padx=10, pady=10)

        confirm_password_label = tk.Label(self.signup_frame, text="Confirm Password:")
        confirm_password_label.grid(row=5, column=0, padx=10, pady=10)

        self.confirm_password_entry = tk.Entry(self.signup_frame)
        self.confirm_password_entry.grid(row=5, column=1, padx=10, pady=10)

        account_type_label = tk.Label(self.signup_frame , text="Select Account Type:")
        account_type_label.grid(row=6, column=0, padx=10, pady=10)

        self.account_type = tk.StringVar()
        self.account_type.set("R")

        renter_radio_button = tk.Radiobutton(self.signup_frame , text="Renter", variable=self.account_type, value="R")
        renter_radio_button.grid(row=6, column=1, padx=10, pady=10)

        dealer_radio_button = tk.Radiobutton(self.signup_frame, text="Dealer", variable=self.account_type, value="D")
        dealer_radio_button.grid(row=6, column=2, padx=10, pady=10)

        signup_button = tk.Button(self.signup_frame, text="Sign-up", command=self.signup, width=20)
        signup_button.grid(row=7, column=0, columnspan=2, padx=10, pady=20)
        
        switch_to_login_button = tk.Button(self.signup_frame, text="Switch to Login", command=self.switch_callback)
        switch_to_login_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def signup(self):
        print("signup!")
        api_endpoint = 'http://localhost:8000/User/Register/'
        payload = {
            "firstname" : self.firstname_entry.get(),
            "lastname" : self.lastname_entry.get(),
            "username" : self.username_entry.get(),
            "password" : self.password_entry.get(),
            "confirm_password" : self.confirm_password_entry.get(),
            "account_type" : self.account_type.get()

        }
        print(payload)
        response = requests.post(api_endpoint,json=payload)
        if response.ok:
            messagebox.showinfo("Register", "Registered!")
            print(response.json())
        else:
            messagebox.showerror("Register", "Error!")
            print("Can not")

    def show(self):
        self.signup_frame.pack()

    def hide(self):
        self.signup_frame.pack_forget()

# root = tk.Tk()
# root.title("Login/Sign-up App")
# root.geometry("800x600")
# app = SignupForm(root)
# app.show()
# root.mainloop()
