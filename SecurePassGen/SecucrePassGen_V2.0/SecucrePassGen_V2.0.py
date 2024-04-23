######################################################################
# SecurePassGen
# Created by Wayne Stock (omegazyph)
# created on 2024-04-23
# this program will use Tkinter and will create a password for the user
#######################################################################

# Imports
import random
import string
from tkinter import *

# Create a window
root = Tk()
root.title("Secure Password Generator ")
root.geometry('400x400')

gen_button = Button(root, text="Gen password", command=GenPass.generate_password).pack()

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
password = generate_password(length=16, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True)
print("Generated Password:", password)



# start the window
root.mainloop()