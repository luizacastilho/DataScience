import pandas as pd
import numpy as np

x = pd.read_csv('C:\\Users\\luiza\\Documents\\2022.2\\DEC7553 - Topicos Especiais III\\Lista2A\\ex2a - Página1.csv', header=None)
y = pd.read_csv('C:\\Users\\luiza\\Documents\\2022.2\\DEC7553 - Topicos Especiais III\\Lista2A\\ex2b - Página1.csv', header=None)

print("Adicao de meatrizes")
if (x.shape == y.shape):
    print(np.add(x, y))

print("Multiplicacao de matrizes")
if (x.shape[1] == y.shape[0]):
    print(np.dot(x, y))

