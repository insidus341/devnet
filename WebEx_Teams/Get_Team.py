import requests
import json
from tools.api_key_webex import key

url = "https://webexapis.com/v1/teams"

def get_team():
    request = requests.session()
    request.headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }

    response = request.get(url, verify=False).json()

    teams = response['items']
    for team in teams:
        team_id = team['id']
        team_name = team['name']

        if team_name == 'James - DevNetStudies':
            print(team_id)
            return team_id

    return None


if __name__ == "__main__":
    get_team()


