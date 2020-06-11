from acitoolkit.acitoolkit import *

url = "https://sandboxapicdc.cisco.com"
user = "admin"
pwd = "ciscopsdt"

session = Session(url, user, pwd)
session.login()

tenants = Tenant.get(session)
for tenant in tenants:

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
