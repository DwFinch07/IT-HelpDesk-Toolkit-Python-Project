import subprocess
import os
import platform

class Firewall:
    def os_firewall():
        operating_system = platform.system()
        warning = "If you want to use this Feature, open as Root/Administrator"
        if operating_system == "Linux":
           #linux_command = subprocess.run(["sudo", "ufw", "status"])
            output = subprocess.check_output(["sudo", "ufw", "status"], stderr=subprocess.STDOUT,universal_newlines=True)
            return output

        if operating_system == "Windows":
            output = subprocess.check_output("powershell -Command 'Get-Service -Name mpssvc'", stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
            return output
        else:
            pass





