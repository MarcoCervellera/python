import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

#sns.countplot(x='day', data=tips)
#sns.pointplot(x='day', y="total_bill", data=tips)
#sns.swarmplot(x="smoker", y="tip", data=tips, hue="sex")
#sns.stripplot(x="smoker", y="tip", data=tips, hue="sex")
#sns.barplot(x='day', y='tip', data=tips)
#sns.boxenplot(x='day', y='tip', data=tips)
sns.violinplot(x='day', y='tip', data=tips)
plt.show()