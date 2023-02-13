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
        hostname = platform.node()
        OS = platform.system()
        os_version = platform.version()
        ip = socket.gethostbyname( socket.gethostname() )
        cpu_perc = int(psutil.cpu_percent( interval=1 ))
        ram = psutil.virtual_memory()
        ram_perc = int(ram[2])
        # disk_usage_perc = str( psutil.disk_usage( 'c:\\' ).percent )
        download_speed_mbps, upload_speed_mbps = get_velocidade_internet()
        if OS == 'Windows' :
            disk_usage_perc = int( psutil.disk_usage( path='c:\\' ).percent )
        else :
            disk_usage_perc = str( psutil.disk_usage( "/" ).percent )
        # chosen_process: dict = top_processes.get( top_processes['name'] )
        token = passwords.ler_token()
        # varChoseProcess = Requests.getschedule()
        # print( varChoseProcess )
        # chosen = varChoseProcess['choosen_process']
        # print( topProcessos.get_chosen_process( chosen ) )
        # print( topProcessos.get_top_five_process() )
        json_: dict = {"hotspot" : {"hostname" : hostname,
                                    "os" : OS,
                                    "os_version" : os_version,
                                    "token" : str( token ),
                                    "ip" : str( ip ),
                                    "download_speed_mbps" : str( download_speed_mbps ),
                                    "upload_speed_mbps" : str( upload_speed_mbps ),
                                    "host" : {"cpu_perc" : str( cpu_perc ), "ram_perc" : str( ram_perc ),
                                              "disk_usage_perc" : str( disk_usage_perc ),
                                              "top_processes" : topProcessos.get_top_process(),
                                              "chosen_processes" : topProcessos.get_chosen_process()
                                              }
                                    }
                       }
        return json_
