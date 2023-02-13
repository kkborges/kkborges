import base64
import requests
import json
import passwords
from datetime import *

# TODO: fazer comentários

def sendhotspot(json_dict: dict):
    print("Sending hotspot")

    url = "https://www.zeropipe.com.br/v1/entry_raws"
    headers = {"Accept": "application/json", "Content-type": "application/json"}

    jsonStr_encoded = base64.b64encode(json.dumps(json_dict).encode('utf-8'))

    print("jsonStr_encoded: " + str(jsonStr_encoded.decode('utf-8')))
    json_final = {"entry_raw": {"payload": str(jsonStr_encoded.decode('utf-8') + "=\n")}}

    response = requests.post(url, headers=headers, json=json_final, verify=False)

    print("status code", response.status_code)
    print("response.json()", response.json())



#Considera o formato AM PM
#Considera o formato AM PM
def convert_date_to_seconds(time: str) -> int:

    str1 = time
    new_time = ""
    # checking last two elements of time
    # if it is AM and first two elements are 12
    if str1[-2 :] == "AM" and str1[:2] == "12" :
        new_time = "00" + str1[2 :-2]

    # remove the AM
    elif str1[-2 :] == "AM" :
        new_time = str1[:-2]

    # If last two elements of time is PM
    # and first two elements are 12
    elif str1[-2 :] == "PM" and str1[:2] == "12" :
        new_time =  str1[:-2]

    else :
        # remove PM and add 12 to hours
        new_time = str( int( str1[:2] ) + 12 ) + str1[2:8]

    # print(f"(convert_data_to_seconds) horário recebido: {time[:4]}")
    hour = int(new_time[:2])
    minute = int(new_time[2:4])
    to_seconds = (hour*60) + minute
    return to_seconds

def getschedule() -> dict:
    """"
    Pega os horários que é permitido executar
    """
    token = passwords.ler_token()
    r = requests.get(f'https://www.zeropipe.com.br/v1/hotspots/{token}.json', verify=False)
    r = r.json()
    hotspot = r['hotspot']
    # TODO: lidar com erros
    schedule = {'active': hotspot['active'], 'sun': hotspot['sun'], 'mon': hotspot['mon'], 'tue': hotspot['tue'],
                'wed': hotspot['wed'], 'thu': hotspot['thu'], 'fri': hotspot['fri'], 'sat': hotspot['sat'],
                'start_time': convert_date_to_seconds(hotspot['start_time_str']),
                'end_time': convert_date_to_seconds(hotspot['end_time_str']), "chosen_process_name": hotspot['chosen_process_name']}

    return schedule
