import tkinter as tk

class ProfilePage:
    def __init__(self, name, email, switch_callback):
        self.name = name
        self.email = email
        self.switch_callback = switch_callback
        self.create_widgets()

    def create_widgets(self):
        # Create the profile page frame
        self.profile_frame = tk.Frame(width=400, height=400)
        self.profile_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create the widgets for the profile page frame
        profile_label = tk.Label(self.profile_frame, text="Profile")
        profile_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        name_label = tk.Label(self.profile_frame, text="Name: {}".format(self.name))
        name_label.grid(row=1, column=0, padx=10, pady=10)
        email_label = tk.Label(self.profile_frame, text="Email: {}".format(self.email))
        email_label.grid(row=2, column=0, padx=10, pady=10)
        switch_to_login_button = tk.Button(self.profile_frame, text="Log out", command=self.switch_callback)
        switch_to_login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def show(self):
        self.profile_frame.pack()

    def hide(self):
        self.profile_frame.pack_forget()
