
import pandas as pd
import numpy as np
from scipy.spatial import distance
# dst = distance.euclidean(a, b)

df = pd.read_csv('dataset.csv')

def opennes():
    for (index, rec) in df.iterrows():
        now = str(rec['o']).split('.')
        lst1 = [int(now[0]), int(now[1])]
        olst = list()
        for (sindex, srec) in df.iterrows():
            srec = str(srec['o']).split('.')
            lst2 = [int(srec[0]), int(srec[1])]
            # print('comparing {} with {}'.format(lst1,lst2))
            dst = distance.euclidean(lst1, lst2)
            olst.append(dst)

        oarray = np.array(olst)
        print(oarray)
        # temp = np.array(oarray)
        # data = temp.mean()
        # for t in np.nditer(data):
        #   print("NOW {}".format(t))
def cons():
    for (index, rec) in df.iterrows():
        now = str(rec['c']).split('.')
        lst1 = [int(now[0]), int(now[1])]
        olst = list()
        for (sindex, srec) in df.iterrows():
            srec = str(srec['c']).split('.')
            lst2 = [int(srec[0]), int(srec[1])]
            # print('comparing {} with {}'.format(lst1,lst2))
            dst = distance.euclidean(lst1, lst2)
            olst.append(dst)

        oarray = np.array(olst)
        print(oarray)
        # temp = np.array(oarray)
        # data = temp.mean()
        # for t in np.nditer(data):
        #   print("NOW {}".format(t))

def extraversion():
    for (index, rec) in df.iterrows():
        now = str(rec['e']).split('.')
        lst1 = [int(now[0]), int(now[1])]
        olst = list()
        for (sindex, srec) in df.iterrows():
            srec = str(srec['e']).split('.')
            lst2 = [int(srec[0]), int(srec[1])]
            # print('comparing {} with {}'.format(lst1,lst2))
            dst = distance.euclidean(lst1, lst2)
            olst.append(dst)

        oarray = np.array(olst)
        print(oarray)
        # temp = np.array(oarray)
        # data = temp.mean()
        # for t in np.nditer(data):
        #   print("NOW {}".format(t))

def agree():
    for (index, rec) in df.iterrows():
        now = str(rec['a']).split('.')
        lst1 = [int(now[0]), int(now[1])]
        olst = list()
        for (sindex, srec) in df.iterrows():
            srec = str(srec['a']).split('.')
            lst2 = [int(srec[0]), int(srec[1])]
            # print('comparing {} with {}'.format(lst1,lst2))
            dst = distance.euclidean(lst1, lst2)
            olst.append(dst)

        oarray = np.array(olst)
        print(oarray)
        # temp = np.array(oarray)
        # data = temp.mean()
        # for t in np.nditer(data):
        #   print("NOW {}".format(t))
def neuro():
    for (index, rec) in df.iterrows():
        now = str(rec['n']).split('.')
        lst1 = [int(now[0]), int(now[1])]
        olst = list()
        for (sindex, srec) in df.iterrows():
            srec = str(srec['n']).split('.')
            lst2 = [int(srec[0]), int(srec[1])]
            # print('comparing {} with {}'.format(lst1,lst2))
            dst = distance.euclidean(lst1, lst2)
            olst.append(dst)

        oarray = np.array(olst)
        print(oarray)
        # temp = np.array(oarray)
        # data = temp.mean()
        # for t in np.nditer(data):
        #   print("NOW {}".format(t))  

print('FINAL RESULTS') 
print('\n')
print('Openness')                     
opennes()
print('\n')
print('Consciousness')
cons()
print('\n')
print('Agreeableness')
agree()
print('\n')
print('Neuroticism')
neuro()



