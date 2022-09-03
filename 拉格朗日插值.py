# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:55:37 2020

@author: Eternity
"""


from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

Xi=np.array([1.0,2.0,4.0,6.0,10.0])#数据点
Yi=np.array([1.0,4.0,16.0,32.0,10.0])
plt.scatter(Xi,Yi,color='green',label='样本点',linewidth=2)

lagrange=interpolate.lagrange(Xi,Yi)#拉格朗日插值
x=np.linspace(0,11,100)
y=lagrange(x)
plt.plot(x, y, color='red',label='拉格朗日插值',linewidth=2)

plt.legend()
plt.show()

