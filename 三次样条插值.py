# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:16:51 2020

@author: Eternity
"""


from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

Xi=np.array([1.0,2.0,4.0,6.0,10.0])
Yi=np.array([1.0,4.0,16.0,32.0,10.0])
plt.scatter(Xi,Yi,color='green',label='样本点',linewidth=2)

cs=interpolate.CubicSpline(Xi,Yi)
#cs=interpolate.CubicSpline(Xi,Yi,bc_type='clamped')#端点导为0
x=np.linspace(0,11,100)
y=cs(x)
plt.plot(x,y,color='orange',label='三次样条',linewidth=2)


plt.legend()
plt.show()
