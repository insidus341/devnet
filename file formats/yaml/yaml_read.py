import yaml
from yaml import load, load_all

with open('yaml_data.yaml') as document:
    doc = load(document, Loader=yaml.FullLoader)
    people = doc['people']

    print(type(people))

    for person in people:
        print(type(person))
        print(person)
        print(person['fname'])
        print(type(person['fname']))
