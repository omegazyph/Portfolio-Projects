########################################################
# Password Manger V 3.0
# created by Wayne Stock (omegazyph)
# created 2024-04-20
# This program is in tkinker to help with your passwords 
########################################################

# Imports
import tkinter as tk
from tkinter import PhotoImage
from cryptography.fernet import Fernet
import tkinter.messagebox
from tkinter import simpledialog


# Define the master password
MASTER_PASSWORD = "12345"




class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager V3.0")
        self.geometry("400x300")  # Set the initial size of the window
        self.configure(background="#f0f0f0")  # Set background color
        #self.check_master_password()  # Check the master password
        
        """ will fill in later
        # Load the background image
        self.background_image = PhotoImage(file="background_image.png")  # Change "background_image.png" to your image file
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        """
        # Create widgets
        self.welcome_label = tk.Label(self, text="Welcome to Password Manager V3.0", 
                              font=("Helvetica", 16), 
                              bg="#f0f0f0", 
                              fg="#333333")  # Set background and foreground color
        self.welcome_label.pack(pady=20)

         # Create widgets
        self.write = tk.Button(self, text="Create a Key", command= write.write_key)
        self.write.pack(side=tk.LEFT, padx=5)  # Place button 1 on the left with some padding

        self.add = tk.Button(self, text="Add a password", command= add.add)
        self.add.pack(side=tk.LEFT, padx=5)  # Place button 2 on the left with some padding

        self.view = tk.Button(self, text="View Passwords")
        self.view.pack(side=tk.LEFT, padx=5)  # Place button 3 on the left with some padding

    def check_master_password(self):
        # Prompt the user for the master password
        while True:
            master_pwd = simpledialog.askstring("Master Password", 
                                                "Enter the master password to access the program:")
            if master_pwd == MASTER_PASSWORD:
                key = LoadKey.load_key()
                fer = Fernet(key)
                break  # Correct master password, exit the loop
            elif master_pwd is None:
                return  # User closed the dialog, close the program
            else:
                tk.messagebox.showerror("Incorrect Password", "Incorrect master password. Please try again.")



class write:
    @staticmethod
    def write_key():
        try:
            # Display a warning message to confirm key creation
            result = tkinter.messagebox.askquestion("Create Key", "Are you sure you want to create a new key?")
            if result == "yes":
                # Display a second warning message to confirm key replacement
                result_confirm = tkinter.messagebox.askquestion("Confirmation", "Are you sure? This will replace your old key!")
                if result_confirm == "yes":
                    # Generate a new key
                    key = Fernet.generate_key()
                    # Write the new key to a file
                    with open("key.key", 'wb') as key_file:
                        key_file.write(key)
                    # Display a success message
                    tkinter.messagebox.showinfo("Key Created", "A new key has been successfully created.")
                else:
                    # Display a message indicating cancellation of key creation
                    tkinter.messagebox.showinfo("Cancelled", "Key creation has been cancelled.")
            else:
                # Display a message indicating cancellation of key creation
                tkinter.messagebox.showinfo("Cancelled", "Key creation has been cancelled.")
        except Exception as e:
            # Display an error message if an exception occurs
            tkinter.messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
class LoadKey:
    # Function to load the key from the file
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
    def add():
        # Create a popup window for user input
        # site input
        while True:
            site = simpledialog.askstring("Site Name", "Enter the name of the site you wish to add:")
            if site is None:
                return
            elif site == "":
                tkinter.messagebox.showerror("Error","Site can not be empty!")
                continue
            else:
                break
        
        # Username input
        while True:
            username = simpledialog.askstring("Username", "Enter the username of the site you wish to add:")
            if username is None:
                return
            if username == "":
                tkinter.messagebox.showerror("Error","Username can not be empty!")
                continue
            
            else:
                break
        
        # Password input
        while True:
            pwd = simpledialog.askstring("Password", "Enter the password of the site you wish to add:")
            if pwd is None:
                return
            if pwd == "":
                tkinter.messagebox.showerror("Error","Password can not be empty!")
                continue
            else:
                with open('passwords.txt', 'a') as f:
                    f.write(site + "\n" + username + ' | ' + Application.fer.encrypt(pwd.encode()).decode() + "\n")
                break






class view:
    pass







if __name__ == "__main__":
    app = Application()
    app.mainloop()
