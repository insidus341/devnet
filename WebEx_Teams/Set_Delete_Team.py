import requests
import json
from tools.api_key_webex import key
from Get_Team import get_team


team_id = get_team()
if team_id is None:
    exit()

url = "https://webexapis.com/v1/teams/" + team_id



request = requests.session()
request.headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}

response = request.delete(url, verify=False).json()
print(response)
