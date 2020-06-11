import requests
import json
from Get_Room import get_room
room_id = get_room('WebEx Automation')
print(room_id)

key = 'NDQ0ZTQ4ZTUtMDNhOC00MmE2LTgyZjYtNTUwODA4OTYwNDJlMDA2YzllMGQtY2Ew_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
url = "https://webexapis.com/v1/messages?roomId="+room_id

request = requests.session()
request.headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}

data = {
    "roomId": room_id
}

# data=json.dumps(data) is not working
# it works as a query though

response = request.get(url, data=json.dumps(data), verify=False).json()

messages = response['items']
for message in messages:
    msg = message['text']
    print(msg)
