import tkinter as tk
from tkinter import messagebox
from settings import Settings as settings
from functions import LoginAndPasswordValidation
from database import PasswordDatabase

# I created interface to check and save login and password. For this I used the tkinter library.


class PasswordValidationInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Validation Login and Password")

        self.frame = tk.Frame(root, padx=30, pady=30)
        self.frame.pack()

        self.login_label = tk.Label(self.frame, text="Login")
        self.login_label.grid(row=0, column=0, sticky="e")

        self.login_entry = tk.Entry(self.frame)
        self.login_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.frame, text="Password")
        self.password_label.grid(row=1, column=0, sticky="e")

        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(
            self.frame, text="Save Password", command=self.build_functions
        )
        self.submit_button.grid(row=2, columnspan=2, pady=10)

        self.check_button = tk.Button(
            self.frame, text="Check Password", command=self.check_password
        )
        self.check_button.grid(row=2, column=2, pady=10)

    # If the password does not meet even one requirement, background "password" will turn red.
    # If password meet all requirements, background "password" will turn green.
    def check_password(self):
        password = self.password_entry.get()
        validation = LoginAndPasswordValidation("login", password)

        if validation.is_valid():
            self.password_entry.config(bg="green")
        else:
            self.password_entry.config(bg="red")

    def build_functions(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        validation = LoginAndPasswordValidation(login, password)

        if validation.is_valid():
            with PasswordDatabase(
                dbname=settings.dbname,
                user=settings.user,
                password=settings.password,
                host=settings.host,
                port=settings.port,
            ) as password_db:
                password_db.save_password_and_login_if_is_valid(login, password)
            messagebox.showinfo("Succes", " Password meets all the requirements! ")
        else:
            messagebox.showinfo(
                "Please, provide a diffrent login or password thats meets all the requiremenst!"
            )
