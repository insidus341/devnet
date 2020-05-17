from pprint import pprint
import xmltodict
from ncclient import manager

from device_configs.csr_1000_devnet import router

filter_template = open(
    'yang/ietf_get_static_routes.xml'
).read()

netconf_filter = filter_template.format()

with manager.connect(
    host=router['host'],
    port=router['port'],
    username=router['username'],
    password=router['password'],
    hostkey_verify=False
) as m:
    requested_config = m.get(netconf_filter)
    requested_config_xml = xmltodict.parse(requested_config.xml)['rpc-reply']['data']

    routing_protocols = requested_config_xml['routing']['routing-instance']['routing-protocols']

    if isinstance(routing_protocols, list):
        for routing_protocol in routing_protocols:
            if routing_protocol['type'] == 'static':
                static_routes = routing_protocol['static-routes']
                for static_route in static_routes:
                    print(static_route)
    else:
        routing_protocol = routing_protocols['routing-protocol']
        if routing_protocol['type'] == 'static':
            route = routing_protocol['static-routes']['ipv4']['route']
            print(route['destination-prefix'])
            print(route['next-hop']['outgoing-interface'])

