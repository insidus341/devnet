from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from tools.api_key import key

meraki = MerakiSdkClient(key)


def get_org_id():
    organization_controller = meraki.organizations
    orgs = organization_controller.get_organizations()

    org_id = None
    for org in orgs:
        org_name = org['name']
        org_id = org['id']
        # print("{} - {}".format(org_name, org_id))

        if org_name == 'James Earl - original':
            return org_id

    return False


# print()
# params = {}
# params['network_id'] = net_id
# clients = clients_controller.get_network_clients(params)
# for client in clients:
#     cli_id = client['id']
#     cli_ip = client['ip']
#     print("{} - {}".format(cli_id, cli_ip))
#
#
#



