import requests
import json

team_id = 'Y2lzY29zcGFyazovL3VzL1RFQU0vMmEyZGMwMDAtYTcxMy0xMWVhLTlmM2ItMTdjMTQxZjAyMjdk'

key = 'NDQ0ZTQ4ZTUtMDNhOC00MmE2LTgyZjYtNTUwODA4OTYwNDJlMDA2YzllMGQtY2Ew_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
url = "https://webexapis.com/v1/teams/" + team_id



request = requests.session()
request.headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}
data = {
    "id": "Y2lzY29zcGFyazovL3VzL1RFQU0vNGJjOWFlYTAtYTcxMi0xMWVhLWI3YTgtYzNmZjYzMzNhMTQx"
}

response = request.delete(url, verify=False).json()
print(response)
