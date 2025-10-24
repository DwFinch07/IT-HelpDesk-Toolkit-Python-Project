import subprocess
import os
import platform

class Firewall:
    def linux_firewall():
        operating_system = platform.system()
        warning = "If you want to use this Feature, open as Root/Administrator"
        if operating_system == "Linux":
           #linux_command = subprocess.run(["sudo", "ufw", "status"])
            output = subprocess.check_output(["sudo", "ufw", "status"], stderr=subprocess.STDOUT,universal_newlines=True)
            return output
        if operating_system == "Windows":
            print("Windows")
        else:
            pass





