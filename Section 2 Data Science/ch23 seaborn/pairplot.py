import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dots = sns.load_dataset('dots')

print(dots.head())
#genera tutti i possibile grafici ottenibili dal dataset
#sns.pairplot(dots)
#è possibile includere parametri non numerici
sns.pairplot(dots, hue="align")
plt.show()