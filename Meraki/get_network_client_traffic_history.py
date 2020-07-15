from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from tools.api_key import key
from get_network_id import get_network_id

meraki = MerakiSdkClient(key)

# net_id = get_network_id()
net_id = 'L_594475150812909110'
cient_id = 'k01816e'
clients_controller = meraki.clients

params = {}
params['network_id'] = net_id
params['client_id'] = 'k01816e'
client = clients_controller.get_network_client_traffic_history(params)
print(client)