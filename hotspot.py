import platform
import socket
import psutil
import speedtest

import passwords
import topProcessos


def get_velocidade_internet():
    tx_down = int( speedtest.Speedtest().download() )
    tx_up = int( speedtest.Speedtest().upload() )
    tx_down.to_bytes( signed=True, byteorder='little', length=8 )
    tx_up.to_bytes( signed=True, byteorder='little', length=8 )
    tx_down = float( tx_up )
    tx_up = float( tx_up )
    return tx_down, tx_up

def get_host_info():
    hotspot: dict = {}
    hostname = platform.node()
    OS = platform.system()
    os_version = platform.version()
    ip = socket.gethostbyname( socket.gethostname() )
    cpu_perc = (psutil.cpu_percent( interval=1 ))
    ram = psutil.virtual_memory()
    ram_perc = ram[2]
    # disk_usage_perc = str( psutil.disk_usage( 'c:\\' ).percent )
    download_speed_mbps, upload_speed_mbps = get_velocidade_internet()
    if OS == 'Windows':
        disk_usage_perc = str( psutil.disk_usage( path='c:\\' ).percent )
    else:
        disk_usage_perc = str( psutil.disk_usage( "/" ).percent )
    #chosen_process: dict = top_processes.get( top_processes['name'] )
    token = passwords.ler_token()
    topProcess = topProcessos.get_top_five_process()
    print(topProcess)
    chosen_: dict = topProcessos.get_chosen_process('pycharm64.exe')
    print(chosen_)
    json_: dict = {"hotspot": {"token": token, "host": {"hostname": hostname,
                                                               "os": OS,
                                                               "os_version": os_version,
                                                               "ip": ip,
                                                               "cpu_perc": cpu_perc,
                                                               "ram_perc": ram_perc,
                                                               "disk_usage_perc": disk_usage_perc,
                                                               "download_speed_mbps": download_speed_mbps,
                                                               "upload_speed_mbps": upload_speed_mbps,
                                                               "chosen_process": topProcessos.get_chosen_process(chosen="chrome.exe"),
                                                               "top_process": topProcessos.get_top_five_process()
                                                               }
                               }
                   }

    print(json_)
    return json_



