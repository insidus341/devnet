from pprint import pprint

from acitoolkit.acitoolkit import *

url = "https://sandboxapicdc.cisco.com"
user = "admin"
pwd = "ciscopsdt"

session = Session(url, user, pwd)
session.login()

# Create the Tenant
new_tenant = Tenant("James_Tenant")
new_tenant.descr = 'Via Python'

# Create the app profile and EPG
new_app = AppProfile('James_app', new_tenant)
new_epg = EPG('James_epg', new_app)

# Create the L3 Namespace
new_context = Context('James_context', new_tenant)
new_bridge_domain = BridgeDomain('James_bd', new_tenant)

# Associate the BD with the L3 Namespace
new_bridge_domain.add_context(new_context)
new_epg.add_bd(new_bridge_domain)

# # # DONE # # #
print(new_tenant.get_url())
print(new_tenant.get_json())
print()

response = session.push_to_apic(
    new_tenant.get_url(), data=new_tenant.get_json()
)

tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'James_Tenant':
        print(tenant.name)
        print(tenant.descr)
