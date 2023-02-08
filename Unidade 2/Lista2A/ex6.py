import pandas as pd

i = 1
for chunk in pd.read_csv('ex6.csv', chunksize=2000):
    chunk.to_csv('ex6parte'+str(i)+'.csv')
    i = i + 1

