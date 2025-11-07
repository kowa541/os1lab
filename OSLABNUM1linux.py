import platform
import psutil


class SysInfo:
    def GetOSNameVersion(self):
        """Метод возвращает название ос."""
        if platform.system() == "Windows":
            return platform.system()+' '+platform.version()
        elif platform.system() == "Linux":
            try:
                with open("/etc/os-release", "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("PRETTY_NAME"):
                            return line.split("=", 1)[1].strip().strip('"')
            except (FileNotFoundError, PermissionError, OSError):
                pass
            return "Linux"
        else:
            return platform.system()


    def GetTotalMemory(self):
        """Общий объём ОЗУ в байтах."""
        return psutil.virtual_memory().total

    def GetFreeMemory(self):
        """Свободный объём ОЗУ в байтах."""
        return psutil.virtual_memory().available

    def GetProcessorCount(self):
        """Количество логических процессоров."""
        return psutil.cpu_count(logical=True)


def format_bytes(bytes_value: int):
    """Байты в мегабайты"""
    mb = round(bytes_value / (1024 ** 2), 2)
    return str(mb)+'MB'


def main():
    sys = SysInfo()

    print('OS Name and Version: ', sys.GetOSNameVersion())
    print('Total Memory:', format_bytes(sys.GetTotalMemory()))
    print('Free Memory:', format_bytes(sys.GetFreeMemory()))
    print('Processor:', sys.GetProcessorCount())


if __name__ == "__main__":
    main()