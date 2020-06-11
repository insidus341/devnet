from acitoolkit.acitoolkit import *

url = "https://sandboxapicdc.cisco.com"
user = "admin"
pwd = "ciscopsdt"

session = Session(url, user, pwd)
session.login()

# Set the Tenant
new_tenant = Tenant("James_Tenant")

new_tenant.mark_as_deleted()
session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
