import tkinter as tk
import requests
import json

class LoginForm:
    api_endpoint = 'http://localhost:8000/User/Login/'
    def __init__(self,master,login_success_callback,sign_up_callback):
        self.master = master
        self.login_successs_callback = login_success_callback
        self.sign_up_callback = sign_up_callback
        self.create_widgets()
        self.user = None

    def create_widgets(self):
        # Create the widgets for the login form frame
        self.login_label = tk.Label(self.master, text="Login")

        self.username_label = tk.Label(self.master, text="Username")
        
        self.username_entry = tk.Entry(self.master)
        
        self.password_label = tk.Label(self.master, text="Password")
        
        self.password_entry = tk.Entry(self.master, show="*")
        
        self.login_button = tk.Button(self.master, text="Log in", command=self.login)
        
        self.signup_button = tk.Button(self.master,text="Sign up", command=self.sign_up_callback)

    def login(self):
        try:
            payload = {
                "username" : self.username_entry.get(),
                "password" : self.password_entry.get()
            }
        except:
            payload = None
            return
        print(payload)
        response = requests.post(self.api_endpoint, json=payload)
        dict_data = json.loads(response.text)
        print(dict_data)
        if dict_data['Message'] == 'Login Fail': 
            print("Login Fail!")
        else:
            print("Login SuccessFully ")
            self.hide()
            self.user = dict_data['user']
            # print(self.user)
            self.login_successs_callback(self.user)

    def show(self):
        self.login_label.pack(padx=10,pady=10)
        self.username_label.pack(padx=10,pady=10)
        self.username_entry.pack(padx=10,pady=10)
        self.password_label.pack(padx=10,pady=10)
        self.password_entry.pack(padx=10,pady=10)
        self.login_button.pack(padx=10,pady=10)
        self.signup_button.pack(padx=10,pady=10)

    def hide(self):
        self.login_label.pack_forget()
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.login_button.pack_forget()
        self.signup_button.pack_forget()

    def get_login_status(self):
        return self.status

# root = tk.Tk()
# root.title("Login/Sign-up App")
# root.geometry("800x600")
# app = LoginForm(root)
# root.mainloop()