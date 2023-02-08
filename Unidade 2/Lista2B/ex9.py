import pandas as pd

df = pd.read_csv (r'netflix1.csv')

df.sort_values("type", inplace = True)

data = pd.DataFrame(df, columns= ['title','country'])
print(data)