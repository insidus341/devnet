import requests
import json
from device_configs.csr_1000_devnet import router

print(router)
session = requests.Session()
session.auth = (router['username'], router['password'])
session.headers = ({
    'Accept': 'application/yang-data+json, application/yang-data.errors+json',
    'Content-Type': 'application/yang-data+json'
})

host = router['host']
port = router['port']
url = "https://{}:{}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet3".format(host, port)

data = {
    'ietf-interfaces:interface': {
        'name': 'GigabitEthernet3', 
        'description': 'Set via Restconf and Python!',
        'type': 'iana-if-type:ethernetCsmacd',
    }
}
response = session.put(url, json=data, verify=False)
print(response)
# print(response.json())

