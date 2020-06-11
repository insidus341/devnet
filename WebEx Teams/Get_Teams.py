import requests
import json

key = 'NDQ0ZTQ4ZTUtMDNhOC00MmE2LTgyZjYtNTUwODA4OTYwNDJlMDA2YzllMGQtY2Ew_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
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


