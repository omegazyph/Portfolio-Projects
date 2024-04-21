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




class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager V3.0")
        self.geometry("400x300")  # Set the initial size of the window
        self.configure(background="#f0f0f0")  # Set background color

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

        self.add = tk.Button(self, text="Add a password")
        self.add.pack(side=tk.LEFT, padx=5)  # Place button 2 on the left with some padding

        self.view = tk.Button(self, text="View Passwords")
        self.view.pack(side=tk.LEFT, padx=5)  # Place button 3 on the left with some padding


   

class write:
    @staticmethod
    def write_key():
        try:
            # Display a warning message
            result = tkinter.messagebox.askquestion("Create Key", "Are you sure you want to create a new key?")
            if result == "yes":
                key = Fernet.generate_key()
                with open("key.key", 'wb') as key_file:
                    key_file.write(key)
                tkinter.messagebox.showinfo("Key Created", "A new key has been successfully created.")
            else:
                tkinter.messagebox.showinfo("Cancelled", "Key creation has been cancelled.")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
class add:
    pass





class view:
    pass







if __name__ == "__main__":
    app = Application()
    app.mainloop()
