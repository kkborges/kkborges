import datetime
import platform
import socket
import sys
import psutil
from typing import List


class Processo:
    host: str = ""
    #TODO: tirar prefixo Process dos atributos?
    ProcessCPU: float = 0.00
    ProcessMemory: float = 0.00
    ProcessName: str = ""
    ProcessUser: str = ""
    BytesSent: str = ""
    BytesRecv: str = ""
    ProcessIP: str = ""
    ProcessHD: str = ""  # TODO: dividir valores? (no momento recebe o valor de uma tupla)

    def __str__(self):
        to_str = "Processo("
        to_str += f"host={self.host}, "
        to_str += f"ProcessName={self.ProcessName}, "
        to_str += f"ProcessMemory={self.ProcessMemory}, "
        to_str += f"ProcessCPU={self.ProcessCPU}, "
        to_str += f"ProcessUser: {self.ProcessUser}, "
        to_str += f"BytesRecv: {self.BytesRecv}, "
        to_str += f"BytesSent: {self.BytesSent}, "
        to_str += f"ProcessIP: {self.ProcessIP}, "
        to_str += f"ProcessHD: {self.ProcessHD})\n"
        return to_str
    def __repr__(self):
        return f"({self.ProcessName}, {self.ProcessCPU}, {self.ProcessMemory})"

    def gravarlog(self, status):
        if sys.platform == "win32":
            path = r'c:\temp\errorLog.txt'
        else:
            path = r'/home/pedro/Downloads/log/errorLog.log'  # TODO: estou usando minha home

        if status == "Sucess":
            if sys.platform == "win32":
                path = r'c:\temp\sucessLog.txt'
            else:
                path = r'/home/pedro/Downloads/log/sucessLog.log'

        data_format = "%Y-%m-%d %H:%M:%S"  # ano-mês-dia hora:min:seg
        data = datetime.datetime.now().strftime(data_format)
        log = f"{data} {status} {self.ProcessIP} {self.ProcessName} {self.ProcessCPU} {self.ProcessMemory} {self.host}\n"
        try:
            # TODO: garantir que diretório existe?
            # TODO: colocar cabeçalho no log pra identificar cada coluna?
            with open(path, 'a') as f:
                f.writelines(log)
        except (IOError, OSError) as e:
            print(e)


def coleta() -> List[Processo]:
    processos = []
    cnt = 1
    for proc in psutil.process_iter():
        processo = Processo()
        try:
            if cnt == 5:  # TODO: apenas para debug, para depois de 5 processos que deram sucesso
                break
            processo.ProcessName = proc.name()
            processo.ProcessMemory = proc.memory_percent()
            processo.ProcessCPU = proc.cpu_percent(interval=0.0)
            processo.ProcessHD = proc.io_counters()
            processo.ProcessUser = proc.username()
            processo.BytesSent, processo.BytesRecv, *_ = psutil.net_io_counters()
            processo.ProcessIP = socket.gethostbyname(socket.gethostname())
            processo.host = platform.node()
            print(processo) # TODO: apenas para debug
            cnt += 1
            processo.gravarlog(status="Sucess")
            processos.append(processo)
        except psutil.ZombieProcess:
            processo.gravarlog(status="ZombieProcess")
        except psutil.NoSuchProcess:
            processo.gravarlog(status="NoSuchProcess")
        except psutil.AccessDenied:
            processo.gravarlog(status="AccessDenied")
        else:
            pass  # TODO: lidar com outros casos?
    return processos

print(coleta())
