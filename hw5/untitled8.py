# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:13:16 2020
Email:zuhuwang@bu.edu
@author: Zuhua Wang
"""

import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("Rates_Discount_Factors.csv") 
# Preview the first 5 lines of the loaded data 
print(data.head().iloc[:,[0,5]])
print(data.iloc[0:5,3])
data.iloc[3,3]=1.9
print(data.iloc[0:5,3])
for i in range(41):
    s=sum(data.iloc[1:i+1,2])
    par=2*(1-data.iloc[i,2])/s
    data.iloc[i,5]=par
print(data.iloc[:,0:6])
data.iloc[1,6]=(1/data.iloc[1,2]-1)*2
for i in range(2,41):
    forward=2*(data.iloc[i-1,2]/data.iloc[i,2]-1)
    data.iloc[i,6]=forward  
print(data.iloc[:,8:9])
for i in range(1,41):
    s=sum(data.iloc[1:i+1,9])
    par=2*(1-data.iloc[i,9])/s
    data.iloc[i,8]=par
print(data.iloc[:,8:9])
for i in range(1,41):
    s=sum(data.iloc[1:i,11])
    dis=(1-data.iloc[i,3]*s)/(1+data.iloc[i,3]/2)
    data.iloc[i,11]=dis
    #print(s)
print(data.iloc[:,11:12])
print(data.iloc[:,12:13])
data.to_csv('result.csv')



