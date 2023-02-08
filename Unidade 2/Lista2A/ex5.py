from lib2to3.pgen2.pgen import DFAState
import numpy as np 
import pandas as pd 


dfa = pd.DataFrame(np.random.randint(5, size=(3, 3)))
print (dfa)
dfb = pd.DataFrame(np.random.randint(9, size=(3,3)))
print(dfb)

multiplicacao = dfa.mul(dfb)

print(multiplicacao)