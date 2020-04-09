#Richiede input all'utente
x = input("Write the first value: ")
y = input("Write the second value: ")
#Attenzione, tutti gli input sono interpretati come String in Python3
#In python2 vengono presi come sono
z = x + y
print(z)
z = int(x) + int(y)
print(z)