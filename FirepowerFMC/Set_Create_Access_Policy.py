import requests
import json
from FirepowerFMC.Get_Token import get_access_token
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies"

data = {
    "type": "AccessPolicy",
    "name": "James Policy Demo",
    "description": "James Demo Policy",
    "defaultAction": {
        "intrusionPolicy": {
            "name": "Security Over Connectivity",
            "type": "IntrusionPolicy",
            "id": "abbad193-46bd-4535-ade6-73cc7e76fb7b"
        },
        "variableSet": {
            "name": "Default-Set",
            "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
            "type": "VariableSet",
        },
        "type": "AccessPolicyDefaultAction",
        "logBegin": False,
        "logEnd": True,
        "sendEventsToFMC": True
    }
}

headers = get_access_token()

response = requests.post(url, headers=headers, data=json.dumps(data), verify=False).json()
policy_id = None

if 'error' not in response:
    print(response)
    print()
    policy_id = response['id']
    print(policy_id)
else:
    print(response)


# Create Rules for Policy
url = f"https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policy_id}"
rules_url = f"{url}/accessrules"
rules_payload = {
    "action": "ALLOW",
    "type": "AccessRule",
    "name": "Rule1",
    "sendEventsToFMC": True,
    "logFiles": True,
    "logBegin": False,
    "logEnd": False,
    "variableSet": {
        "name": "Default Set",
        "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
        "type": "VariableSet"
    },
    "sourceNetworks": {
        "objects": [{
            "type": "NetworkGroup",
            "id": "15b12b14-dace-4117-b9d9-a9a7dcfa356f",
            "name": "IPv4-Private-All-RFC1918"
        }]
    },
    "filePolicy": {
        "name": "Malware",
        "id": "48a37aea-c382-11e9-a0df-dc4a169f7a43",
        "type": "FilePolicy"
    }
}

response = requests.post(rules_url, headers=headers, data=json.dumps(rules_payload), verify=False).json()
print(response)