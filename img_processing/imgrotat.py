import numpy as np


##QUESTION 1
x=np.zeros((8,8),dtype=int)
x[1::2, ::2] = 1
x[::2, 1::2] = 1
print(x)

##QUESTION 2
r=np.arange(9,dtype=int).reshape((3,3))
s=np.random.randint(0,50,9).reshape((3,3))
print(np.dot(r,s))

##QUESTION 3
list=[]
for i in range(9):
    d=int(input())
    list.append(d)
dog=np.array(list).reshape((3,3))
cat1=dog.sum(axis=1)
cat2=dog.sum(axis=0)
print("sum of columns "+str(cat1[0])+" "+str(cat1[1])+" "+str(cat1[2]))
print("sum of rows "+str(cat2[0])+" "+str(cat2[1])+" "+str(cat2[2]))
print("max sum of column "+str(np.amax(cat1)))
print("max sum of rows "+str(np.amax(cat2)))

##QUESTION 4
dict={'Gfg' : 6, 'is' : 7, 'best' : 9, 'for' : 8, 'geeks' : 11}
i=int(input("lower "))
j=int(input("higher "))
new={}
for key, val in dict.items(): 
    if int(val) >= i and int(val) <= j: 
        new[key] = val
print(str(new))


##QUESTION 5
a=[]
for i in range(3):
    p=input()
    q=input()
    r=input()
    a.append((p,q,r))
b=(a[0],a[1],a[2])
res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]}  
                               for sub in b]
print(res)