import os
import psutil
import time
from datetime import datetime
import Requests
from erros import showErrorAlert
from hotspot import Hotspot


# TODO: fazer os comentários das funções

# from: https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
def find_process_id_by_name(process_name):
    """
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    """
    listOfProcessObjects = []
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            # Check if process name contains the given name string.
            if process_name.lower() == pinfo['name'].lower():
                listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listOfProcessObjects


def alreadyopen() -> bool:
    """
    Verifica se já há o mesmo processo aberto
    """
    pid = os.getpid()
    p = psutil.Process(pid)
    # print(psutil.Process(pid))
    name = p.name()
    process_same_name = find_process_id_by_name(name)
    # for i in process_same_name:
    #     print(i)
    return False  # TODO: só funciona se já tiver o executável
    # return len(l) > 1


def is_allowed_execute(schedule):
    if not schedule['active']:
        return False

    now = datetime.now()
    id_day = now.weekday()  # 0->segunda, 1->terça, ...
    id_to_str = {0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', 4: 'fri', 5: 'sat', 6: 'sun'}
    str_day = id_to_str[id_day]
    if not schedule[str_day]:
        return False

    to_seconds = now.hour * 60 + now.minute
    start_time = schedule['start_time']
    end_time = schedule['end_time']

    # print(f"Agora: {hour * 60 + minute}, start_time: {start_time}, end_time:{end_time} ")

    if start_time <= to_seconds <= end_time:
        return True
    return False


def hora_min_sec(min:int)->str:
    hora = min//(60)
    min = min % 60
    return f"{hora}:{min}"
def main():
    if alreadyopen():
        showErrorAlert('Erro: Múltiplas instâncias', 'O programa já está em execução')
        exit(1)

    schedule = Requests.getschedule()
    temposleep = 60
    while True:
        # Se não é permitido executar dorme por 5 minutos
        if not is_allowed_execute(schedule):
            print('Executando fora do horário')  # TODO: Fazer log disso?
            print(f"Agora sao: {datetime.now().strftime('%H:%M')}, (inicio do agente) às {hora_min_sec(schedule['start_time'])}, (fim) às {hora_min_sec(schedule['end_time'])}" )
            time.sleep(5 * 60)
            continue
        hotspot = Hotspot()
        print(hotspot.as_dict())
        Requests.sendhotspot(hotspot.as_dict())
        time.sleep(temposleep)


if __name__ == "__main__":
    main()
