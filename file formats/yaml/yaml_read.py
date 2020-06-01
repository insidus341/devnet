import yaml
from yaml import load, load_all

with open('yaml_data.yaml') as document:
    # Load the YAML document
    doc = load(document, Loader=yaml.FullLoader)
    # Name and specify the document
    people = doc['people'] # list
    print(type(people))

    # can be accessed as a normal python list/dict
    for person in people: # dict
        print(type(person))
        print(person)
        print(person['fname'])
        print(type(person['fname'])) # str
