import requests

def get_token():
    url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

    payload = "{\n\t\"aaaUser\":{\n\t\t\"attributes\":{\n\t\t\t\"name\": \"admin\",\n\t\t\t\"pwd\": \"Admin_1234!\"\n\t\t}\n\t}\n}"
    headers = {
      'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, data=payload, verify=False).json()
    token = response['imdata'][0]['aaaLogin']['attributes']['token']
    print(token)

    cookies={}
    cookies['APIC-cookie'] = token

    return cookies
