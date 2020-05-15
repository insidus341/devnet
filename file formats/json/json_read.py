import json

jsonobj = json.load(open('json_data.json'))

for person in jsonobj['people']:
    print(person)
    print(person['id'])

