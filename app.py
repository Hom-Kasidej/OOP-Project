from tkinter import *
from tkinter import ttk
import requests
import tkinter.font as tkFont


class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self) 
        self.container = Frame(self)
        self.container.pack(fill=BOTH,expand=YES)
        self.container.config()
        
        self.frame = StartPage(self.container,self)
        self.frame.pack(fill=BOTH,expand=YES)

    def change_frame(self,frame):
        self.frame.destroy()
        self.frame = frame(self.container,self)
        self.frame.pack(fill=BOTH,expand=YES)
class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        container.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas =Canvas(container)
        self.scrollbar = Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side='left',fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
class StartPage(Frame):
    api_endpoint = "http://127.0.0.1:8000/"
    logout_endpoint = "http://127.0.0.1:8000/logout"

    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.response = requests.get(self.api_endpoint)

        top_bar_frame = Frame(self,bg='pink')
        top_bar_frame.pack(side=TOP,fill=X)
        if self.response.ok:
            #top bar frame elements
            self.label = Label(top_bar_frame,text="This is the starting page. Welcome! " + self.response.json()['data'])
            self.label.pack(side=LEFT,anchor=W)
            self.login_button = Button(top_bar_frame,text="Log in",command=lambda:controller.change_frame(LoginPage))
            self.login_button.pack(side=RIGHT)
            self.register_button = Button(top_bar_frame,text="Register",command=lambda:controller.change_frame(RegisterPage))
            self.register_button.pack(side=RIGHT)
            '''
            self.canvas = Canvas(self)
            self.scrollbar = Scrollbar(self,orient=VERTICAL,command=self.canvas.yview)
            self.scrollable_frame = Frame(self.canvas)
            self.scrollable_frame.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
            self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
            self.canvas.configure(yscrollcommand=self.scrollbar.set)
            self.canvas.pack(side="left", fill="both", expand=True)
            self.scrollbar.pack(side="right", fill="y")
            '''
            
            #scrollable frame
            
            self.main_frame = Frame(self,bg='gray')
            self.main_frame.pack(fill=BOTH,expand=YES)
            
            '''
            for i in range(50):
                Label(self.main_frame.scrollable_frame, text=f"Sample scrolling label{i}").pack()

            '''  
            drivemate_logo = Label(self.main_frame,text = "DRIVEMATE",font = 100,bg ="yellow",fg ="red")
            drivemate_logo.pack()

            self.searchbar_frame = Frame(self.main_frame,bg='cyan')
            self.searchbar_frame.pack(side=TOP,fill=X,expand=YES)
            

            myLabel2 = Label(self.searchbar_frame,text = "จาก :",font = 50)
            myLabel2.pack(side=LEFT,expand=YES,fill=X)
            cbo_day_pickup = ttk.Combobox(self.searchbar_frame, values = list(range(1,32)), width = 3, state="readonly")
            cbo_day_pickup.current(0)
            cbo_day_pickup.pack(side=LEFT,expand=YES,fill=X)
            cbo_month_pickup = ttk.Combobox(self.searchbar_frame, values = list(range(1,13)), width = 4,state = "readonly")
            cbo_month_pickup.current(1)
            cbo_month_pickup.pack(side=LEFT,expand=YES,fill=X)
            cbo_year_pickup = ttk.Combobox(self.searchbar_frame, values = list(range(2023,2100)), width = 5)
            cbo_year_pickup.current(1)
            cbo_year_pickup.pack(side=LEFT,expand=YES,fill=X)

            myLabel3 = Label(self.searchbar_frame,text = "เวลา :",font = 50)
            myLabel3.pack(side=LEFT,expand=YES,fill=X)
            cbo_hour_pickup = ttk.Combobox(self.searchbar_frame, values = list(range(1,25)),width = 2,state = "readonly")
            cbo_hour_pickup.current(1)
            cbo_hour_pickup.pack(side=LEFT,expand=YES,fill=X)
            cbo_minute_pickup = ttk.Combobox(self.searchbar_frame, values = list(range(0,61)),width = 2,state = "readonly")
            cbo_minute_pickup.current(1)
            cbo_minute_pickup.pack(side=LEFT,expand=YES,fill=X)

           

            myLabel4 = Label(self.searchbar_frame,text = "จนกระทั่ง :",font = 50)
            myLabel4.pack(side=LEFT,expand=YES,fill=X)
            cbo_day_return = ttk.Combobox(self.searchbar_frame, values = list(range(1,32)), width = 3, state="readonly")
            cbo_day_return.current(0)
            cbo_day_return.pack(side=LEFT,expand=YES,fill=X)
    
            cbo_month_return = ttk.Combobox(self.searchbar_frame, values = list(range(1,13)), width = 4,state = "readonly")
            cbo_month_return.current(1)
            cbo_month_return.pack(side=LEFT,expand=YES,fill=X)
    
            cbo_year_return = ttk.Combobox(self.searchbar_frame, values = list(range(2023,2100)), width = 5)
            cbo_year_return.current(1)
            cbo_year_return.pack(side=LEFT,expand=YES,fill=X)
            myLabel5 = Label(self.searchbar_frame,text = "เวลา :",font = 50)
            myLabel5.pack(side=LEFT,expand=YES,fill=X)
            cbo_hour_return = ttk.Combobox(self.searchbar_frame, values = list(range(1,25)),width = 2,state = "readonly")
            cbo_hour_return.current(1)
            cbo_hour_return.pack(side=LEFT,expand=YES,fill=X)
    
            cbo_minute_return = ttk.Combobox(self.searchbar_frame, values = list(range(0,61)),width = 2,state = "readonly")
            cbo_minute_return.current(1)
            cbo_minute_return.pack(side=LEFT,expand=YES,fill=X)

            provinces = {"Amnat Charoen", "Ang Thong", "Bangkok", "Bueng Kan", "Buri Ram", "Chachoengsao", "Chai Nat", "Chaiyaphum", "Chanthaburi", "Chiang Mai", "Chiang Rai", "Chon Buri", "Chumphon", "Kalasin", "Kamphaeng Phet", "Kanchanaburi", "Khon Kaen", "Krabi", "Lampang", "Lamphun", "Loei", "Lopburi", "Mae Hong Son", "Maha Sarakham", "Mukdahan", "Nakhon Nayok", "Nakhon Pathom", "Nakhon Phanom", "Nakhon Ratchasima", "Nakhon Sawan", "Nakhon Si Thammarat", "Nan", "Narathiwat", "Nong Bua Lamphu", "Nong Khai", "Nonthaburi", "Pathum Thani", "Pattani", "Phang Nga", "Phatthalung", "Phayao", "Phetchabun", "Phetchaburi", "Phichit", "Phitsanulok", "Phra Nakhon Si Ayutthaya", "Phrae", "Phuket", "Prachinburi", "Prachuap Khiri Khan", "Ranong", "Ratchaburi", "Rayong", "Roi Et", "Sa Kaeo", "Sakon Nakhon", "Samut Prakan", "Samut Sakhon", "Samut Songkhram", "Saraburi", "Satun", "Sing Buri", "Sisaket", "Songkhla", "Sukhothai", "Suphan Buri", "Surat Thani", "Surin", "Tak", "Trang", "Trat", "Ubon Ratchathani", "Udon Thani", "Uthai Thani", "Uttaradit", "Yala", "Yasothon"}
            tv_string = StringVar()

            selectedOpt = StringVar()
            selectedOpt.set('Bangkok')
    
            om = OptionMenu(self.searchbar_frame, selectedOpt, *provinces)
            om.config(width = 20)
            om.pack(side=LEFT,expand=YES,fill=X)
    
            btn = Button(self.searchbar_frame, text ="Search")
            btn.pack(side=LEFT,expand=YES,fill=X)
            btn.bind("<Button-1>")
            
        if self.response.json()['data'] != 'Guest':
            self.login_button.pack_forget()
            self.register_button.pack_forget()
            self.logout_button = Button(top_bar_frame,text="Log out",command=self.logout_click)
            self.logout_button.pack(side=RIGHT)
    def logout_click(self):
        new_response = requests.get(self.logout_endpoint)
        self.login_button.pack(side=RIGHT)
        self.register_button.pack(side=RIGHT)
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