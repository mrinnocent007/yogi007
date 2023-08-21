 import pandas as pd
import numpy as np

ser1=pd.Series([10,1,4,3])
ser2=pd.Series([10,5,8,4])

u=pd.Series(np.union1d(ser1,ser2))
print(u)

i=pd.Series(np.intersect1d(ser1,ser2))
print(i)

notcommon=u[u.isin(i)]
print(notcommon)
