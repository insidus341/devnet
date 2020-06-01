from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from tools.api_key import key
from get_network_id import get_network_id

meraki = MerakiSdkClient(key)

net_id = get_network_id()
clients_controller = meraki.clients

params = {}
params['network_id'] = net_id
clients = clients_controller.get_network_clients(params)
for client in clients:
    cli_id = client['id']
    cli_ip = client['ip']
    print("{} - {}".format(cli_id, cli_ip))