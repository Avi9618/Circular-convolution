import numpy as np
import matplotlib.pyplot as plt

M=int(input("enter the length of x1[n]"))
N=int(input("enter the length of x2[n]"))
g=max(M,N)
a=np.zeros(g)
b=np.zeros(g)
c=np.zeros((g,1))
for i in range(0,M):
    a[i]=input("enter x1["+str(i)+"]")
print(a)
for i in range(0,N):
    b[i]=input("enter x2["+str(i)+"]")
print(b)
z=np.zeros((g,g))

for i in range(0,g):
    z[i]=np.roll(b,i)
z=z.T
#print(z)
c=np.dot(z,a)
print(c)

