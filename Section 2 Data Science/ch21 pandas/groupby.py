import numpy as np
import pandas as pd

p = {
    "item":['apple', 'apple', 'orange', 'orange', 'guns', 'guns'], 
    'days':['mon', 'tue', 'wed', 'thu', 'fri', 'sat'],
    'sales': [100,80,200,100,5,10]
    }

df = pd.DataFrame(p)
print(df.groupby('item').describe())
