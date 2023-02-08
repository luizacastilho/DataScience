import pandas as pd
from collections import Counter

with open('ciência_de_dados.txt') as file:
    contagem= Counter(file.read().split())
    print(contagem)

df = pd.DataFrame.from_dict(contagem, orient='index').reset_index()
print(df)