import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df1 = sns.load_dataset('tips')
df2 = pd.read_csv('iris.csv')

x1 = np.random.rand(100,5)
x2 = np.random.rand(10,5)

df3 = pd.DataFrame(x1, columns=["a", "b", "c", "d", "e"])
df4 = pd.DataFrame(x2, columns=["a", "b", "c", "d", "e"])

#df3.plot.scatter(x='a', y='b')
#df3["a"].plot.line()
#df4.plot.kde()
#df4.hist()
#df4.plot.bar()
df4.plot.area()

plt.show()