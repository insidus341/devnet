import requests
import json
from Get_Token import get_api_token

request = requests.session()

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"
request.headers = {
    'x-auth-token': get_api_token(),
    'Content-Type': 'application/json'
}
request.querystring = {
    'timestamp': ''
}

response = request.get(url, verify=False).json()


for site in response['response']:
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
