from lxml import etree as et

stream = open('xml_data.xml')
xml = et.parse(stream)
xml_root = xml.getroot()

for person in xml_root:
    print(et.tostring(person))
    print("")
    print(person.get('id'))
