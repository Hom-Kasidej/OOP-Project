import tkinter as tk

class LoginForm:
    def __init__(self, login_callback, signup_callback):
        self.login_callback = login_callback
        self.signup_callback = signup_callback
        self.create_widgets()

    def create_widgets(self):
        # Create the login form frame
        self.login_frame = tk.Frame(width=1200, height=900)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create the widgets for the login form frame
        login_label = tk.Label(self.login_frame, text="Login")
        login_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        email_label = tk.Label(self.login_frame, text="Email")
        email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self.login_frame)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)
        password_label = tk.Label(self.login_frame, text="Password")
        password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)
        login_button = tk.Button(self.login_frame, text="Log in", command=self.login)
        login_button.grid(row=3, column=0, padx=10, pady=10)
        signup_button = tk.Button(self.login_frame, text="Sign up", command=self.signup_callback)
        signup_button.grid(row=4, column=0, padx=10, pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.login_callback(email, password)

    def show(self):
        self.login_frame.pack()

    def hide(self):
        self.login_frame.pack_forget()
