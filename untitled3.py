# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:34:58 2020

@author: 17862
"""
import math
import matplotlib.pyplot as plt

import numpy as np
def stock_matrix(N):
    stockM=np.zeros((1+2*N,N+1))
    stockM[N,0]=40
    for col in range(N):
        for row in range(1+2*N):
            if stockM[row,col]!=0:
                stockM[row-1,col+1]=stockM[row, col]*math.exp(0.21)
                stockM[row+1,col+1]=stockM[row,col]*math.exp(-0.21)
    print(stockM)
    print()
    return stockM    
def payoff(matrix):
    matrix=matrix.T
    matrix=matrix[-1].T
    for i in range(len(matrix)):
        if matrix[i]!=0:
            matrix[i]=max(40-matrix[i],0)
    print(matrix)
    return matrix

def p0(N):
    p=np.zeros((1+2*N,N+1))
    p=p.T
    p[-1]=payoff(stock_matrix(N))
    p=p.T
    count=1
    last=2*N
    for col in range(N-1,-1,-1):
        #print(row)
        for row in range(count, last):
            p[row][col]=(math.exp(-0.02)*(0.495*p[row-1][col+1]+0.505*p[row+1][col+1]))
            #print(p)
        count+=1
        last-=1
    print(p)
    return p
    
#print(p0(2))
list=[]
for i in range(1,4):
    #print (p0(i))
    list.append(p0(i)[i][0])
    print(i)
print(list)
plt.plot(list)
plt.ylabel('some numbers')
plt.show()