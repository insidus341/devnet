import requests
import json
from Get_Team import get_team
from tools.api_key_webex import key

url = "https://webexapis.com/v1/rooms"

request = requests.session()
request.headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}

data = {
    'title': "WebEx Automation",
    'teamId': get_team()
}

response = request.post(url, data=json.dumps(data), verify=False).json()
print(response)
