from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from tools.api_key import key
from get_network_id import get_network_id
from tools.sdk_create_organization_network import CreateOrganizationNetworkModel

meraki = MerakiSdkClient(key)
network_id = get_network_id()
vlan_controller = meraki.vlans

params = {}
params['network_id'] = network_id
params['update_network_vlans_enabled_state'] = {
    "enabled": "true"
}

vlans_enabled_state = vlan_controller.get_network_vlans_enabled_state(network_id)
if vlans_enabled_state['enabled'] == False:
    vlans_enabled = vlan_controller.update_network_vlans_enabled_state(params)
    print(vlans_enabled)