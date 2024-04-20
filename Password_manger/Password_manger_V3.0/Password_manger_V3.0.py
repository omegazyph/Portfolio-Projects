import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager V3.0")
        self.geometry("400x300")  # Set the initial size of the window
        self.configure(background="#f0f0f0")  # Set background color

        # Create widgets
        self.label = tk.Label(self, text="Hello, Tkinter!", 
                              font=("Helvetica", 16), 
                              bg="#f0f0f0", 
                              fg="#333333")  # Set background and foreground color
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Click Me!", 
                                command=self.on_button_click, 
                                bg="#008CBA", 
                                fg="white")  # Set button colors
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button clicked!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
