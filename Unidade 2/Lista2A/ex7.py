from collections import Counter

with open('ciência_de_dados.txt') as file:
    contagem= Counter(file.read().split())
    print(contagem)