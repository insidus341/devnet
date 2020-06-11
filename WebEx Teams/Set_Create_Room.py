import requests
import json
from Get_Team import get_team

key = 'NDQ0ZTQ4ZTUtMDNhOC00MmE2LTgyZjYtNTUwODA4OTYwNDJlMDA2YzllMGQtY2Ew_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
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
