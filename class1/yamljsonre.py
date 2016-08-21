#!/usr/bin/env python

import json
import yaml
from pprint import pprint

with open("lista.json") as f:
    lista_json = json.load(f)
f.close()
print("read from json file")
pprint(lista_json)


with open("lista.yaml")as g:
    lista_yaml = yaml.load(g)
g.close()
print("read from yaml file")
pprint(lista_yaml)

