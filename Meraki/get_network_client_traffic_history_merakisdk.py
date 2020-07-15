import meraki
from tools.api_key import key
from get_network_id import get_network_id

dashboard = meraki.DashboardAPI(key)

# net_id = get_network_id()
network_id = 'L_594475150812909110'
client_id = 'k01816e'

traffichistory = dashboard.networks.getNetworkClientTrafficHistory(
    network_id, client_id, startingAfter='2019-10-11T00:00:00.000000Z'
)

print(traffichistory)