# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 22:41:19 2020

@author: Eternity
"""


import numpy as np
A=np.array([[1,0,5],
            [0,3,1],
            [5,1,5]])
print(np.linalg.eig(A)[0])#特征值
#print(np.linalg.eigvals(A))#或这个
print(np.linalg.eig(A)[1])#特征向量矩阵，都被规范化
