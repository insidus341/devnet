from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='NDQ0ZTQ4ZTUtMDNhOC00MmE2LTgyZjYtNTUwODA4OTYwNDJlMDA2YzllMGQtY2Ew_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f')
teams = api.teams.list()
my_room_id = None

for team in teams:
    team_name = team.name
    team_id = team.id

    if team_name == 'James - DevNetStudies':

        rooms = api.rooms.list(team_id)
        for room in rooms:
            room_name = room.title
            room_id = room.id

            if room_name == 'WebEx Automation':
                message = 'Sent with the Python WebEx SDK'
                api.messages.create(roomId=room_id, text=message)

