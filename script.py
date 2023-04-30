from tkinter import *
import requests
import tkinter.font as tkFont

API_ENDPOINT1 = "http://127.0.0.1:8000/login"

def login_click():
    payload = {'username' : username.get(),
               'password' : password.get()}
    response = requests.get(API_ENDPOINT1,params=payload)
    if response.ok:
       message = Label(root, text=response.json()['data'])
       message.place(x=100, y=150)
       message.after(5000,func=message.destroy)
    return 

#gui setup
root = Tk()
root.geometry("800x600")
root.option_add("*Font", "aerial 20 bold")

#setup
button_font = tkFont.Font(family = "Aerial",size = 20)
username = StringVar()
password = StringVar()

#loop
username_label = Label(root,text='Username:').place(x=0, y=0)
username_entry = Entry(root,textvariable=username, width=20, justify="left",bg='cyan').place(x=200, y=0)
password_label = Label(root,text='Password:').place(x=0, y=50)
password_entry = Entry(root,textvariable=password, width=20, justify="left",bg='cyan').place(x=200, y=50)

login_button = Button(root, text="Login", bg="green", command=login_click, height=1 , width=5,font=button_font).place(x=100, y=100)
root.mainloop()