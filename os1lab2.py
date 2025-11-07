import subprocess
import os
import shutil
import socket

try:
    with open("/etc/os-release", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("PRETTY_NAME"):
                print(line.split("=", 1)[1].strip().strip('"'))
except (FileNotFoundError, PermissionError, OSError):
    pass
    print('Linux')
    
print("Kernel: ", os.uname().release)

info = {}
with open('/proc/meminfo', 'r') as f:
    for line in f:
        splitt = line.split()
        if splitt[0].rstrip(':') == "MemFree":
            free_memory = int(splitt[1])
        if splitt[0].rstrip(':') == "MemTotal":
            total_memory = int(splitt[1])
        if splitt[0].rstrip(':') == "SwapFree":
            free_swapmemory = int(splitt[1])
        if splitt[0].rstrip(':') == "SwapTotal":
            total_swapmemory = int(splitt[1])
            
with open('/proc/self/status', 'r') as f:
    for line in f:
        if line.startswith("VmSize"):
            vmmemory = int(line.split()[1])
            
print("RAM: ", free_memory//1024, "MB free/", total_memory//1024, "MB total")
print("Swap: ", free_swapmemory//1024, "MB free/", total_swapmemory//1024, "MB total")
print("Virtual memory ", vmmemory//1024, "MB")

print("Logical processors: ", os.cpu_count())

onecpu, fivecpu, fiftcpu = os.getloadavg()
print(f"Load average: {onecpu:.2f} {fivecpu:.2f} {fiftcpu:.2f}")

print("Drives:")
if os.path.exists("/"):
    total, used, free = shutil.disk_usage("/")
    print("/ ext4", free//(1024**3), "GB free / ", total//(1024**3), "GB total")
if os.path.exists("/mnt/c"):
    totalmnt, usedmnt, freemnt = shutil.disk_usage("/mnt/c")
    print("/mnt/c fuse ", freemnt//(1024**3), "GB free / ", totalmnt//(1024**3), "GB total")


print("User: ", os.getlogin())
print("Hostname: ", socket.gethostname())

print("Architecture: ", os.uname().machine)
