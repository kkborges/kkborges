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


#Considera o formato AM PM
def convert_date_to_seconds(time: str) -> int:
    # print(f"(convert_data_to_seconds) horário recebido: {time[:4]}")
    hour = int(time[0:2])
    if (time[4:] == "PM"):
        hour += 12

    minute = int(time[2:4])
    # print(f"{hour}:{minute}")
    to_seconds = hour * 60 + minute
    # print(to_seconds)
    return to_seconds

def getschedule() -> dict:
    """"
    Pega os horários que é permitido executar
    """

    r = requests.get(f'https://shrouded-spire-06255.herokuapp.com/v1/hotspots/{passwords.token}.json')
    r = r.json()
    hotspot = r['hotspot']
    # TODO: lidar com erros
    schedule = {'active': r['active'], 'sun': hotspot['sun'], 'mon': hotspot['mon'], 'tue': hotspot['tue'],
                'wed': hotspot['wed'], 'thu': hotspot['thu'], 'fri': hotspot['fri'], 'sat': hotspot['sat'],
                'start_time': convert_date_to_seconds(hotspot['start_time_str']),
                'end_time': convert_date_to_seconds(hotspot['end_time_str'])}
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