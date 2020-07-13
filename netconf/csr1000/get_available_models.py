from pprint import pprint
import xmltodict
from ncclient import manager

from device_configs.csr_1000_devnet import router

with manager.connect(
    host=router['host'],
    port=router['port'],
    username=router['username'],
    password=router['password'],
    hostkey_verify=False
) as m:
    containers = m.server_capabilities
    for container in containers:

        search = 'interface'
        if search in str(container):
            print(container)
