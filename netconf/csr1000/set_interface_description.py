from pprint import pprint
import xmltodict
from ncclient import manager
from device_configs.csr_1000_devnet import router

config_template = open(
    'yang/ietf_set_interface_description.xml'
).read()

netconf_config = config_template.format(
    interface='GigabitEthernet3',
    description='Interface'
)

with manager.connect(
    host=router['host'],
    port=router['port'],
    username=router['username'],
    password=router['password'],
    hostkey_verify=False
) as m:
    device_reply = m.edit_config(netconf_config, target='running')
    pprint(device_reply)

