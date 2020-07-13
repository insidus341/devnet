import requests
import json
from tools.api_key_webex import key

url = "https://webexapis.com/v1/teams"

request = requests.session()
request.headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}
data = {
    "name": "James - DevNetStudies"
}

response = request.post(url, data=json.dumps(data), verify=False).json()
print(response)

