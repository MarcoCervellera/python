import numpy as np 

x = [[1,2,3], [4,5,6], [7,8,9]]

#dichiara un array numpy
y = np.array(x)
print(y)

#dichiarare una matrice di zeri
zeroMatrix = np.zeros((3,3))
print(zeroMatrix)

#matrice di 1
oneMatrix = np.ones((3,4))
print(oneMatrix)

#matrice identità
I = np.eye(3)
print(I)

#array con elementi in un range
arange = np.arange(10)
print(arange)

#reshape cambia la forma di un array
reshape = np.arange(50).reshape(5,10)
print(reshape)

#linear space genera un array con valori nel range specificato, un terzo parametro indica quanti generarne
linspace = np.linspace(0,1)
print(linspace)

#i seguenti restituiscono i valori minimi e massimi degli array
print(linspace.min())
print(linspace.argmin())
print(linspace.max())
print(linspace.argmax())

#numpy ci permette anche di generare valori casuali
print(np.random.rand(5))

#anche negativi
print(np.random.randn(5))

#o interi
print(np.random.randint(5,100))

#indici matrice
x = np.arange(25).reshape(5,5)
print(x[2,2])
#slice matrice
print(x[2:4, :])
#condizional sull'intera matrice
print(x > 10)
#conditional selection
print(x[x>10])

#Operazioni con numpy
x = np.arange(12).reshape(3,4)
y = np.arange(10,22).reshape(4,3)

#è possibile effettuare qualsiasi operazione tra elementi di vettori
z = x * y
print(z)