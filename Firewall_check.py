import subprocess
import os
import platform
import customtkinter as ctk
from main import password_prompt
password = password_prompt

class Firewall:
    def linux_firewall():
        operating_system = platform.system()
        if operating_system == "Linux":
            command = f'echo {password} | sudo -S ufw status'
            output = subprocess.check_output([command], stderr=subprocess.STDOUT,universal_newlines=True)
            return output
        if operating_system == "Windows":
            print("Windows")
        else:
            pass





