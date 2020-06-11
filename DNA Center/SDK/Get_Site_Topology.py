from pprint import pprint

from dnacentersdk import DNACenterAPI

api = DNACenterAPI(
    username='devnetuser',
    password='Cisco123!',
    base_url='https://sandboxdnac2.cisco.com',
    version='1.2.10'
)

site_topology = api.networks.get_site_topology()
pprint(site_topology)


