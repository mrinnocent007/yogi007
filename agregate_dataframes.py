import pandas as pd
import numpy as np

data={'day' : [1,2,3,4,5,6,7,8,9,10],
      'steps' : [4335,9552,7332,4504,5335,7552,8332,6504,8965,7689],
      'pushups' : [1,4,6,7,8,10,12,24,5,7]}
p=pd.DataFrame(data)
print(data)
print(p)
print()
print(p['pushups'].groupby)
print(p['pushups'].min)
print(p['steps'].sum)


