from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from tools.api_key import key
from get_network_id import get_network_id
from tools.sdk_create_organization_network import CreateOrganizationNetworkModel

meraki = MerakiSdkClient(key)
network_id = get_network_id()
vlan_controller = meraki.vlans

params = {}
params['network_id'] = network_id
params['create_network_vlan'] = {
    "id": "100",
    "name": "API VLAN",
    "subnet": "10.0.0.0/24",
    "applianceIp": "10.0.0.1"
}

vlan_controller.create_network_vlan(params)