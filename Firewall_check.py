import subprocess
import os
import platform
import customtkinter as ctk
from dialogs import ask_password

class Firewall:

    def linux_firewall():
        password = ask_password()
        if not password:
            return "No password entered" 
        operating_system = platform.system()
        if operating_system == "Linux":
            command = f'echo {password} | sudo -S ufw status'
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return output
        if operating_system == "Windows":
            print("Windows")
        else:
            pass





