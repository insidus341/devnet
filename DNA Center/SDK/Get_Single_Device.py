from pprint import pprint

from dnacentersdk import DNACenterAPI

api = DNACenterAPI(
    username='devnetuser',
    password='Cisco123!',
    base_url='https://sandboxdnac2.cisco.com',
    version='1.2.10'
)

id = '85daf2da-571a-4570-9ce3-c68867ad891a'
devices = api.devices.get_device_by_id(id)
pprint(devices)
