import numpy as np

matriz = np.random.rand(4,4)
print(matriz)

np.savetxt('ex4.csv', matriz, delimiter=',')