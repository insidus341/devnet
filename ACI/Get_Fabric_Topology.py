import os
from pprint import pprint
from Get_Token import get_api_token
import requests
import json

url = "https://sandboxapicdc.cisco.com/api/mo/topology.json?query-target=children"
headers = {
    "Content-Type": "application/json"
}
cookie = {
    "APIC-cookie": get_api_token()
}

payload = {}


api_request = requests.session()
api_request.headers = headers
response = api_request.request(url=url, data=json.dumps(payload), cookies=cookie, method='GET',
                               verify=False).json()

pprint(response)
