import platform
import socket
from typing import List
import psutil

import ProcessoP
import topProcessos
from JSON import json
from ProcessoP import Processo


# TODO: encapsular os códigos de ProcessoP.py e topProcess.py aqui!!

class Hotspot:
    hostname: str = ""
    os: str = ""
    os_version: str = ""
    ip: str = ""
    cpu_perc: float = 0.0
    ram_perc: float = 0.0
    disk_usage_perc: float = 0.0
    top_processes: List[Processo] = []
    def get_host_info(self):
        self.hostname = platform.node()
        self.os = platform.system()
        self.os_version = platform.version()
        self.ip = socket.gethostbyname(socket.gethostname())
        self.cpu_perc = psutil.cpu_percent(interval=0.1)
        _, _, self.ram_perc, *_ = psutil.virtual_memory()
        *_, self.disk_usage_perc = psutil.disk_usage('/')
        self.top_processes = [p.as_dict() for p in topProcessos.topprocessos()]
    def as_dict(self) -> json:
        self.get_host_info()
        return {"hotspot": {"hostname": self.hostname,
                       "os": self.os,
                       "os_version": self.os_version,
                       "token": "22111548-c912-427f-8f8f-b138c83c5cf5", #TODO: colocar valor real
                       "ip": self.ip,
                       "download_speed_mbps": "90", #TODO: colocar valor real
                       "upload_speed_mbps": "15", #TODO: colocar valore real
                       "host": {"cpu_perc": self.cpu_perc,
                                "ram_perc": self.ram_perc,
                                "disk_usage_perc": self.disk_usage_perc,
                                "top_processes": self.top_processes,
                                "chosen_processes": [{"name": "teamviewer.exe", #TODO: colocar valores reais / verificar o significado desse atributo
                                                      "cpu_perc": "99",
                                                      "ram_perc": "50",
                                                      "disk_usage_perc": "22"}]
                                }
                       }
           }

hotspot = Hotspot()
print(hotspot.as_dict())