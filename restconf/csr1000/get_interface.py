import requests
import json
from device_configs.csr_1000_devnet import router

print(router)
session = requests.Session()
session.auth = (router['username'], router['password'])
session.headers = ({
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
})

host = router['host']
port = router['port']
container = 'Cisco-IOS-XE-interfaces-oper'
leaf = 'interfaces'
request = 'interface'
value = 'GigabitEthernet3'
# url = "https://{}:{}/restconf/data/{}:{}/{}={}".format(host, port, container, leaf, request, value)
url = "https://{}:{}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet3".format(host, port)

response = session.get(url, verify=False)
print(response)
print(response.status_code)
json_response = response.json()
print(json_response)
exit()

interface = response.json()["{}:{}".format(container, request)]

print(interface['name'])
print(interface['description'])
if 'ipv4' in interface:
    print(interface['ipv4'])
    print(interface['ipv4-subnet-mask'])
print('*' * 50)
