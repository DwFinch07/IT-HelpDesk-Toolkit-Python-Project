import platform
import os
import psutil
import subprocess
#Will get CPU temp and other system information based on platform


class Resources:
    def windows_stats():
        info = {}
        
        info["OS"] = platform.system()
        info["OS Version"] = platform.version()
        info["CPU Cores"] = psutil.cpu_count(logical=False)
        info["Logical CPU Cores"] = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq()
        if cpu_freq:
            info["CPU Freq (MHz)"] = round(cpu_freq.current,2)
        info["Current CPU Usage"] = psutil.cpu_percent(interval=1)
        info["Disk Usage"] = psutil.disk_usage('/')
        info["Battery Usage"] = psutil.sensors_battery()


        
        return info