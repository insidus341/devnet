from pprint import pprint
import xmltodict
from ncclient import manager

from device_configs.csr_1000_devnet import router

filter_template = open(
    'yang/ietf_get_interfaces.xml'
).read()

netconf_filter = filter_template.format(
    interface=''
)

with manager.connect(
    host=router['host'],
    port=router['port'],
    username=router['username'],
    password=router['password'],
    hostkey_verify=False
) as m:
    requested_config = m.get(netconf_filter)
    requested_config_xml = xmltodict.parse(requested_config.xml)['rpc-reply']['data']

    handler = requested_config_xml['interfaces']['interface']

    if isinstance(handler, dict):
        print(handler['name']['#text'])
        print(handler['description'])

    elif isinstance(handler, list):
        for interface in handler:
            print(f"Name: { interface['name'] }")
            try:
                print(f"Description: { interface['description'] }")
            except:
                pass
            print("*" * 50)
            print()