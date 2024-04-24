######################################################################
# SecurePassGen
# Created by Wayne Stock (omegazyph)
# created on 2024-04-23
# this program will use Tkinter and will create a password for the user
#######################################################################

# Imports
import random
import string
import tkinter as tk
from tkinter import messagebox, simpledialog, Text,Toplevel, Button, Label

# Main App Class
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure Password Generator ")
        self.geometry('400x200')
        self.configure(background="#f0f0f0")
        
        # Create a Label widget with text
        self.main_lable = Label(self, 
                                text="Welcome to Secure Password Generator", 
                                font=("Helvetica", 16),
                                bg="#f0f0f0", 
                                fg="#333333")
        self.main_lable.pack(pady=20)

        # Create a Button widget
        self.gen_button = Button(self, 
                                 text="Gen password", 
                                 command=GenPass.generate_password)
        self.gen_button.pack(pady=20)


        # Create a Label widget with text
        text_label = tk.Label(self, text="Password here!")
        text_label.pack()

class GenPass:
    def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
        characters = ''
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if not characters:
            raise ValueError("At least one character type should be included")

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

# Example usage
password = GenPass.generate_password(length=16, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True)
print("Generated Password:", password)



# Entry Point
if __name__ == "__main__":
    window = App()
    window.mainloop()    
