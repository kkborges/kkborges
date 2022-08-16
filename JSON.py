import platform

hostname = platform.uname()
print(hostname.node)
host = hostname.node
ProcessMemory: float = 0.00
ProcessName: str = ""
ProcessCPU: float = 0.00
ProcessUser: str = ""
ProcessNet: str = ""
json = {"hotspot": {"id": "token", "host": {"cpu_perc": "99",
                                            "ram_perc": "50",
                                            "disk_usage_perc": "22",
                                            "network_bytes_sent": "43534",
                                            "network_bytes_received": "767",
                                            "processes": [
                                                {
                                                    "name": "lua.exe",
                                                    "cpu_perc": "99",
                                                    "ram_perc": "50",
                                                    "disk_usage_perc": "22",
                                                    "network_bytes_sent": "43534",
                                                    "network_bytes_received": "767"
                                                },
                                                {
                                                    "name": "lua.exe",
                                                    "cpu_perc": "99",
                                                    "ram_perc": "50",
                                                    "disk_usage_perc": "22",
                                                    "network_bytes_sent": "43534",
                                                    "network_bytes_received": "767"
                                                },
                                                {
                                                    "name": "lua.exe",
                                                    "cpu_perc": "99",
                                                    "ram_perc": "50",
                                                    "disk_usage_perc": "22",
                                                    "network_bytes_sent": "43534",
                                                    "network_bytes_received": "767"
                                                }
                                            ]
                                            }
                    }
        }
