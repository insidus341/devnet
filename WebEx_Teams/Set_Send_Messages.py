import requests
import json
from Get_Room import get_room
from tools.api_key_webex import key

room_id = get_room('WebEx Automation')
print(room_id)

url = "https://webexapis.com/v1/messages"

request = requests.session()
request.headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}

data = {
    "roomId": room_id,
    "text": "This is a new message"
}

# data=json.dumps(data) is not working
# it works as a query though

response = request.post(url, data=json.dumps(data), verify=False).json()
if 'id' in response:
    print('Message Sent')