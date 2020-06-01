from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from tools.api_key import key
from get_network_id import get_network_id

meraki = MerakiSdkClient(key)

net_id = get_network_id()
devices_controller = meraki.devices
devices = devices_controller.get_network_devices(net_id)
for device in devices:
    de_mac = device['mac']
    print("MAC - {}".format(de_mac))