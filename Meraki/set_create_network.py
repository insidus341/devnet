from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from tools.api_key import key
from get_organization_id import get_org_id
from tools.sdk_create_organization_network import CreateOrganizationNetworkModel

meraki = MerakiSdkClient(key)
org_id = get_org_id()
network_controller = meraki.networks

params = {}
params['organization_id'] = org_id
params['create_organization_network'] = {
    "name": 'James test',
    "type": "appliance",
    "timeZone": 'Europe/London',
    "tags": 'tag1',
}

network = network_controller.create_organization_network(params)
network_id = network['id']
print(network_id)
