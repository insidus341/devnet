import requests
import json
from Get_Rooms import get_rooms

def get_room(_title):
    room_title = None
    room_id = None
    room_team_id = None

    for room in get_rooms():
        try: 
            room_title = room['title']
            room_id = room['id']
            room_team_id = room['teamId']
        except:
            continue

        if room_title == _title:
            return room_id

    if room_id is None:
        exit()


if __name__ == "__main__":
    get_room('WebEx Automation')