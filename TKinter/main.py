import tkinter as tk
from login_form import LoginForm
from signup_form import SignupForm
from profile_page import ProfilePage
from navbar import NavigationBar

class Application:
    def __init__(self, master):
        self.master = master
        self.navbar = NavigationBar(self.show_login_form)
        self.navbar.show()

        self.show_login_form()

    def show_login_form(self):

        self.login_form = LoginForm(self.login_success_callback, self.show_signup_form)

        if hasattr(self, 'signup_form'):
            self.signup_form.hide()
        if hasattr(self, 'profile_page'):
            self.profile_page.hide()

        # Create and show the login form
        self.login_form.show()

        self.set_login_form_displayed(True)

    def show_signup_form(self):

        self.signup_form = SignupForm(self.show_login_form)
        if hasattr(self, 'login_form'):
            self.login_form.hide()
        if hasattr(self, 'profile_page'):
            self.profile_page.hide()


        self.signup_form.show()
        
        self.set_login_form_displayed(False)

    def login_success_callback(self, name, email):
        self.profile_page = ProfilePage(name, email, self.show_login_form)

        if hasattr(self, 'login_form'):
            self.login_form.hide()
        if hasattr(self, 'signup_form'):
            self.signup_form.hide()

        self.profile_page.show()

        self.set_login_form_displayed(False)

    def set_login_form_displayed(self, is_displayed):
        self.navbar.set_login_form_displayed(is_displayed)



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Login/Sign-up App")
    root.geometry("800x600")
    app = Application(root)
    root.mainloop()
