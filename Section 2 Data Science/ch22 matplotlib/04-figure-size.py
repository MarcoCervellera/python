import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-10,10,20)
y = x * x

#settare dimensioni figura
fig = plt.figure(figsize= (5,5))
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y, color="g", linewidth="2", alpha=0.2, linestyle="steps", marker="o", markersize="20")
axes.set_xlabel("x-axis")
axes.set_ylabel("y-axis")
axes.set_title("graph")
plt.show()