from pprint import pprint
import xmltodict
from ncclient import manager

from device_configs.csr_1000_devnet import router
from tools.tools import try_print

filter_template = open(
    'yang/ietf_get_interfaces_ip.xml'
).read()

netconf_filter = filter_template.format(
    interface='GigabitEthernet1'
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

    # If there is one interface, the output will the be dict
    if isinstance(handler, dict):
        try_print('Name', handler['name']['#text'])

        if 'description' in handler:
            try_print('Description', handler['description'])

        if 'ipv4' in handler:
            # If there is one of more IP address, the output will the be list
            # else, the output will be a dict
            if isinstance(handler['ipv4']['address'], list):
                for address in handler['ipv4']['address']:

                    print()
                    try_print('IP Address', address['ip'])
                    try_print('Netmask', address['netmask'])

            else:
                # Dict, one IP address
                try_print('IP Address', handler['ipv4']['address']['ip'])
                try_print('Netmask', handler['ipv4']['address']['netmask'])

    # If there is more than one interface
    elif isinstance(handler, list):
        for interface in handler:
            try_print('Name', interface['name'])
            if 'description' in interface:
                try_print('Description', interface['description'])

            if 'ipv4' in interface:
                # If there is one of more IP address, the output will the be list
                # else, the output will be a dict
                if isinstance(interface['ipv4']['address'], list):
                    for address in interface['ipv4']['address']:

                        print()
                        try_print('IP Address', address['ip'])
                        try_print('Netmask', address['netmask'])

                else:
                    # Dict, one IP address
                    try_print('IP Address', interface['ipv4']['address']['ip'])
                    try_print('Netmask', interface['ipv4']['address']['netmask'])
            print("*" * 50)
            print()



