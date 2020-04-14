#Le liste si trovano all'interno di parentesi quadre
#Possono contenere qualsiasi tipologia di dato
x = [ 15, "Marco"]
#per accedere all'i-esimo elemento di una lista basta usare x[i]
print(x[1])
#numero di elementi di una lista len(x)
print(len(x))
#il metodo pop rimuove e ritorno l'ultimo elemento di una lista
y = x.pop()
print(y)
print(x)
#Il metodo append aggiunge un elemento in coda ad una lista
x.append(y)
print(x)
#il metodo remove rimuove gli elementi indicati
x.remove(15)
print(x)