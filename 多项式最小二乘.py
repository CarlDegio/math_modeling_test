# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:25:12 2020

@author: Eternity
"""

from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt

#误差函数,最小二乘的对象
def epsilon(P,x,y):#P=(k,t),x属于Xi向量,y属于Yi向量
    k,t=P
    return k*x+t-y#估计值-真值

def epsilon2(P, x, y):
    a,b,c=P
    return a*x*x+b*x+c-y
    


Xi=np.array([1.0,2.0,4.0,6.0,10.0])
Yi=np.array([1.0,4.0,16.0,32.0,10.0])
p0=[5,6] #y=5x+6,起始值
p1=[1,1,1]#y=x^2+x+1
#初始系数任意给，几乎都能收敛到正确的最小二乘

Result1=leastsq(epsilon,p0,args=(Xi,Yi))#一次拟合
Result2=leastsq(epsilon2,p1,args=(Xi,Yi))#二次拟合
k,t=Result1[0]
a,b,c=Result2[0]
print(Result1)
print(Result2)


plt.scatter(Xi,Yi,color='green',label='样本点',linewidth=2)#散点

x=np.linspace(0,11,100)#画直线和曲线
y=k*x+t
y2=a*x*x+b*x+c
plt.plot(x, y,color='orange',label='拟合直线',linewidth=2)
plt.plot(x, y2,color='red',label='拟合直线',linewidth=2)

plt.legend()#图例
plt.show()#绘制
    