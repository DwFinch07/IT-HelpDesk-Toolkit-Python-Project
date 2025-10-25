import customtkinter as ctk
import os
from ping_functions import *
from resources import * 
from Firewall_check import *
from speedtest_function import *
import threading
#Main Tkinter file (will have main GUI functionality, button presses will use Functions created in other files ex. ping.py)
#DONE IDEAS
#Pinging Google (DONE) For Testing Internet Connections
#(Done)CPU and Resource Monitoring Built in
#(DONE)Check if firewall active Linux 
#(DONE)On Top Make Label and Bar
#(DONE)Find a way to detect if program is being used on windows or linux or make an options setting to change

#System Report using all functions and return results
#RDP Checker to see if RDP is running (Possible)
#Test VPN (Possible)
#Get Remaining Disk Usage on apps


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("HelpDesk Toolkit")
        self.geometry("1200x800")
        self.resizable(False,False)

        #App Label
        label_font = ("Times New Roman", 50, "bold")
        self.app_label = ctk.CTkLabel(self, text = "Help Desk Toolkit", fg_color= "transparent", font= label_font, corner_radius= 40 ) 
        self.app_label.place(x=400,y=-5)

         #Frames
        self.main_frame = ctk.CTkFrame(self, width = 1000, height = 700, border_color= "dark_color")
        self.main_frame.place(x= 100 ,y = 50)
            #Frame for CMD Output
        self.output_frame = ctk.CTkFrame(self, width = 1000, height = 250, border_color= "dark_color", fg_color="black")
        self.output_frame.place(x= 100 ,y = 500)

        self.output_textbox = ctk.CTkTextbox(self.output_frame, width= 980, height= 230)
        self.output_textbox.place(x=10, y=10)
        self.output_textbox.configure(state = "disabled")
   
        #Ping Button
        self.ping_button = ctk.CTkButton(self.main_frame, text = "Test Internet Connection",command = self.ping_on_click, height= 50, width= 50,border_color="black", border_width= 2)
        self.ping_button.place(x = 50, y= 300)

        #Resources Button
        self.resource_button = ctk.CTkButton(self.main_frame, text = "Resource Checker",command = self.resource_check, height= 50, width= 50 ,border_color="black", border_width= 2)
        self.resource_button.place(x = 50, y= 200)

        #Firewall Button
        self.firewall_button = ctk.CTkButton(self.main_frame, text = "Check Firewall Status",command = self.firewall, height= 50, width= 50, border_color="black", border_width= 2)
        self.firewall_button.place(x = 50, y= 100)

        #Speed Test Button
        self.firewall_button = ctk.CTkButton(self.main_frame, text = "Speed Test",command = self.speed_test_function, height= 50, width= 50, border_color="black", border_width= 2)
        self.firewall_button.place(x = 550, y= 100)

        #Quit Button
        self.quit_button = ctk.CTkButton(self, text = "Quit", command = self.destroy)
        self.quit_button.place(x=550,y=760)

        #Labels
        #self.label = ctk.CTkLabel(self.main_frame, text = "Test Ping")
        #self.label.place(x = 120, y = 250
        

    def ping_on_click(self):
        ping_result = Ping.test_ping(times= 2)
        self.output_textbox.configure(state="normal")
        self.output_textbox.insert("end", ping_result + "\n")
        self.output_textbox.configure(state= "disabled")
        self.output_textbox.see("end")

    def resource_check(self):
        resource_list = Resources.windows_stats()
        for key, value in resource_list.items():
              self.output_textbox.insert("end",f"{key}: {value}" + "\n")
        self.output_textbox.configure(state="normal")
    
    def firewall(self):
        firewal_status = Firewall.linux_firewall()
        self.output_textbox.configure(state="normal")
        self.output_textbox.insert("end",f"{firewal_status}" + "\n")
        self.output_textbox.configure(state= "disabled")
        self.output_textbox.see("end")

    def speed_test_function(self):
        speed_test_result = Speed_test.test_speed()
        self.output_textbox.configure(state="normal")
        self.output_textbox.insert("end",f"{speed_test_result}" + "\n")
        self.output_textbox.configure(state= "disabled")
        self.output_textbox.see("end")


    #def password_prompt(self):
    #    ask_user_root_password = ctk.CTkInputDialog(text = "Root Password Is Required: ", title="Root Password" )
    #    user_root_password = ask_user_root_password.get_input()
    #    if user_root_password:
    #        thread = threading.Thread(target=self.password_check, args=(user_root_password,))
    #        thread.start()

    def password_check(self,user_root_password):
        try:
            output = Firewall.linux_firewall(user_root_password)
            self.append_output(output)
        except Exception as e:
            self.append_output(f"Error: {e}")


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green")
    root = Root()
    root.mainloop()
    



#Extra Code

#Text Box
#text_box = tk.CTkTextbox(root)
#text_box.insert("0.0","Hello World")
#text_box.grid(row= 0 , column = 0)
#text = text_box.get("0.0", "end")
#text_box.configure(state="disabled")

#tk.CTkToplevel(fg_color='Black') ##Create 2nd Window Above Could be used in future
