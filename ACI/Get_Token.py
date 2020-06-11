import os
from pprint import pprint

import requests
import json


def get_api_token():
    url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "aaaUser": {
            "attributes": {
                "name": "admin",
                "pwd": "ciscopsdt"
            }
        }
    }

    api_request = requests.session()
    api_request.headers = headers
    response = api_request.request(url=url, data=json.dumps(payload), method='POST', verify=False).json()

    # pprint(response)

    if response['imdata'][0]['aaaLogin']['attributes']['token'] is not None:
        api_token = response['imdata'][0]['aaaLogin']['attributes']['token']
        # print(api_token)

        return api_token

    return None
