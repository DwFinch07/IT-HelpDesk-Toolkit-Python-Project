import customtkinter as tk
import os
from ping_functions import *
#Main Tkinter file (will have main GUI functionality, button presses will use Functions created in other files ex. ping.py)

root = tk.CTk()
root.title("HelpDesk Toolkit")
root.configure(bg="#494652")
root.geometry("800x500")

def ping_on_click():
    result = test_ping
    return result
#Ping Button
ping_button = tk.CTkButton(root, text = "Test Internet Connection",command = ping_on_click())
ping_button.place(x=200,y=200)

#Quit Button
quit_button = tk.CTkButton(root, text = "Quit", command = root.destroy)
quit_button.place(x=700,y=425)

root.mainloop()
