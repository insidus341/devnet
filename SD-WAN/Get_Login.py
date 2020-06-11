import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://sandboxsdwan.cisco.com:8443/j_security_check"

data = {
    "j_username": "devnetuser",
    "j_password": "Cisco123!"
}

session = requests.session()
response = session.post(url, data=data, verify=False)

if response.text:
    print("Auth failure")
    exit()
else:
    print('*' * 50)
    print("Auth succeeded")
    print('*' * 50)
    print()


# Get devices
url = "https://sandboxsdwan.cisco.com:8443/dataservice/device"
data = {}

response = session.get(url, verify=False).json()
devices = response['data']

for device in devices:
    print('*' * 50)
    device_ip = device['system-ip']
    device_hostname = device['host-name']
    device_reachability = device['reachability']
    device_model = device['device-model']

    print(f"IP: {device_ip}")
    print(f"Hostname: {device_hostname}")
    print(f"Model: {device_model}")
    print(f"Status: {device_reachability}")
    print('*' * 50)
    print()

