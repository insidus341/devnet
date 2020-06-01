from pprint import pprint

import requests
from get_token import get_token

cookies = get_token()
url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/34].json?"

payload = {}
headers = {}

response = requests.get(url, headers=headers, data=payload, cookies=cookies, verify=False).json()
pprint(response)