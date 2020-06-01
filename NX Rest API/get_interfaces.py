from pprint import pprint

import requests
from get_token import get_token

cookies = get_token()
url = "https://sbx-nxos-mgmt.cisco.com/api/node/class/l1PhysIf.json?"

payload = {}
headers = {}

response = requests.get(url, headers=headers, data=payload, cookies=cookies, verify=False).json()
pprint(response)