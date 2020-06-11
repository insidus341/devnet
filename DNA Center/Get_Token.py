import requests
import json

def get_api_token():
    request = requests.session()

    url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
    request.auth = ('devnetuser', 'Cisco123!')
    response = request.post(url, verify=False).json()

    if response['Token']:
        return response['Token']

    return None