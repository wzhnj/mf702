# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:30:02 2020

@author: 17862
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:34:58 2020

@author: 17862
"""
import math
import numpy as np
def stock_matrix(N):
    stockM=np.zeros((1+2*N,N+1))
    stockM[N,0]=20
    for col in range(N):
        for row in range(1+2*N):
            if stockM[row,col]!=0:
                stockM[row-1,col+1]=stockM[row, col]*math.exp(0.38*1.5/12)
                stockM[row+1,col+1]=stockM[row,col]*math.exp(-0.42*1.5/12)
   # print(stockM)
    #print()
    return stockM    
def payoff(matrix):
    matrix=matrix.T
    matrix=matrix[-1].T
    for i in range(len(matrix)):
        if matrix[i]!=0:
            matrix[i]=max(matrix[i]-21,0)
    print (matrix)
    return matrix

def p0(N):
    p=np.zeros((1+2*N,N+1))
    p=p.T
    p[-1]=payoff(stock_matrix(N))
    p=p.T
    for col in range(N-1,-1,-1):
        #print(row)
        for row in range(1, 2*N):
            p[row][col]=math.exp(-0.005)*(0.51*p[row-1][col+1]+0.49*p[row+1][col+1])
    return p
    
print(p0(2))