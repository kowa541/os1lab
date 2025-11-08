import win32api
import win32file
import win32con
import socket
import platform
import sys


def get_version():
    
    ver = win32api.GetVersionEx()
    major = ver[0]
    minor = ver[1]
        
    if major > 10 or (major == 10 and minor >= 0):
            return "Windows 10 or Greater"
    else:
            return "Windows under 10"


def get_name_pc():
    try:
        return win32api.GetComputerName()
    except Exception:
        return "Unknown"


def get_user_name():
    try:
        return win32api.GetUserName()
    except Exception:
        return "Unknown"


def get_architecture():
    return platform.machine()


def get_memory():
   
    try:
        mem = win32api.GlobalMemoryStatus()
        total = mem['TotalPhys'] // (1024 **2)   
        avail = mem['AvailPhys'] // (1024 **2)   
        load = mem['MemoryLoad']                    
        return {
            'ram_total': total,
            'ram_avail': avail,
            'load': load
        }
    except Exception as e:
        print(f"Error {e}")
        return None


def get_pagefile():
    try:
        mem = win32api.GlobalMemoryStatus()
        total_pagefile_mb = mem['TotalPageFile'] // (1024 **2)
        return total_pagefile_mb
    except Exception as e:
        print(f"Error {e}")
        return 0


def get_processor_count():
    try:
        return win32api.GetSystemInfo()[5]  
    except Exception:
        return 0


def get_disk():
    
    drives = []
    try:
        drive_strings = win32api.GetLogicalDriveStrings().split('\0')
        for drive in drive_strings:
            if len(drive) != 3 or drive[1:] != ":\\": 
                continue
            try:
                disk_type = win32file.GetDriveType(drive)
                if disk_type not in (win32file.DRIVE_FIXED, win32file.DRIVE_REMOVABLE):
                    continue  
                free, total, _ = win32api.GetDiskFreeSpaceEx(drive)
                total_gb = total // (1024**3)
                free_gb = free // (1024**3)
                fs_type = win32api.GetVolumeInformation(drive)[4]  
                drives.append((drive, fs_type, free_gb, total_gb))
            except Exception:
                pass  
    except Exception:
        pass
    return drives


def main():
    print("OS: " + get_version())
    print("Computer Name: " + get_name_pc())
    print("User: " + get_user_name())
    print("Architecture: " + get_architecture())

    mem = get_memory()
    if mem:
        print("RAM: " + str(mem['ram_avail']) + "MB / " + str(mem['ram_total']) + "MB")
        print("Memory Load: " + str(mem['load']) + "%")
    else:
        print("Error")

    pf_total = get_pagefile()
    print("Pagefile: " + str(pf_total) + "MB")

    print("Processors: " + str(get_processor_count()))
    print("Drives:")
    disks = get_disk()
    if disks:
        for drive, fstype, free, total in disks:
            print("  - " + drive + " (" + fstype + "): " +
                  str(free) + " GB free / " + str(total) + " GB total")
    else:
        print("  - No drives")


if __name__ == "__main__":
    if sys.platform != "win32":
        print("You need Windows")
    else:
        main()
           