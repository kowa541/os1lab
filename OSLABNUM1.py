import platform
import psutil
import socket
import getpass

def is_windows_10():
    if platform.system() != "Windows":
        return False

    version = int(platform.version().split('.')[0])
    return version >= 10

def byte_to_mb(num):
    return str(int(num / (1024**2)))+'MB'


if is_windows_10():
    print("Windows 10 or Greater")
else:
    print("Older than Windows 10")

#ôèçè÷åñêàÿ ïàìÿòü
ram = psutil.virtual_memory()
print("RAM: ", byte_to_mb(ram.available), "/", byte_to_mb(ram.total))
print("Memory Load: ", ram.percent, "%")

#âèðòóàëüíàÿ ïàìÿòü
virtual_memory = psutil.swap_memory()
print("Pagefile: ", byte_to_mb(virtual_memory.used), "/", byte_to_mb(virtual_memory.total))
print("Memory Load: ", virtual_memory.percent, "%")

#èìÿ óñòðîéñòâà
host = socket.gethostname()
print("Computer Name: ", host)

#èìÿ ïîëüçîâàòåëÿ
user = getpass.getuser()
print("User: ", user)

#ôèçè÷åñêèå ÿäðà
physical_cores = psutil.cpu_count(logical=False)
print("Physical cores: ", physical_cores)

#ëîãè÷åñêèå ÿäðà
logical_cores = psutil.cpu_count(logical=True)
print("Logical cores: ", logical_cores)

#àðõèòåêòóðà
print("Architecture: ", platform.machine())

#äèñêè
print("Drives:")

for i in psutil.disk_partitions():
    device = i.device
    fstype = i.fstype  
    
    try:
        usage = psutil.disk_usage(device)
        total_gb = int(usage.total / (1024**3))
        free_gb = int(usage.free / (1024**3))
        
        print("  - ", device, fstype, free_gb, "GB free /", total_gb, "GB total")
        
    except PermissionError:
        print(device, "unavailable")
