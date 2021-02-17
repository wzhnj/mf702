import math
import numpy as np
from numpy.linalg import solve
s0=20
su=20.97
sd=18.98
suu=22
sud=19.9
sdd=18
e=math.exp(0.005*3/12)
cuu=max(0,suu-21)
cdd=max(0,sdd-21)
cud=max(0,sud-21)

a=np.mat([[su-e*s0,e,0,0,-1,0],
          [sd-e*s0,e,0,0,0,-1],
          [0,0,suu-e*su,0,e,0],
          [0,0,0,sdd-e*sd,0,e],
          [0,0,0,sud-e*sd,0,e],
          [0,0,sud-e*su,0,e,0]])#系数矩阵
b=np.mat([0,0,cuu,cdd,cud,cud]).T    #常数项列矩阵
x=solve(a,b)        #方程组的解
print(x)
