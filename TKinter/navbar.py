import tkinter as tk

class NavigationBar:
    def __init__(self, master,login_callback,logout_callback,home_callback,profile_callback):
        self.login_callback = login_callback
        self.logout_callback = logout_callback
        self.home_callback = home_callback
        self.profile_callback = profile_callback
    
        self.master = master
        self.state = True

        # Create a Frame for the navigation bar
        self.navbar_frame = tk.Frame(self.master, bg="blue")
        self.navbar_frame.pack(side="top", fill="x")
        
        # Create a Label with the logo
        self.logo_label = tk.Label(self.navbar_frame, text="DRIVEMATE", font=("Arial", 16), padx=10, bg="Blue",fg="white")
        self.logo_label.pack(side="left")
        self.logo_label.bind("<Button-1>", self.home_callback)

        self.login_button = tk.Button(self.navbar_frame, text="Login", font=("Arial", 16), padx=10, bg="Blue", fg="white", command=self.login_callback)

        self.profile_button = tk.Button(self.navbar_frame, text="profile", font=("Arial", 16), padx=10, bg="Blue", fg="white", command=self.profile_callback)

        self.logout_button = tk.Button(self.navbar_frame, text="Logout", font=("Arial", 16), padx=10, bg="Blue", fg="white", command=self.logout_callback)
        
        self.username_label = tk.Label(self.navbar_frame, text="username_test", font=("Arial", 16), padx=10, bg="Blue", fg="white")

        self.show_login_button()
        self.show()
        
    def show(self):
        # Show the navigation bar
        self.navbar_frame.pack(side="top", fill="x")
        
    def hide(self):
        # Hide the navigation bar
        self.navbar_frame.pack_forget()

    def show_login_button(self):
        if self.state:
            self.login_button.pack(side="right")
            self.profile_button.pack_forget()
            self.username_label.pack_forget()
            # self.logout_button.pack_forget()
        else:
            self.login_button.pack_forget()
            self.profile_button.pack(side="right")
            # self.logout_button.pack(side="right")
            self.username_label.pack(side="right")

    def set_login_button_state(self, state):
        self.state = state

    def show_user_info(self, username):
        self.username_label.config(text=f"Welcome, {username}")
        self.show_login_button()


# root = tk.Tk()
# root.title("Login/Sign-up App")
# root.geometry("800x600")
# app = NavigationBar(root)
# app.show()
# root.mainloop()
