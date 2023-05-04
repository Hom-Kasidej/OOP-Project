import tkinter as tk

class SignupForm:
    def __init__(self, switch_callback):
        self.switch_callback = switch_callback
        self.create_widgets()

    def create_widgets(self):
        # Create the sign-up frame
        self.signup_frame = tk.Frame(width=400, height=400)
        self.signup_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create the widgets for the sign-up frame
        signup_label = tk.Label(self.signup_frame, text="Sign-up")
        signup_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        username_label = tk.Label(self.signup_frame, text="Name:")
        username_label.grid(row=1, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.signup_frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)
        password_label = tk.Label(self.signup_frame, text="Password:")
        password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.signup_frame)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)
        confirm_password_label = tk.Label(self.signup_frame, text="Confirm Password:")
        confirm_password_label.grid(row=3, column=0, padx=10, pady=10)
        self.confirm_password_entry = tk.Entry(self.signup_frame)
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)
        signup_button = tk.Button(self.signup_frame, text="Sign-up", command=self.signup, width=20)
        signup_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20)
        switch_to_login_button = tk.Button(self.signup_frame, text="Switch to Login", command=self.switch_callback)
        switch_to_login_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def signup(self):
        # Sign-up logic here
        pass

    def show(self):
        self.signup_frame.pack()

    def hide(self):
        self.signup_frame.pack_forget()
