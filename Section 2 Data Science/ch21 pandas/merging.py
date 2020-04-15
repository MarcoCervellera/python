import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'key1' : [1,2,4],
    'a': [2,3,4],
    'b': [5,6,7]
})

df2 = pd.DataFrame({
    'key1' : [1,2,3],
    'c': [2,6,7],
    'd': [5,8,9]
})

m = pd.merge(df1,df2, how="outer", on="key1")
print(m)