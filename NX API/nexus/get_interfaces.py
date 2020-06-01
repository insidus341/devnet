import requests
import json
from device_configs.nexus_devnet import router
from tools.showcmd import get_command

session = requests.Session()
session.auth = (router['username'], router['password'])
session.headers = ({
    'Content-Type': 'application/json'
})

url = 'https://{}/ins'.format(router['host'])
cmd = 'show ip int brief'
showcmd = get_command(cmd)

response = session.post(
    url,
    data=json.dumps(showcmd),
    verify=False,
).json()

print(response)