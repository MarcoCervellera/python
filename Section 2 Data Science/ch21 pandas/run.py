import numpy as np
import pandas as pd

x = ['a','b','c','d','e']
x2 = ['a','b','c','d','e']
y = [1,2,3,4,5]
z = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

#series
e = pd.Series(y, x)
g = pd.Series(y, x2)

print(e + g)

#dataframe
A=[1,2,3,4]
B = [5,6,7,8]
C = [9,0,1,2]
D = [3,4,5,6]
E = [7,8,9,0]

df = pd.DataFrame([A,B,C,D,E], ['a','b','c','d','e'], ['W','X', 'Y', 'Z'])
#print(df)
#aggiungere una colonna
df['P'] = df['Y'] + df['Z']
#print(df)

#rimuovere una riga
df.drop('e', inplace = True)
#print(df)

#rimuovere una colonna
df.drop('P', axis=1, inplace= True)
#accedere a una colonna
#print(df['X'])
#accedere a una riga
#print(df.loc['a'])
#per accedere un elemento
#print(df.loc['a','X'])
#accedere a una riga per indice numerico
#print(df.iloc[1])
#accesso condizionato
print(df[df['X'] > 3])