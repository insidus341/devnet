import xmltodict

stream = open('xml_data.xml')
xml = xmltodict.parse(stream.read())

for e in xml['people']['person']:
    print(e['@id'])
    print(e['lname'])