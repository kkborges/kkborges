import math
import platform
import socket
from typing import List
import psutil
import passwords
import topProcessos
from JSON import json
from ProcessoP import Processo


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
                            "os": "WINDOWS", #self.os, TODO
                            "os_version": "10", #self.os_version,
                            "token": passwords.token,
                            "ip": self.ip,
                            "download_speed_mbps": "90",  # TODO: colocar valor real
                            "upload_speed_mbps": "15",  # TODO: colocar valore real
                            "host": {"cpu_perc": 99, #TODO #math.ceil(self.cpu_perc),
                                     "ram_perc": math.ceil(self.ram_perc),
                                     "disk_usage_perc": math.ceil(self.disk_usage_perc),
                                     "top_processes": self.top_processes,
                                     "chosen_processes": []
                                     }
                            }
                }