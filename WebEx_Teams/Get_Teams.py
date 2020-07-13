import requests
import json
from tools.api_key_webex import key

url = "https://webexapis.com/v1/teams"

request = requests.session()
request.headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}

response = request.get(url, verify=False).json()
print(response)

teams = response['items']
for team in teams:
    team_id = team['id']
    team_name = team['name']

    print(team_name)
    print(team_id)
    print('*' * 30)


