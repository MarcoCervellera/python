import json

#convertire dati in json

x = {"name" : "marco", "age": 26}

#da dizionario
y = json.dumps(x)

#da stringa
x = '{"name" : "marco", "age": 26}'
y = json.loads(x)

print(y)