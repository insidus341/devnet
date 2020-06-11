import os
from pprint import pprint
from Get_Token import get_api_token
import requests
import json

url = "https://sandboxapicdc.cisco.com/api/mo/uni/tn-Heroes/ap-Save_The_Planet.json"
headers = {
    "Content-Type": "application/json"
}
cookie = {
    "APIC-cookie": get_api_token()
}

payload = {
    'fvAp': {
        'attributes': {
            "descr": "",
            "dn": "uni/tn-Heroes/ap-Save_The_Planet"
        }
    }
}


api_request = requests.session()
api_request.headers = headers
response = api_request.request(url=url, data=json.dumps(payload), cookies=cookie, method='POST',
                               verify=False).json()

pprint(response)
