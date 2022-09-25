import base64
import requests
import json
import passwords


# TODO: fazer comentários

def sendhotspot(json_dict: dict):
    print("Sending hotspot")

    url = "https://shrouded-spire-06255.herokuapp.com/v1/entry_raws"
    headers = {"Accept": "application/json", "Content-type": "application/json"}

    jsonStr_encoded = base64.b64encode(json.dumps(json_dict).encode('utf-8'))

    print("jsonStr_encoded: " + str(jsonStr_encoded.decode('utf-8')))
    json_final = {"entry_raw": {"payload": str(jsonStr_encoded.decode('utf-8') + "=\n")}}

    response = requests.post(url, headers=headers, json=json_final, verify=False)

    print("status code", response.status_code)
    print("response.json()", response.json())


# TODO: ver qual é o formato do tempo?
# Considerando o formato 0000AM ou 0000PM
def convert_date_to_int(time: str) -> int:
    if len(time) == 0:
        return 0

    if len(time) != 6:
        print("Formato errado")
        # TODO: lidar melhor
        exit(1)

    print(f"{int(time[0])} {int(time[1])} {int(time[2])} {int(time[3])}")
    hour = int(time[0]) * 10 + int(time[1])
    minute = int(time[2]) * 10 + int(time[3])

    if time[4:] == "PM":
        hour += 12

    print(f"{hour}:{minute}")
    return hour * 60 + minute


def getschedule() -> dict:
    """"
    Pega os horários que é permitido executar
    """
    tmp = f"https://shrouded-spire-06255.herokuapp.com/v1/hotspots/{passwords.token}.json"
    r = requests.get(tmp)
    r = r.json()

    hotspot = r['hotspot']
    # TODO: lidar com erros
    schedule = {'active': r['active'], 'sun': hotspot['sun'], 'mon': hotspot['mon'], 'tue': hotspot['tue'],
                'wed': hotspot['wed'], 'thu': hotspot['thu'], 'fri': hotspot['fri'], 'sat': hotspot['sat'],
                'start_time': convert_date_to_int(hotspot['start_time']),
                'end_time': convert_date_to_int(hotspot['end_time'])}

    # estou lidando aqui com o caso de não ser fornecido o end_time
    if schedule['end_time'] == 0:
        schedule['end_time'] = 24 * 60
    return schedule


# TODO: Melhorar testes
def teste():
    sendhotspot({"hotspot": {"hostname": "DESK932LK-ELO",
                             "os": "WINDOWS",
                             "os_version": "10",
                             "token": passwords.token,
                             "ip": "120.211.3.111",
                             "download_speed_mbps": "90",
                             "upload_speed_mbps": "15",
                             "host": {"cpu_perc": "40",
                                      "ram_perc": "40",
                                      "disk_usage_perc": "40",
                                      "top_processes": [{"name": "lua.exe",
                                                         "cpu_perc": "45",
                                                         "ram_perc": "45",
                                                         "disk_usage_perc": "45"}],
                                      "chosen_processes": [{"name": "teamviewer.exe",
                                                            "cpu_perc": "45",
                                                            "ram_perc": "45",
                                                            "disk_usage_perc": "45"}]
                                      }
                             }
                 })

    convert_date_to_int("1200AM")
    convert_date_to_int("0950PM")
    convert_date_to_int("0800AM")
teste()