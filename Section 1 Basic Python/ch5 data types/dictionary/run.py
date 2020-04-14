#i dizionari vengono inizializzati con parentesi graffe
x = {}
print(x)
#I dizionari rappresentano coppie chiave-valore separati da virgola
x = {"number" : "1", "name" : "Marco"}
#Si può accedere ai valori usando le chiavi
print(x["name"])
#il metodo len resituisce il numero di elementi nel dizionario
print(len(x))
#il metodo pop rimuove e resituisce l'elemento relativo alla chiave indicata
print(x.pop("number"))
print(x)
#se vogliamo rimuovere l'ultimo elemento inserito dovremo usare il metodo popitem
x["age"] = 2019
print(x)
print(x.popitem())
print(x)