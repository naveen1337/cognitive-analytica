import pandas as pd
import numpy as np
from scipy.spatial import distance
from pymongo import MongoClient
import os
# dst = distance.euclidean(a, b)

df = pd.read_csv('dataset.csv')
rows = rows = df['name'].values.tolist()
df['min'] =  (df['o1'] + df['c1'] + df['e1'] + df['a1'] + df['n1']) /5
df['max'] =   (df['o2'] + df['c2'] + df['e2'] + df['a2'] + df['n2']) /5
df.set_index('name', inplace=True)

newdf = pd.DataFrame(index=rows,columns=rows)

for index,rec in df.iterrows():
  now = [rec['min'],rec['max']]

  for sindex,srec in df.iterrows():

    sub = [srec['min'],srec['max']]
    new_value = distance.euclidean(now,sub)
    newdf.at[index,sindex] = new_value
# print(newdf)

# MongoDB connection
client = MongoClient(os.getenv("DB_URI"))

db = client['cadb']
collection = db['cascore']

data = newdf.to_dict()
row = newdf.index.values.tolist()
for key in row:
  newobj = {
            'name':key,
            'similar':data[key]
            } 
  rec_id = collection.insert_one(newobj).inserted_id 
  print(rec_id)         
  # print(newobj)
  # print('\n')  


