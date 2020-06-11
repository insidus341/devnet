import requests
import json

def get_access_token(token=False):

    if token is False:
        url = "https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/auth/generatetoken"
        request = requests.session()
        request.auth = ('jamearl', 'e66Z7VGQ')
        request.headers = {
            "Content-Type": "application/json"
        }

        response = request.post(url, verify=False)
        token = response.headers.get('X-auth-access-token', default=None)

    headers = {
        "X-auth-access-token": token,
        "Content-Type": "application/json"
    }

    print(headers)
    return headers


if __name__ == "__main__":
    get_access_token()
