import requests
import json
from FirepowerFMC.Get_Token import get_access_token

url = "https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies?limit=400"
session = requests.session()
session.headers = get_access_token()

response = session.get(url, verify=False).json()
policies = response['items']

for policy in policies:
    print('*' * 50)
    p_name = policy['name']
    p_id = policy['id']
    p_type = policy['type']
    p_link = policy['links']['self']

    print(f"Name: {p_name}")
    print(f"Id: {p_id}")
    print(f"Type: {p_type}")
    print(f"Link: {p_link}")
    print('*' * 50)



