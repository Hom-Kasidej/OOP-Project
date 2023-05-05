import tkinter as tk
from datetime import datetime
import requests


class PaymentForm:
    def __init__(self, master,rent_id,user_id,home_callback):
        self.home_callback = home_callback
        self.master = master
        self.user_id = user_id
        self.rent_id = rent_id
        self.master.title("Payment Form")
        self.master.geometry("800x600")
 
        self.payment_frame = tk.Frame(width=1200, height=900)
        self.payment_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create payment type selection
        self.payment_type_label = tk.Label(self.payment_frame , text="Select Payment Type:")

        self.payment_type = tk.StringVar()
        self.payment_type.set("Cash")

        self.cash_radio_button = tk.Radiobutton(self.payment_frame , text="Cash", variable=self.payment_type, value="Cash", command=self.show_cash_payment)

        self.credit_card_radio_button = tk.Radiobutton(self.payment_frame , text="Credit Card", variable=self.payment_type, value="Credit Card", command=self.show_credit_card_payment)

        # Create cash payment fields
        self.cash_frame = tk.Frame(self.payment_frame )

        self.cash_type_label = tk.Label(self.cash_frame, text="Cash Type:")

        self.cash_type_options = ["Cash", "Bank", "Promptpay"]
        self.cash_type = tk.StringVar()
        self.cash_type.set(self.cash_type_options[0])
        self.cash_type_dropdown = tk.OptionMenu(self.cash_frame, self.cash_type, *self.cash_type_options)

        self.cash_date_label = tk.Label(self.cash_frame, text="Date:")

        self.cash_date = tk.Entry(self.cash_frame)
        self.cash_date.insert(tk.END, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Create credit card payment fields
        self.credit_card_frame = tk.Frame(self.payment_frame)

        self.card_type_label = tk.Label(self.credit_card_frame, text="Card Type:")

        self.card_type_options = ["Visa", "MasterCard", "ETC."]
        self.card_type = tk.StringVar()
        self.card_type.set(self.card_type_options[0])
        self.card_type_dropdown = tk.OptionMenu(self.credit_card_frame, self.card_type, *self.card_type_options)

        self.card_number_label = tk.Label(self.credit_card_frame, text="Card Number:")

        self.card_number = tk.Entry(self.credit_card_frame)

        self.card_name_label = tk.Label(self.credit_card_frame, text="Card Name:")

        self.card_name = tk.Entry(self.credit_card_frame)

        self.card_expire_label = tk.Label(self.credit_card_frame, text="Card Expire:")

        self.card_expire = tk.Entry(self.credit_card_frame)

        self.card_cvc_label = tk.Label(self.credit_card_frame, text="Card CVC:")

        self.card_cvc = tk.Entry(self.credit_card_frame)

        self.card_date_label = tk.Label(self.credit_card_frame, text="Date:")

        self.card_date = tk.Entry(self.credit_card_frame)
        self.card_date.insert(tk.END, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Create submit button
        self.submit_button = tk.Button(self.payment_frame, text="Submit", command=self.submit_payment)

        # Show the cash payment fields by default
        self.show_cash_payment()

    def show_cash_payment(self):
        self.credit_card_frame.pack_forget()
        self.cash_frame.pack()

    def show_credit_card_payment(self):
        self.cash_frame.pack_forget()
        self.credit_card_frame.pack()

    def submit_payment(self):
        if self.payment_type.get() == "Cash":
            # Get the values from the Cash Payment inputs
            cash_type = self.cash_type.get()
            payment_date = self.cash_date.get()
            payload = { "payment_type" : 0,
                        "cash_type" : cash_type,
                        "date" : payment_date}
            api_endpoint = f'http://localhost:8000/Rents/{self.rent_id}/Payment'
            response = requests.post(api_endpoint, json=payload)
            if response.ok:
            # Do something with the Cash Payment data
                print(response.json())
                data_dict = response.json()
                payment_id = data_dict["Payment"]["_payment_no"]
                print(payment_id)
                # http://localhost:8000/Payments/1/PaymentProcess?status=Success
                api_endpoint2 = f'http://localhost:8000/Payments/{payment_id}/PaymentProcess?status=Success'
                response2 = requests.post(api_endpoint2)
                if response2.ok:
                    print(response2.json())
                    # http://localhost:8000/Rents/3/RentProcess?user_id=5
                    api_endpoint3 = f'http://localhost:8000/Rents/{self.rent_id}/RentProcess?user_id={self.user_id}'
                    response3 = requests.post(api_endpoint3)
                    if response3.ok:
                        print(response3.json())
                        self.home_callback()

        elif self.payment_type.get() == "Credit Card":
            # Get the values from the Credit Card Payment inputs
            payment_date = self.card_date.get()
            payload = {
                'rent_id' : self.rent_id,
                'payment_type' : 1,
                'card_type' : self.card_type.get(),
                'card_number' : self.card_number.get(),
                'card_name' : self.card_name.get(),
                'card_exp' : self.card_expire.get(),
                'card_CVC' : self.card_cvc.get(),
                'date' : payment_date
            }
            api_endpoint = f'http://localhost:8000/Rents/{self.rent_id}/Payment'
            response = requests.post(api_endpoint, json=payload)
            if response.ok:

            # Do something with the Credit Card Payment data
                print(response.json())
                data_dict = response.json()
                payment_id = data_dict["Payment"]["_payment_no"]
                print(payment_id)
                api_endpoint2 = f'http://localhost:8000/Payments/{payment_id}/PaymentProcess?status=Success'
                response2 = requests.post(api_endpoint2)
                if response2.ok:
                    print(response2.json())
                    api_endpoint3 = f'http://localhost:8000/Rents/{self.rent_id}/RentProcess?user_id={self.user_id}'
                    response3 = requests.post(api_endpoint3)
                    if response3.ok:
                        print(response3.json())
                        self.home_callback()
                        
    def show(self):
        self.payment_frame.pack(padx= 10,pady=5)
        self.payment_type_label.pack(padx= 10,pady=5)
        self.cash_radio_button.pack(padx= 10,pady=5)
        self.credit_card_radio_button.pack(padx= 10,pady=5)
        self.cash_frame.pack(padx= 10,pady=5)
        self.payment_frame.pack(padx= 10,pady=5)
        self.cash_type_label.pack(padx= 10,pady=5)
        self.cash_type_dropdown.pack(padx= 10,pady=5)
        self.cash_date_label.pack(padx= 10,pady=5)
        self.cash_date.pack(padx= 10,pady=5)
        self.card_type_label.pack(padx= 10,pady=5)
        self.card_type_dropdown.pack(padx= 10,pady=5)
        self.card_number_label.pack(padx= 10,pady=5)
        self.card_number.pack(padx= 10,pady=5)
        self.card_name_label.pack(padx= 10,pady=5)
        self.card_name.pack(padx= 10,pady=5)
        self.card_expire_label.pack(padx= 10,pady=5)
        self.card_expire.pack(padx= 10,pady=5)
        self.card_cvc_label.pack(padx= 10,pady=5)
        self.card_cvc.pack(padx= 10,pady=5)
        self.submit_button.pack(padx= 10,pady=5)

    def hide(self):
        self.payment_frame.pack_forget()
        self.payment_type_label.pack_forget()
        self.cash_radio_button.pack_forget()
        self.credit_card_radio_button.pack_forget()
        self.cash_frame.pack_forget()
        self.payment_frame.pack_forget()
        self.cash_type_label.pack_forget()
        self.cash_type_dropdown.pack_forget()
        self.cash_date_label.pack_forget()
        self.cash_date.pack_forget()
        self.card_type_label.pack_forget()
        self.card_type_dropdown.pack_forget()
        self.card_number_label.pack_forget()
        self.card_number.pack_forget()
        self.card_name_label.pack_forget()
        self.card_name.pack_forget()
        self.card_expire_label.pack_forget()
        self.card_expire.pack_forget()
        self.card_cvc_label.pack_forget()
        self.card_cvc.pack_forget()
        self.submit_button.pack_forget()