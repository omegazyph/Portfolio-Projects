########################################################
# Password Manager V 3.0
# created by Wayne Stock (omegazyph)
# created 2024-04-20
# This program is in tkinter to help with your passwords 
########################################################

import tkinter as tk
from cryptography.fernet import Fernet
import tkinter.messagebox
from tkinter import simpledialog

# Define the master password
MASTER_PASSWORD = "" # Put in the password you want

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager V3.0")
        self.geometry("400x300")  # Set the initial size of the window
        self.configure(background="#f0f0f0")  # Set background color
        self.fer = None  # Initialize Fernet instance attribute
        self.check_master_password()  # Check the master password

        # Load the Fernet instance
        self.load_fernet_instance()

        # Create widgets
        self.create_widgets()

    def check_master_password(self):
        # Prompt the user for the master password
        while True:
            master_pwd = simpledialog.askstring("Master Password", 
                                                "Enter the master password to access the program:")
            if master_pwd == MASTER_PASSWORD:
                break  # Correct master password, exit the loop
            elif master_pwd is None:
                self.destroy()  # User closed the dialog, close the program
                return
            else:
                tk.messagebox.showerror("Incorrect Password", "Incorrect master password. Please try again.")

    def load_fernet_instance(self):
        try:
            key = LoadKey.load_key()
            self.fer = Fernet(key)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"An error occurred while loading Fernet instance: {str(e)}")

    def create_widgets(self):
        # Create welcome label
        self.welcome_label = tk.Label(self, text="Welcome to Password Manager V3.0", 
                                      font=("Helvetica", 16), 
                                      bg="#f0f0f0", 
                                      fg="#333333")
        self.welcome_label.pack(pady=20)

        # Create buttons
        self.write_button = tk.Button(self, text="Create a Key", command=write.write_key)
        self.write_button.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self, text="Add a password", command=add.add)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.view_button = tk.Button(self, text="View Passwords")
        self.view_button.pack(side=tk.LEFT, padx=5)


class write:
    @staticmethod
    def write_key():
        try:
            # Display a warning message to confirm key creation
            result = tkinter.messagebox.askquestion("Create Key", "Are you sure you want to create a new key?")
            if result == "yes":
                # Generate a new key
                key = Fernet.generate_key()
                # Write the new key to a file
                with open("key.key", 'wb') as key_file:
                    key_file.write(key)
                # Display a success message
                tkinter.messagebox.showinfo("Key Created", "A new key has been successfully created.")
        except Exception as e:
            # Display an error message if an exception occurs
            tkinter.messagebox.showerror("Error", f"An error occurred: {str(e)}")


class LoadKey:
    @staticmethod
    def load_key():
        try:
            with open("key.key", 'rb') as file:
                key = file.read()
                return key
        except FileNotFoundError:
            print("Key file not found")
            # Prompt user to create a new key if it doesn't exist
            choice = input("Would you like to create a key? (yes/no) <: ")
            if choice == "yes":
                write.write_key()
            else:
                print("If you already have a key, put it in the current working directory")


class add:
    @staticmethod
    def add():
        # Create a popup window for user input
        # Site input
        while True:
            site = simpledialog.askstring("Site Name", "Enter the name of the site you wish to add:")
            if site is None:
                return
            elif site == "":
                tkinter.messagebox.showerror("Error", "Site can not be empty!")
                continue
            else:
                break

        # Username input
        while True:
            username = simpledialog.askstring("Username", "Enter the username of the site you wish to add:")
            if username is None:
                return
            if username == "":
                tkinter.messagebox.showerror("Error", "Username can not be empty!")
                continue
            else:
                break

        # Password input
        while True:
            pwd = simpledialog.askstring("Password", "Enter the password of the site you wish to add:")
            if pwd is None:
                return
            if pwd == "":
                tkinter.messagebox.showerror("Error", "Password can not be empty!")
                continue
            else:
                with open('passwords.txt', 'a') as f:
                    f.write(site + "\n" + username + ' | ' + Application.fer.encrypt(pwd.encode()).decode() + "\n")
                break


if __name__ == "__main__":
    app = Application()
    app.mainloop()
