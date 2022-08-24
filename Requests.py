import base64
import requests
import requests

import json
#from hotspot import Hotspot


# import ssl

# TODO: mudar nome?
url = "https://shrouded-spire-06255.herokuapp.com/v1/entry_raws"
headers = {"Accept": "application/json", "Content-type": "application/json"}

# TODO: Pegar valor real
# hotspot = Hotspot()
# jsonStr = hotspot.as_dict()
jsonStr = {"hotspot": {"hostname": "DESK932LK-ELO",
                       "os": "WINDOWS",
                       "os_version": "10",
                       "token": "ddba573f-ecfd-4f1f-895d-08ca8f234c5e",
                       "ip": "120.211.3.111",
                       "download_speed_mbps": "90",
                       "upload_speed_mbps": "15",
                       "host": {"cpu_perc": "99",
                                "ram_perc": "50",
                                "disk_usage_perc": "22",
                                "top_processes": [{"name": "lua.exe",
                                                   "cpu_perc": "99",
                                                   "ram_perc": "50",
                                                   "disk_usage_perc": "22"}],
                                "chosen_processes": [{"name": "teamviewer.exe",
                                                      "cpu_perc": "99",
                                                      "ram_perc": "50",
                                                      "disk_usage_perc": "22"}]
                                }
                       }
           }

jsonStr_encoded = base64.b64encode(json.dumps(jsonStr).encode('utf-8'))

print("jsonStr_encoded: " + str(jsonStr_encoded.decode('utf-8')))
json_final = {"entry_raw": {"payload": str(jsonStr_encoded.decode('utf-8') + "=\n")}}

response = requests.post(url, headers=headers, json=json_final, verify=False)
print("status code", response.status_code)
print("response.json()", response.json())