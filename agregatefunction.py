#array agregate funtions
import numpy as np
arr = np.array([1,2,3])
print(arr.ndim)

print("sum of array ",arr.sum())
print("sum axis",arr.sum(axis=0))
print("minimun",arr.min())
print("maximun",arr.max())
print("minimun axis",arr.min(axis=0))
print("maximun axis",arr.max(axis=0))
print("product ",np.prod(arr))
