import tkinter as tk

class ProfilePage:
    def __init__(self,master, user, switch_callback):
        self.master = master
        self.user = user
        self.switch_callback = switch_callback
        self.create_widgets()
        self.show()
        self.hide()

    def create_widgets(self):
        # Create the widgets for the profile page frame
        self.profile_label = tk.Label(self.master, text="Profile")

        self.name_label = tk.Label(self.master, text="Name: {}".format(self.user["_name"]))

        self.sex_label = tk.Label(self.master, text="Sex:")

        self.sex_var = tk.StringVar(value=self.user["_gender"])
        self.male_radio = tk.Radiobutton(self.master, text="Male", variable=self.sex_var, value="Male")
        self.female_radio = tk.Radiobutton(self.master, text="Female", variable=self.sex_var, value="Female")

        self.note_label = tk.Label(self.master, text="Note:")

        self.note_text = tk.Text(self.master, width=30, height=10,state="disabled")
        if self.user['_info']:
            self.note_text.insert('end',self.user['_info'])


        self.switch_to_login_button = tk.Button(self.master, text="Log out", command=self.switch_callback)
    

    def show(self):
        self.profile_label.pack(padx=10, pady=10, anchor=tk.W)
        self.name_label.pack(padx=10, pady=10, anchor=tk.W)
        self.sex_label.pack(padx=10, pady=10, anchor=tk.W)
        self.male_radio.pack(padx=10, pady=10, anchor=tk.W)
        self.female_radio.pack(padx=10, pady=10, anchor=tk.W)
        self.note_label.pack(padx=10, pady=10, anchor=tk.W)
        self.note_text.pack(padx=10, pady=10, anchor=tk.W)
        self.switch_to_login_button.pack(padx=10, pady=10, anchor=tk.W)

    def hide(self):
        self.profile_label.pack_forget()
        self.name_label.pack_forget()
        self.sex_label.pack_forget()
        self.male_radio.pack_forget()
        self.female_radio.pack_forget()
        self.note_label.pack_forget()
        self.note_text.pack_forget()
        self.switch_to_login_button.pack_forget()

    def delete(self):
        self.delete


# root = tk.Tk()
# root.title("Login/Sign-up App")
# root.geometry("800x600")
# app = ProfilePage("test",None)
# root.mainloop()
