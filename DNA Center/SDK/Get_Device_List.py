from pprint import pprint

from dnacentersdk import DNACenterAPI

api = DNACenterAPI(
    username='devnetuser',
    password='Cisco123!',
    base_url='https://sandboxdnac2.cisco.com',
    version='1.2.10'
)

devices = api.devices.get_device_list()
pprint(devices)
