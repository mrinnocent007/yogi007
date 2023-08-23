import pandas as pd
import numpy as np
num=np.array([10,20,30,40,50])
a = pd.Series(num)
print(a)


i=pd.Index([10,20,30,40,50])
print(i.value_counts())


#fillna,dropna,ets functions

import pandas as pd
import numpy as np

dict={'first score':[20,40,np.nan,50],
      'second score':[40,50,90,np.nan],
      'third score':[np.nan,20,56,20] }
data=pd.DataFrame(dict)
print(data)
print(data.isnull())
print(data.notnull())

print(data.fillna(0))
print(data.fillna(method='pad'))
print(data.fillna(method="bfill"))

print(data.replace(to_replace=np.nan,value=-99))
print(data)




##fillna,dropna,ets functions using titanic dataset
import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTIT-22/Desktop/tested.csv")
print(data)

print(data.isnull())
print(data.notnull())

print(data.fillna(0))
print(data.fillna(method="bfill"))
print(data.fillna(method='pad'))
print(data.replace(to_replace=np.nan,value=00))
print(data)
