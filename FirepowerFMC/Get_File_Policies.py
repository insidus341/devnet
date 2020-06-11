import requests
import json
from FirepowerFMC.Get_Token import get_access_token
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/filepolicies?limit=400"
session = requests.session()
session.headers = get_access_token()

response = session.get(url, verify=False).json()
file_policies = response['items']

for file_policy in file_policies:
    print(file_policy)
