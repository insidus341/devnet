from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from tools.api_key import key
from get_organization_id import get_org_id

meraki = MerakiSdkClient(key)

def get_network_id():
    org_id = get_org_id()
    if org_id is False:
        return False

    network_controller = meraki.networks
    params = {}
    params['organization_id'] = org_id

    networks = network_controller.get_organization_networks(params)
    for network in networks:
        net_name = network['name']
        net_id = network['id']
        # print("{} - {}".format(net_name, net_id))

        if net_name == 'Home':
            return net_id

    return False
