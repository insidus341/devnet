from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='NDQ0ZTQ4ZTUtMDNhOC00MmE2LTgyZjYtNTUwODA4OTYwNDJlMDA2YzllMGQtY2Ew_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f')

teams = api.teams.list()

my_room_id = None

for team in teams:

    print('*' * 50)
    team_name = team.name
    team_id = team.id

    print(f"Team: {team_name}")

    rooms = api.rooms.list(team_id)
    for room in rooms:
        room_name = room.title
        room_id = room.id
        print(f"{'':>5}Room: {room_name}")

