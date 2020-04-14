#identity operator
#is controlla l'ugualianza
x = 3
y = 3.0
print(x is y)
#is not
print(x is not y)

#Membership operator
x = [1,2,3,4]
#in controlla la presenza dell'elemento nella lista
print(3 in x)
print(5 in x)
#not in
print(5 not in x)
#funziona anche con le substringhe in stringhe
print("if" in "life")