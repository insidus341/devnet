from acitoolkit.acitoolkit import *


url = "https://sandboxapicdc.cisco.com"
user = "admin"
pwd = "ciscopsdt"

session = Session(url, user, pwd)
session.login()

fab_devices = Endpoint.get(session)
for device in fab_devices:
    print(device)
    exit()

    if tenant.name == 'James_Tenant':
        print('*' * 30)
        print('*' * 30)
        print(tenant.name)
        print(tenant.descr)
        print('*' * 30)

    else:
        print(tenant.name)
        print(tenant.descr)

    print('*' * 30)
    print()
