import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x

fig = plt.figure()
#coordinate x,y,width,height
x1 = fig.add_axes([0.1,0.1,1,1])
x2 = fig.add_axes([0.1,0.1,0.3,0.3])
x1.plot(x,y)
x2.plot(y,x)
plt.show()

fig, axes = plt.subplots(2,2)

axes[0,0].plot(x,y)
axes[1,0].plot(x,x)
axes[1,1].plot(y,x)
axes[0,1].plot(y,y)
plt.tight_layout()
plt.show()