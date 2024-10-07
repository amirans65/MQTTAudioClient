import platform
class Platform:
    WINDOWS = "windows"
    LINUX = "linux"
    def get_platform(self):
        os = platform.platform()
        if os.lower().startswith(self.WINDOWS):
            return self.WINDOWS
        if os.lower().startswith(self.LINUX):
            return self.LINUX
    def is_windows(self):
        return self.get_platform() == self.WINDOWS
    def is_linux(self):
        return self.get_platform() == self.LINUX
        