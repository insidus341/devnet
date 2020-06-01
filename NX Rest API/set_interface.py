from pprint import pprint

import requests
from get_token import get_token
import json

cookies = get_token()
url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/34].json?"

payload = {
    "l1PhysIf":{
        "attributes":{
            "descr": ""
        }
    }
 }
headers = {}

response = requests.put(url, headers=headers, data=json.dumps(payload), cookies=cookies, verify=False).json()
pprint(response)