import requests
import json
from FirepowerFMC.Get_Application_Policy import get_access_policy
from FirepowerFMC.Get_Token import get_access_token
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = get_access_token()
policy_id = get_access_policy(headers['X-auth-access-token'])

url = f"https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policy_id}"
response = requests.delete(url, headers=headers, verify=False).json()
print(response)