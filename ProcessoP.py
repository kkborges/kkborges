import datetime
import math
import platform
import socket
import sys
import psutil
from typing import List

import topProcessos
from JSON import json


class Processo:
    host: str = ""
    cpu: int = 0
    ProcessoTop = []
    memory: int = 0
    name: str = ""
    user: str = ""
    bytesSent: str = ""
    bytesRecv: str = ""
    ip: str = ""
    hd: str = ""

    def gravarlog(self, status) -> None:
        if sys.platform == "win32":
            path = r'.\errorLog.txt'
        else:
            path = r'./paradoerrorLog.log'

        if status == "Sucess":
            if sys.platform == "win32":
                path = r'.\sucessLog.txt'
            else:
                path = r'./sucessLog.log'

        data_format = "%Y-%m-%d %H:%M:%S"  # ano-mês-dia hora:min:seg
        data = datetime.datetime.now().strftime( data_format )
        log = f"{data} {status} ({self.host},{self.name}, {int( self.memory )}, {int( self.cpu )}, {self.user}, {self.bytesRecv}, {self.bytesSent}, {self.ip}, {int( self.hd )}, {self.ProcessoTop}\n"
        try:
            # TODO: garantir que diretório existe?
            # TODO: colocar cabeçalho no log pra identificar cada coluna?
            with open( path, 'a' ) as f:
                f.writelines( log )
        except (IOError, OSError) as e:
            print( e )

    def as_dict(self) -> json:
        return {"name": self.name,
                "cpu_perc": int(self.cpu),
                "ram_perc": int(self.memory) ,
                "disk_usage_perc": self.hd}




def coletarProcessos():
    processos = []
    count = 1
    for proc in psutil.process_iter():
        processo = Processo()
        try:
            processo.name = proc.name()
            processo.memory = proc.memory_percent(memtype='vms')
            processo.cpu = proc.cpu_percent(interval=1)
            processo.hd = psutil.disk_usage('c:\\').percent
            processo.user = proc.username()
            processo.bytesSent = psutil.net_io_counters().bytes_sent
            processo.bytesRecv = psutil.net_io_counters().bytes_recv
            processo.ip = socket.gethostbyname( socket.gethostname() )
            processo.host = platform.node()
            processo.gravarlog( status="Sucess" )
            processos.append( processo )
            count += 1
        except psutil.ZombieProcess:
            processo.gravarlog( status="ZombieProcess" )
        except psutil.NoSuchProcess:
            processo.gravarlog( status="NoSuchProcess" )
        except psutil.AccessDenied:
            processo.gravarlog( status="AccessDenied" )
        if count == 5:
            return processos
        break
    print( processos )
    return processos
