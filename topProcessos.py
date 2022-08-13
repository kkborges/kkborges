import datetime
import fileinput
import ntpath
import platform

import psutil

# print(psutil.cpu_times())

hostname = platform.uname()
print(hostname.node)
host = hostname.node

processMemory: float = 0.0

topProcessMemory: float = 0.00
topProcessName: str = ""
topProcessCPU: float = 0.00
topProcessUser: str = ""
topProcessIp: str = ""

for proc in psutil.process_iter():
    try:
        topProcess = proc.memory_percent()
        if topProcess > topProcessMemory:
            topProcessMemory = topProcess
            topProcessName = proc.name()
            topProcessCPU = proc.cpu_percent(interval=0)
            topProcessUser = proc.username()
            topProcessIp = str(psutil.net_io_counters())
            topProcess = proc.memory_percent()

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        errorLog = open(r'c:\temp\errorLog.txt', 'w')
        gravaLog = datetime.datetime.now(), psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess
        gravaLog = (gravaLog)
        errorLog.writelines(str(gravaLog))
        errorLog.writelines("\n")
        errorLog.close()

        pass
        print("\n")
        ## print(topProcessName, topProcessCPU, topProcessMemory, topProcessUser)
        successLog = open(r'c:\temp\successLog.txt', 'w')
        gravaLog = datetime.datetime.now(time), topProcessName, topProcessCPU, topProcessMemory, topProcessUser, topProcessIp
        successLog.writelines(str(gravaLog))
        successLog.writelines("\n")
        successLog.close()
