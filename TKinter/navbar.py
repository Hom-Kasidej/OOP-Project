import tkinter as tk

class NavigationBar(tk.Frame):
    def __init__(self, login_callback, master=None):
        super().__init__(master, height=50, bg="blue")
        self.login_callback = login_callback
        self.create_widgets()

    def create_widgets(self):
        self.logo_label = tk.Label(self, text="MyApp", font=("Arial", 20), bg="blue", fg="white")
        self.logo_label.pack(side="left", padx=10, pady=5)

        if self.login_callback is not None:
            self.login_button = tk.Button(self, text="Sign In", font=("Arial", 14), bg="blue", fg="white", bd=0,
                                          command=self.login_callback)
            self.login_button.pack(side="right", padx=10) 

    def show(self):
        self.pack(side="top", fill="x")

    def hide(self):
        self.pack_forget()

    def set_login_form_displayed(self, is_displayed):
        if is_displayed:
            self.login_button.pack_forget()
        else:
            self.login_button.pack(side="right", padx=10)

