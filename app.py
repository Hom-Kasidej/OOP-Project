from tkinter import *
import requests
import tkinter.font as tkFont

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self) 
        self.container = Frame(self)
        self.container.pack(fill = "both", expand = True)
        self.frame = StartPage(self.container,self)
        self.frame.pack(fill='both')

    def change_frame(self,frame):
        self.frame.destroy()
        self.frame = frame(self.container,self)
        self.frame.pack(fill='both')

class StartPage(Frame):
    api_endpoint = "http://127.0.0.1:8000/"
    logout_endpoint = "http://127.0.0.1:8000/logout"

    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.response = requests.get(self.api_endpoint)
        if self.response.ok:
            self.label = Label(self,text="This is the starting page. Welcome! " + self.response.json()['data'])
            self.label.pack()
            self.login_button = Button(self,text="Log in",command=lambda:controller.change_frame(LoginPage))
            self.login_button.pack()
            self.register_button = Button(self,text="Register",command=lambda:controller.change_frame(RegisterPage))
            self.register_button.pack()
        if self.response.json()['data'] != 'Guest':
            self.login_button.pack_forget()
            self.register_button.pack_forget()
            self.logout_button = Button(self,text="Log out",command=self.logout_click)
            self.logout_button.pack()
    def logout_click(self):
        new_response = requests.get(self.logout_endpoint)
        self.login_button.pack()
        self.register_button.pack()
        self.logout_button.pack_forget()
        self.label.config(text="This is the starting page. Welcome! " +'Guest')


class LoginPage(Frame):
    api_endpoint = "http://127.0.0.1:8000/login"
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        self.username = StringVar()
        self.password = StringVar()

        self.label = Label(self,text="This is the login page.")
        self.label.pack()
        self.back_button = Button(self,text="Back",command=lambda:controller.change_frame(StartPage))
        self.back_button.pack()
        self.username_label = Label(self,text="Username:")
        self.username_label.pack()
        self.username_entry = Entry(self,textvariable=self.username, width=20, justify="left",bg='cyan')
        self.username_entry.pack()
        self.password_label = Label(self,text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(self,textvariable=self.password, width=20, justify="left",bg='cyan')
        self.password_entry.pack()
        self.login_button = Button(self,text="Login",command= lambda : self.login_click(controller))
        self.login_button.pack()
    def login_click(self,controller):
        payload = {'username' : self.username.get(),
                    'password' : self.password.get()}
        response = requests.get(self.api_endpoint,params=payload)
        if response.ok:
            message = Label(self, text=response.json()['data'])
            message.pack()
            controller.after(2000,lambda:controller.change_frame(StartPage))
            #controller.change_frame(StartPage)
            
        else:
            message = Label(self, text="Login Failed!")
            message.pack()

class RegisterPage(Frame):
    api_endpoint = "http://127.0.0.1:8000/register"
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        self.name = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.check_box = StringVar()
    

        self.label = Label(self,text="This is the register page.")
        self.label.pack()
        self.back_button = Button(self,text="Back",command=lambda:controller.change_frame(StartPage))
        self.back_button.pack()
        self.name_label = Label(self,text="Name:")
        self.name_label.pack()
        self.name_entry = Entry(self,textvariable=self.name, width=20, justify="left",bg='cyan')
        self.name_entry.pack()
        self.username_label = Label(self,text="Username:")
        self.username_label.pack()
        self.username_entry = Entry(self,textvariable=self.username, width=20, justify="left",bg='cyan')
        self.username_entry.pack()
        self.password_label = Label(self,text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(self,textvariable=self.password, width=20, justify="left",bg='cyan')
        self.password_entry.pack()
        self.check_box_renter = Checkbutton(self,text="Renter",variable=self.check_box,onvalue="Renter")
        self.check_box_renter.deselect()
        self.check_box_renter.pack()
        self.check_box_dealer = Checkbutton(self,text="Dealer",variable=self.check_box,onvalue="Dealer")
        self.check_box_dealer.deselect()
        self.check_box_dealer.pack()
        self.register_button = Button(self,text="Register",command= lambda : self.register_click(controller))
        self.register_button.pack()
    def register_click(self,controller):
        payload = { 'name' : self.name.get(),
                    'username' : self.username.get(),
                    'password' : self.password.get(),
                    'user_role' : self.check_box.get()}
        response = requests.post(self.api_endpoint,json=payload)
        if response.ok:
            print('yes')
            message = Label(self, text=response.json()['message'])
            message.pack()
            #controller.change_frame(StartPage)


if __name__ == "__main__":
    app = MainApp()
    app.geometry("1280x720")
    app.mainloop()