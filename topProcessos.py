import os
import psutil

def get_top_five_process():
    process_strings = []
    for process in psutil.process_iter():
        try:

            process_info = process.as_dict( attrs=['name', 'memory_percent', 'cpu_percent', 'username', 'cmdline'] )

            username=process.as_dict(attrs=['username'])
            proc_bytes_sent = psutil.net_io_counters( pernic=False ).bytes_sent
            proc_bytes_received = psutil.net_io_counters( pernic=False ).bytes_recv
            if os.system == 'Windows':
                disk_usage_perc = str( psutil.disk_usage( path='c:\\' ).percent )
            else:
                disk_usage_perc = str( psutil.disk_usage( "/" ).percent )
            name = process_info['name']
            cpu_percent = process_info['cpu_percent']
            memory_percent = process_info['memory_percent']
            disk_usage_perc = disk_usage_perc
            network_bytes_sent = proc_bytes_sent
            network_bytes_received = proc_bytes_received
            process_string = {"name": name, "cpu_perc": str(cpu_percent), "mem_perc": str(memory_percent), "disk_usage_perc": disk_usage_perc, "network_bytes_sent": str(network_bytes_sent), "network_bytes_received": str(network_bytes_received)}
            if process_info['name'] != 'System Idle Process':
                    if process_info['name'] != 'System':
                            if username != 'None':
                                if int(process_info['cpu_percent']) > 5:
                                    process_strings.append( process_string )
        except (psutil.AccessDenied, psutil.NoSuchProcess, OSError):
            # Ignore the error, use whatever info is available for access.
            pass

    processos = sorted( process_strings, key=lambda process: process_info['memory_percent'], reverse=True  )

    return processos

def get_chosen_process(chosen):
    chosen_ = get_top_five_process()
    chosen = chosen_[0]

    return chosen



