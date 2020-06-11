from pprint import pprint

from dnacentersdk import DNACenterAPI

api = DNACenterAPI(
    username='devnetuser',
    password='Cisco123!',
    base_url='https://sandboxdnac2.cisco.com',
    version='1.2.10'
)

vlan_id = 'Vlan20'

topology_details = api.networks.get_topology_details(vlan_id)
pprint(topology_details)
