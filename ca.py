import pandas as pd
import numpy as np
from scipy.spatial import distance
# dst = distance.euclidean(a, b)

df = pd.read_csv('large-dataset.csv')
rows = rows = df['name'].values.tolist()
df['min'] =  (df['o1'] + df['c1'] + df['e1'] + df['a1'] + df['n1']) /5
df['max'] =   (df['o2'] + df['c2'] + df['e2'] + df['a2'] + df['n2']) /5
df.set_index('name', inplace=True)

newdf = pd.DataFrame(index=rows,columns=rows)

for index,rec in df.iterrows():
  # print(index)
  # print('---')
  now = [rec['min'],rec['max']]
  for sindex,srec in df.iterrows():
    # print(sindex)
    sub = [srec['min'],srec['max']]
    new_value = distance.euclidean(now,sub)
    newdf.at[index,sindex] = new_value
print(newdf)