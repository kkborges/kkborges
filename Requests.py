import base64
import ssl

import requests


url = "https://shrouded-spire06255.herokuapp.com/v1/entry_raws"
print(url)
headers = {"Accept: application/json" "Content-type: application/json"}

print(headers)

jsonStr = '{ "hotspot": { "hostname": "DESK932LK-ELO", "os": "WINDOWS", "os_version": "10", "token": "22111548-c912-427f-8f8f-b138c83c5cf5", "ip":"120.211.3.111", "download_speed_mbps": "90", "upload_speed_mbps": "15", "host":{ "cpu_perc": "99", "ram_perc": "50", "disk_usage_perc": "22", "top_processes": [ { "name": "lua.exe", "cpu_perc": "99", "ram_perc": "50", "disk_usage_perc": "22" } ], "chosen_processes": [ { "name": "teamviewer.exe", "cpu_perc": "99", "ram_perc": "50", "disk_usage_perc": "22" } ] } } }'

jsonStr_encoded = base64.b64encode(jsonStr.encode('utf-8'))
print(jsonStr_encoded)
jsonStr_decoded = base64.b64decode(jsonStr_encoded)
json_final = ' {"entry_raw": {"payload":"' + str(jsonStr_encoded) + '=\n"}}'

print(json_final)

print(jsonStr_decoded)
response = requests.post(url, headers=headers, json=json_final)
print("status code", response.status_code)
#print("json.response", base64.b64decode(jsonStr_encoded).decode('utf-8'))
