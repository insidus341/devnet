import requests
import json
from Get_Team import get_team

key = 'NDQ0ZTQ4ZTUtMDNhOC00MmE2LTgyZjYtNTUwODA4OTYwNDJlMDA2YzllMGQtY2Ew_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
url = "https://webexapis.com/v1/rooms"

def get_rooms():
    request = requests.session()
    request.headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }

    team_id = get_team()

    data = {
        'teamId': team_id
    }

    response = request.get(url, data=json.dumps(data), verify=False).json()
    print(response)

    rooms = response['items']
    for room in rooms:

        if 'teamId' in room and room['teamId'] == team_id:
            room_id = room['id']
            room_title = room['title']

            print()
            print('*' * 50)
            print(f"Room ID: {room_id}")
            print(f"Room Nmae: {room_title}")
            print('*' * 50)

    return rooms


if __name__ == "__main__":
    get_rooms()