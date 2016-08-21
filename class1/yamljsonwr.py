#!/usr/bin/env python
import json
import yaml

lista = []
lista.append(range(10))
lista.append("hello ")
lista.append("world")
lista.append({})
lista[-1]['ipaddr'] = '10.1.1.1'
lista[-1]['model'] = 'router'

#print(lista)

with open("lista.yaml","w") as f:
    f.write(yaml.dump(lista,default_flow_style=False))
f.close()

with open("lista.json","w") as g:
    g.write(json.dumps(lista,indent =4 ))
g.close()

