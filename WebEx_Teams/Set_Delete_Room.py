import requests
import json
from Get_Team import get_team
from tools.api_key_webex import key

roomid = 'Y2lzY29zcGFyazovL3VzL1JPT00vYjdiODY5YTAtYzFlMS0xMWVhLTg2OWMtNDU3NTQwMTQ3MmM0'
url = f"https://webexapis.com/v1/rooms/{roomid}"

request = requests.session()
request.headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}

response = request.delete(url, verify=False)

