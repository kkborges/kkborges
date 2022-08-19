import platform

import psutil
# TODO: encapsular os códigos de ProcessoP.py e topProcess.py aqui!!

class Hotspot:
    def getHostname(self) -> object:
        pass
            # hostname = platform.node()
            # return self.hostname
    def getOS(self) -> str:
        return platform.system()
    def getOSVersion(self) -> str:
        return platform.version()

    def getToken(self):
        pass
        # return self.token

    def getIP(self):
        pass
    # return self.ip

    def getDownSpeed(self):
        pass
        # return self.download_speed_mbps

    def getUpSpeed(self):
        pass
        # return self.upload_speed_mbps

    def getTopProcess(self) -> object:
        pass
        # for proc in psutil.process_iter():
        #     try:
        #         topProcess = proc.memory_percent()
        #         if topProcess > topProcessMemory:
        #             topProcessMemory = topProcess
        #             topProcessName = proc.name()
        #             topProcessCPU = proc.cpu_percent(interval=0)
        #             topProcessUser = proc.username()
        #             topProcessIp = str(psutil.net_io_counters())
        #             topProcess = proc.memory_percent()
        #
        #         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        #             errorLog = open(r'c:\temp\errorLog.txt', 'w')
        #             gravaLog = datetime.datetime.now(), psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess
        #             gravaLog = (gravaLog)
        #             errorLog.writelines(str(gravaLog))
        #             errorLog.writelines("\n")
        #             errorLog.close()
        #         pass
        #         print("\n")
        #         ## print(topProcessName, topProcessCPU, topProcessMemory, topProcessUser)
        #         successLog = open(r'c:\temp\successLog.txt', 'w')
        #         gravaLog = datetime.datetime.now(
        #             time), topProcessName, topProcessCPU, topProcessMemory, topProcessUser, topProcessIp
        #         successLog.writelines(str(gravaLog))
        #         successLog.writelines("\n")
        #         successLog.close()
        # return self.topProcess