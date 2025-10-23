import platform
import os
from PyLibreHardwareMonitor import Computer
#Will get CPU temp and other system information based on platform


class Resources:
    def get_os_type():
        os_name = platform.system()
        if os_name == "Windows":
            return "Windows"
        if os_name == "Linux":

            return "Linux"
        else:
            return "Unknown"

Resources.get_os_type()
#Windows


#Linux