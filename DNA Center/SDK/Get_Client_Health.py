from pprint import pprint

from dnacentersdk import DNACenterAPI

api = DNACenterAPI(
    username='devnetuser',
    password='Cisco123!',
    base_url='https://sandboxdnac2.cisco.com',
    version='1.2.10'
)

client_health = api.clients.get_overall_client_health()
pprint(client_health)


for site in client_health['response']:
    print('*' * 30)
    print("Site ID: {}".format(site['siteId']))
    print('*' * 30)

    for scoreType in site['scoreDetail']:
        client_category = scoreType['scoreCategory']['value']
        client_count = scoreType['clientCount']

        print("{} Clients: {}".format(client_category, client_count))

        if 'scoreList' in scoreType:
            for score_state in scoreType['scoreList']:
                score_state_category = score_state['scoreCategory']['value']
                score_state_client_count = score_state['clientCount']
                print("{:>10} Clients: {}".format(score_state_category, score_state_client_count))

        print('*' * 30)
        print()


