from pprint import pprint

import requests
import json
from Get_Token import get_api_token

request = requests.session()

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-detail"
request.headers = {
    'x-auth-token': get_api_token(),
    'Content-Type': 'application/json'
}
request.querystring = {
    'timestamp': '',
    'macAddress': '00:00:2A:01:00:50'
}

response = request.get(url, verify=False).json()
pprint(response)