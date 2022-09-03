# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:08:39 2020

@author: Eternity
"""


import numpy as np
p=np.poly1d([4,3,2,1])#f(x)=4x^3+3x^2+2x+1
p1=np.poly1d([4,3,2,1],True)#f(x)=(x-4)(x-3)(x-2)(x-1)

print(p)
print(p(2),'\n')#f(2)

print(np.polyder(p))#求导
print(np.polyint(p))#积分
print(p.r)#求所有根
#print(np.roots(p))#等价

print(p*p1)#多项式乘法