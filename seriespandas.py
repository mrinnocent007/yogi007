import pandas as pd
import numpy as np
num=np.array([10,20,30,40,50])
a = pd.Series(num)
print(a)


i=pd.Index([10,20,30,40,50])
print(i.value_counts())

