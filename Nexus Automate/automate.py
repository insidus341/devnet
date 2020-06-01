import json
from pprint import pprint
import requests
from device_configs.nexus_devnet import router


############## GET CDP NEIGHBORS #############
cdp_cmd = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show cdp nei",
    "output_format": "json"
  }
})

url = "https://{}/ins".format(router['host'])

session = requests.Session()
session.headers = ({
    "Content-Type": "application/json"
})
session.auth = (router['username'], router['password'])

cdp_response = session.post(
  url,
  data=cdp_cmd,
  verify=False
).json()

cdp_nei_count = cdp_response['ins_api']['outputs']['output']['body']['neigh_count']
print("Neighbor count: {}".format(cdp_nei_count))


################## REST API ###################

url = "https://{}/api/mo/aaaLogin.json".format(router['host'])
session = requests.Session()
session.headers = ({
    "Content-Type": "application/json"
})
auth_cmd = json.dumps({
  "aaaUser": {
    "attributes":{
      "name": router['username'],
      "pwd": router['password']
    }
  }
})

auth_response = session.post(
  url,
  data=auth_cmd,
  verify=False
).json()

auth_token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = auth_token
print(auth_token)


############## SET INTERFACE DESC #############

session = requests.Session()
session.headers = ({
    "Content-Type": "application/json"
})

description = "Hello World"
description = ""
set_int_desc_cmd = json.dumps({
  "l1PhysIf": {
    "attributes": {
      "descr": description
    }
  }
})

url = "https://{}/api/node/mo/sys/intf/phys-[eth1/34].json?".format(router['host'])
get_int_response = session.put(
  url,
  data=set_int_desc_cmd,
  cookies=cookies,
  verify=False
).json()

pprint((get_int_response))


############## GET INTERFACE DESC #############
session = requests.Session()
session.headers = ({
    "Content-Type": "application/json"
})

url = "https://{}/api/node/mo/sys/intf/phys-[eth1/34].json?".format(router['host'])
get_int_response = session.get(
  url,
  cookies=cookies,
  verify=False
).json()

descr = get_int_response['imdata'][0]['l1PhysIf']['attributes']['descr']
print(descr)