#lambda function
a=lambda x : x+2
print(a(2))

b=lambda x : x**x
print(b)

#map function
lst =[1,2,3,4,5]
l=list(map(lambda x : x+5 , lst))
print(l)

#filter function
lst =[1,2,3,4,5,6,7,8]
l=list(filter(lambda x :x%2 ,lst))
print(l)

#reduce function
from functools import reduce 
lst =[1,2,3,4,5,6,7,8]
y=reduce(lambda x,y : x+y , lst )
print(y)

