import os
import psutil
import Requests

def get_top_process():
    processo_top = []
    processos = ""
    #logger = logging.getLogger( __name__ )
    for process in psutil.process_iter():
        try:
            if process.name() != 'System Idle Process' or process.name() != 'System' or process.username() != 'None':
                if os.system == 'Windows' :
                    top_process_disk_usage_perc = str(psutil.disk_usage( path='c:\\' ).percent )
                else :
                    top_process_disk_usage_perc = str( psutil.disk_usage( "/" ).percent )
                top_process_name = process.name()
                top_disk = (top_process_disk_usage_perc[0 :2])
                top_process_disk_usage_perc = int( top_disk )
                top_process_cpu_perc = str( process.cpu_percent() )
                top_p = top_process_cpu_perc[0]
                top_process_cpu_perc = int(top_p)
                top_process_ram_perc = str( process.memory_percent())
                top_ram = (top_process_ram_perc[0 :1])
                top_process_ram_perc = int( top_ram )
                print("pqp")
                processo_top.append({"name": top_process_name, "cpu_perc": str(top_process_cpu_perc), "ram_perc": str(top_process_ram_perc), "disk_usage_perc": str(top_process_disk_usage_perc)})
            print(processo_top)
        except (psutil.AccessDenied, psutil.NoSuchProcess, OSError):
                #logger.info( (OSError) )
            pass
        #logger.info(process)

        return processo_top

def get_chosen_process():

    hotspot = Requests.getschedule()
    chosen_process = hotspot['chosen_process_name']
    chosen_p = []

    for process in psutil.process_iter():
        if process.name() == chosen_process:
            chose_p_cpu_perc = str( psutil.cpu_percent() )
            cpu_perc = int(chose_p_cpu_perc[0])
            chose_p_ram = str(process.memory_percent())
            ram_perc = int(chose_p_ram[0:1])
            if os.system == 'Windows' :
                disk_usage_perc = int( psutil.disk_usage( path='c:\\' ).percent )
            else :
                disk_usage_perc = int( psutil.disk_usage( "/" ).percent )
            chosen_p.append({"name" : chosen_process, "cpu_perc" : str(cpu_perc), "ram_perc" : str(ram_perc), "disk_usage_perc" : str(disk_usage_perc)})
            return chosen_p

