import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(10000,5),columns=['a','b','c','d','e'])
df.describe()
#https://www.youtube.com/watch?v=CG3EV7UBELA