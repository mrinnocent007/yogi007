#map
lst=["mango","apple","orange","kiwi"]
l=list(filter(lambda x : 'g' in x,lst ))
print(l)

#filter
a=[1,1,1,1]
b=[1,2,3,4]
c=[1,1,1,5]
x =list (lambda x,y,z:x+y+z,a,b,c)
print(x)
