import subprocess
from classes.platform import Platform
class Bluetooth:
    def __init__(self):
        pass
    def connect(self):
        if Platform().is_linux():
            try:
                result = subprocess.run(['bl.sh'], capture_output=True, text=True)
                return result.stdout.strip() == "True"
            except:
                return False
        elif Platform().is_windows():
            print("Warning: connect to bluetooth is not implemented for Windows Os. ")
        else:
            print("Error: platform is not known.")