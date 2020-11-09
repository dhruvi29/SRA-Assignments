import numpy as np


def ech(_r,_c,matrix):
    pivot=matrix[_r][_c]
    E1=np.eye(m)
    E1[_r][_r]=1/pivot
    E2=np.eye(m)
    matrix=np.matmul(E1,matrix)
    for i in range(_r+1,m):
        E2[i][_r]=matrix[i][c]*-1
    matrix=np.matmul(E2,matrix)
    return matrix

def rearrange_pivot(_r,_c,matrix):
    pivots=np.full((m),99)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                continue
            else:
                pivots[i]=j
                break
    new_pivot=_r
    for i in range(_r+1,m):
        if pivots[i]<pivots[_r]:
            new_pivot=i
    E1=np.eye(m)
    E1[_r][_r]=0
    E1[new_pivot][new_pivot]=0
    E1[_r][new_pivot]=1
    E1[new_pivot][_r]=1
    _c=pivots[new_pivot]
    matrix=np.matmul(E1,matrix)
    return _c,matrix


m,n=input("no of rows and columns ").split()
m=int(m)
n=int(n)

my_matrix=np.zeros((m,n))
identity=np.identity(m)

for i in range(m):
    for j in range(n):
        my_matrix[i][j]=int(input())

print(my_matrix)
r=0
c=0
# rearrange_pivot(r,c,my_matrix)
for i in range(m):
    if my_matrix[r][c]==0:
        c,my_matrix=rearrange_pivot(r,c,my_matrix)
        # print(c)
        if c == 99:
            break
    my_matrix=ech(r,c,my_matrix)
    # print(my_matrix)
    r+=1
    c+=1
    if r==m or c==n:
        break
print(my_matrix)    
    

