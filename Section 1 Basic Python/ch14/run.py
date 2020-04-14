import numpy as np
import matplotlib.pyplot as plt
from module import add

x = [[1,2,3],[4,5,6],[7,8,9]]
a = np.array(x)
print(a)

x = np.linspace(0,10, 100)
y = x ** 2
plt.plot(x,y)
plt.show()
add(1,2)