import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

#a coppie inseriamo i dati da visualizzare
plt.subplot(3,2,1)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Unnecessary graph")
plt.plot(x,z)
plt.tight_layout()
plt.show()

plt.scatter(x,y)
plt.show()
plt.hist(x,y)
plt.show()
plt.bar(x,y)
plt.show()
plt.fill(x,y)
plt.show()
plt.polar(x,y)