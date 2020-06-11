import requests
import json
from FirepowerFMC.Get_Token import get_access_token

url = "https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/applications"
session = requests.session()
session.headers = get_access_token()

response = session.get(url, verify=False).json()
apps = response['items']

for app in apps:
    print('*' * 50)
    app_name = app['name']
    app_id = app['id']
    app_type = app['type']
    app_link = app['links']['self']

    print(f"Name: {app_name}")
    print(f"Id: {app_id}")
    print(f"Type: {app_type}")
    print(f"Link: {app_link}")
    print('*' * 50)
