import requests
import json
from FirepowerFMC.Get_Token import get_access_token
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_access_policy(token=False):

    url = "https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies?limit=400"
    session = requests.session()
    session.headers = get_access_token(token)

    response = session.get(url, verify=False).json()
    policies = response['items']

    for policy in policies:
        p_name = policy['name']
        p_id = policy['id']
        p_type = policy['type']
        p_link = policy['links']['self']

        if p_name == 'James Policy Demo':

            response = session.get(p_link, verify=False).json()
            policyrules = response['rules']

            print(f"Name: {p_name}")
            print(f"Id: {p_id}")
            print(f"Type: {p_type}")
            print(f"Rules")

            if type(policyrules) == list:
                for rule in policyrules:
                    r_type = rule['type']
                    r_link = rule['links']['self']

                    print(f"{r_link}")
                    print('*' * 50)

            else:
                print(f"Type: {policyrules['type']}")
                print(f"{policyrules['links']['self']}")

            return p_id

    return None


if __name__ == "__main__":
    get_access_policy()

