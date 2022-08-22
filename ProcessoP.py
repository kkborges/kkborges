import datetime
import platform
import socket
import sys
import psutil
from typing import List

from JSON import json


class Processo:
    host: str = ""
    cpu: float = 0.00
    memory: float = 0.00
    name: str = ""
    user: str = ""
    bytesSent: str = ""
    bytesRecv: str = ""
    ip: str = ""
#    hd: str = ""  # TODO: Verificar qual os significado desse valor

    def __str__(self) -> str:
        to_str = "Processo("
        to_str += f"host={self.host}, "
        to_str += f"ProcessName={self.name}, "
        to_str += f"ProcessMemory={self.memory}, "
        to_str += f"ProcessCPU={self.cpu}, "
        to_str += f"ProcessUser: {self.user}, "
        to_str += f"BytesRecv: {self.bytesRecv}, "
        to_str += f"BytesSent: {self.bytesSent}, "
        to_str += f"ProcessIP: {self.ip})\n"
#        to_str += f"ProcessHD: {self.hd})\n"
        return to_str

    def __repr__(self) -> str:
        return f"({self.name}, {self.cpu}, {self.memory})"

    def gravarlog(self, status) -> None:
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
        log = f"{data} {status} {self.ip} {self.name} {self.cpu} {self.memory} {self.host}\n"
        try:
            # TODO: garantir que diretório existe?
            # TODO: colocar cabeçalho no log pra identificar cada coluna?
            with open(path, 'a') as f:
                f.writelines(log)
        except (IOError, OSError) as e:
            print(e)

    def as_dict(self) -> json:
        return {"name": self.name,
                "cpu_perc": self.cpu,
                "ram_perc": self.memory,
                "disk_usage_perc": 0.0} #TODO
                #"disk_usage_perc": self.hd}


# TODO: onde colocar essa função
def coletarProcessos() -> List[Processo]:
    processos = []
    # cnt = 1
    for proc in psutil.process_iter():
        processo = Processo()
        try:
            # if cnt == 10:  # TODO: apenas para debug, para depois de 5 processos que deram sucesso
            #    break
            processo.name = proc.name()
            processo.memory = proc.memory_percent()
            processo.cpu = proc.cpu_percent(
                interval=0.1)  # TODO: precisei colocar um valor > 0.0 pra chegar em uma resposta válida
#            processo.hd =
            processo.user = proc.username()
            processo.bytesSent, processo.bytesRecv, *_ = psutil.net_io_counters()
            processo.ip = socket.gethostbyname(socket.gethostname())
            processo.host = platform.node()
            # print(processo) # TODO: apenas para debug
            # cnt += 1
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