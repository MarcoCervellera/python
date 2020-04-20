import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
#print(flights.head())

#sns.heatmap(tips.corr(), annot=True, lw=3, linecolor="black", cmap="cool")

flightPivot = flights.pivot_table(index='month', columns="year", values="passengers")
sns.heatmap(flightPivot, annot=False, lw=1, cmap="cool")
#sns.clustermap(flightPivot)
sns.set_context("paper")
#rimuove bordi
sns.despine()
plt.show()