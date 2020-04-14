#Una funzione è un pezzo di codice con un task specifico
#Ha funzione di organizzazione del codice

def add(x,y=0):
    x = int(x)
    y = int(y)
    z = x + y
    return z

x = input("Enter first value: ")
y = input("Enter second value: ")
c = add(x,y)
print(c)
#possibile perchè abbiamo specificato un valore di default per y
c = add(x)
print(c)