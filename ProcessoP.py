import datetime
import fileinput
import ipaddress
import ntpath
import platform

import psutil

# print(psutil.cpu_times())

host: str = ""
ProcessMemory: float = 0.00
ProcessName: str = ""
ProcessCPU: float = 0.00
ProcessUser: str = ""
ProcessNet: str = ""
ProcessIP: str = ""

for proc in psutil.process_iter():
    try:
        ProcessName = proc.name()
        if ProcessName == "python.exe":
            ProcessMemory = proc.memory_percent()
            ProcessCPU = proc.cpu_percent(interval=0)
            ProcessHD = proc.io_counters()
            ProcessUser = proc.username()
            ProcessNet = str(psutil.net_io_counters())
            ProcessIP = ipaddress.IPv4Address
            host = platform.node()

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        errorLog = open(r'c:\temp\errorLog.txt', 'w')
        gravaLog = datetime.datetime.now(), psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, ProcessIP, ProcessName, ProcessCPU, ProcessMemory, host
        errorLog.writelines(str(gravaLog))
        errorLog.writelines("\n")
        errorLog.close()

        pass
        print("\n")
        ## print(topProcessName, topProcessCPU, topProcessMemory, topProcessUser)
        successLog = open(r'c:\temp\successLog.txt', 'w')
        gravaLog = datetime.datetime.now(), ProcessName, ProcessCPU, ProcessMemory, ProcessUser, ProcessNet, ProcessIP, host
        successLog.writelines(str(gravaLog))
        successLog.writelines("\n")
        successLog.close()
