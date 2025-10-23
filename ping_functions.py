import subprocess
import platform

def test_ping(times=1):
    hostname = "google.com"

    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        output = subprocess.check_output(["ping", param, str(times), hostname], stderr=subprocess.STDOUT,universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output
    
