import customtkinter as ctk
import os
from ping_functions import *
#Main Tkinter file (will have main GUI functionality, button presses will use Functions created in other files ex. ping.py)

#Ideas For Application 
#CPU and Resource Monitoring Built in
#Pinging Google (DONE) For Testing Internet Connections
#System Report using all functions and return results
#RDP Checker to see if RDP is running (Possible)
#Test VPN (Possible)
#Get Remaining Disk Usage on apps
#Check if firewall active
#Find a way to detect if program is being used on windows or linux or make an options setting to change



root = ctk.CTk()
root.title("HelpDesk Toolkit")
#root.configure(bg="#494652")
root.geometry("800x500")

#Text Box
#text_box = tk.CTkTextbox(root)
#text_box.insert("0.0","Hello World")
#text_box.grid(row= 0 , column = 0)
#text = text_box.get("0.0", "end")
#text_box.configure(state="disabled")

#tk.CTkToplevel(fg_color='Black') ##Create 2nd Window Above Could be used in future

label = ctk.CTkLabel(master = root, text = "Test Ping")
label.place(anchor = ctk.CENTER)


def ping_on_click():
    result = test_ping
    return result
#Ping Button
ping_button = ctk.CTkButton(master = root, text = "Test Internet Connection",command = ping_on_click())
ping_button.place(x=200,y=200)

#Quit Button
quit_button = ctk.CTkButton(root, text = "Quit", command = root.destroy)
quit_button.place(x=700,y=425)

root.mainloop()
