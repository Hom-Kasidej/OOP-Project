from tkinter import *
from tkinter import ttk

def on_click(e):
    tv_string.set(f'you selected{selectedOpt.get()} ({provinces[selectedOpt.get()]})')

root = Tk()

root.title("Drivemate")

myLabel1 = Label(text = "DRIVEMATE",font = 100,bg ="yellow",fg ="red").pack()
myLabel2 = Label(text = "จาก :",font = 50).place(x = 160 , y = 30)
myLabel3 = Label(text = "เวลา :",font = 50).place(x = 190 , y = 55)
myLabel4 = Label(text = "จนกระทั่ง :",font = 50).place(x = 360 , y = 30)
myLabel5 = Label(text = "เวลา :",font = 50).place(x = 420 , y = 55)

provinces = {"Amnat Charoen", "Ang Thong", "Bangkok", "Bueng Kan", "Buri Ram", "Chachoengsao", "Chai Nat", "Chaiyaphum", "Chanthaburi", "Chiang Mai", "Chiang Rai", "Chon Buri", "Chumphon", "Kalasin", "Kamphaeng Phet", "Kanchanaburi", "Khon Kaen", "Krabi", "Lampang", "Lamphun", "Loei", "Lopburi", "Mae Hong Son", "Maha Sarakham", "Mukdahan", "Nakhon Nayok", "Nakhon Pathom", "Nakhon Phanom", "Nakhon Ratchasima", "Nakhon Sawan", "Nakhon Si Thammarat", "Nan", "Narathiwat", "Nong Bua Lamphu", "Nong Khai", "Nonthaburi", "Pathum Thani", "Pattani", "Phang Nga", "Phatthalung", "Phayao", "Phetchabun", "Phetchaburi", "Phichit", "Phitsanulok", "Phra Nakhon Si Ayutthaya", "Phrae", "Phuket", "Prachinburi", "Prachuap Khiri Khan", "Ranong", "Ratchaburi", "Rayong", "Roi Et", "Sa Kaeo", "Sakon Nakhon", "Samut Prakan", "Samut Sakhon", "Samut Songkhram", "Saraburi", "Satun", "Sing Buri", "Sisaket", "Songkhla", "Sukhothai", "Suphan Buri", "Surat Thani", "Surin", "Tak", "Trang", "Trat", "Ubon Ratchathani", "Udon Thani", "Uthai Thani", "Uttaradit", "Yala", "Yasothon"}
tv_string = StringVar()

selectedOpt = StringVar()
selectedOpt.set('Bangkok')

om = OptionMenu(root, selectedOpt, *provinces)
om.config(width = 20)
om.place(x = 700 , y = 30)


cbo_day_pickup = ttk.Combobox(root, values = list(range(1,32)), width = 3, state="readonly")
cbo_day_pickup.current(0)
cbo_day_pickup.place(x = 200 , y = 30)

cbo_month_pickup = ttk.Combobox(root, values = list(range(1,13)), width = 4,state = "readonly")
cbo_month_pickup.current(1)
cbo_month_pickup.place(x = 245, y = 30)

cbo_year_pickup = ttk.Combobox(root, values = list(range(2023,2100)), width = 5)
cbo_year_pickup.current(1)
cbo_year_pickup.place(x = 295 , y = 30)

cbo_hour_pickup = ttk.Combobox(root, values = list(range(1,25)),width = 2,state = "readonly")
cbo_hour_pickup.current(1)
cbo_hour_pickup.place(x = 230 , y = 55)

cbo_minute_pickup = ttk.Combobox(root, values = list(range(0,61)),width = 2,state = "readonly")
cbo_minute_pickup.current(1)
cbo_minute_pickup.place(x = 270 , y = 55)

cbo_day_return = ttk.Combobox(root, values = list(range(1,32)), width = 3, state="readonly")
cbo_day_return.current(0)
cbo_day_return.place(x = 430 , y = 30)

cbo_month_return = ttk.Combobox(root, values = list(range(1,13)), width = 4,state = "readonly")
cbo_month_return.current(1)
cbo_month_return.place(x = 475, y = 30)

cbo_year_return = ttk.Combobox(root, values = list(range(2023,2100)), width = 5)
cbo_year_return.current(1)
cbo_year_return.place(x = 525 , y = 30)

cbo_hour_return = ttk.Combobox(root, values = list(range(1,25)),width = 2,state = "readonly")
cbo_hour_return.current(1)
cbo_hour_return.place(x = 460 , y = 55)

cbo_minute_return = ttk.Combobox(root, values = list(range(0,61)),width = 2,state = "readonly")
cbo_minute_return.current(1)
cbo_minute_return.place(x = 500 , y = 55)

btn = Button(root, text ="search")
btn.place(x = 485, y = 80)
btn.bind("<Button-1>")


root.geometry("1024x720+200+50")

root.mainloop()