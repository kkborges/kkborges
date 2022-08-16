import datetime
import fileinput
import ntpath
import platform
import psutil

# TODO: Pegar top 5 processos que mais consomem memória/cpu


# TODO: codigo duplicado
hostname = platform.uname()
host: str = platform.node()
processMemory: float = 0.0
topProcessMemory: float = 0.00
topProcessName: str = ""
topProcessCPU: float = 0.00
topProcessUser: str = ""
topProcessIp: str = ""


# TODO: codigo duplicado
def echo():
    print(f"host: {host}")
    print(f"ProcessName: {topProcessName}")
    print(f"ProcessMemory: {topProcessMemory}")
    print(f"ProcessCPU: {topProcessCPU}")
    print(f"ProcessUser: {topProcessUser}")
    # print(f"ProcessNet: {topProcessNet}")
    # print(f"ProcessIP: {topProcessIP}\n")


for proc in psutil.process_iter():
    try:
        topProcess = proc.memory_percent()
        if topProcess > topProcessMemory:
            topProcessMemory = topProcess
            topProcessName = proc.name()
            topProcessCPU = proc.cpu_percent(interval=0.0)
            topProcessUser = proc.username()
            topProcessIp = str(psutil.net_io_counters())
            topProcess = proc.memory_percent()

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
        # TODO: similar ao anterior, registrar os erros
        # errorLog = open(r'c:\temp\errorLog.txt', 'w')
        # gravaLog = datetime.datetime.now(), psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess
        # gravaLog = (gravaLog)
        # errorLog.writelines(str(gravaLog))
        # errorLog.writelines("\n")
        # errorLog.close()
        #
        # pass
        # print("\n")
        # ## print(topProcessName, topProcessCPU, topProcessMemory, topProcessUser)
        # successLog = open(r'c:\temp\successLog.txt', 'w')
        # gravaLog = datetime.datetime.now(), topProcessName, topProcessCPU, topProcessMemory, topProcessUser, topProcessIp
        # successLog.writelines(str(gravaLog))
        # successLog.writelines("\n")
        # successLog.close()
echo()
