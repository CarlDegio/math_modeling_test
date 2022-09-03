# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:01:26 2020

@author: Eternity
"""


from scipy.optimize import minimize
import numpy as np
def f(x):
    return (x[0]-1)**2+x[1]**2
#min (x-1)^2+(y)^2
x0=np.zeros(2)#初始探索位点
result=minimize(f,x0,method='BFGS')#梯度bfgs法
print(result)


def f(x):
    return (x[0])+1/x[0]
#min x+1/x
cons=({'type': 'ineq', 'fun':lambda x:x[0]-0})#正值代表可行域

x0=np.array([0.1])#初值会影响最值，甚至于取到负范围引发异常
result=minimize(f,x0,method='SLSQP',constraints=cons)#序列二次规划
print(result)
