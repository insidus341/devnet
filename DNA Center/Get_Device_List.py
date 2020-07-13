import requests
import json
from Get_Token import get_api_token

request = requests.session()

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"
request.headers = {
    'x-auth-token': get_api_token(),
    'Content-Type': 'application/json'
}
request.querystring = {
    'timestamp': ''
}

response = request.get(url, verify=False).json()


for device in response['response']:
    print('*' * 30)
    print("Device: {}".format(device))
    print('*' * 30)