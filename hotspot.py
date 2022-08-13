import psutil


class Hotspot:
       def getHostname(self) -> object:
            hostname = platform.node()
            return self.hostname

        def getOS(self) -> object:
            OS = psutil.getSo()
            return self.os

        def getOSVersion(self):
            return self.os_version

        def getToken(self):
            return self.token

        def getIP(self):
            return self.ip

        def getDownSpeed(self):
            return self.download_speed_mbps

        def getUpSpeed(self):
            return self.upload_speed_mbps

        def getTopProcess(self) -> object:
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
                    gravaLog = datetime.datetime.now(
                        time), topProcessName, topProcessCPU, topProcessMemory, topProcessUser, topProcessIp
                    successLog.writelines(str(gravaLog))
                    successLog.writelines("\n")
                    successLog.close()
            return self.topProcess
            :