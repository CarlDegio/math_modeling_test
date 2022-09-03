# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:35:13 2020

@author: Eternity
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Xi=[5,-5,-4,-4,-3,
    -3,-2,-2,-1,-1,
    -1,0,0,1,1,
    1,2,3,4,5]
Yi=[1,3,4,5,0,
    3,-5,1,2,4,
    4,5,-5,-4,-3,
    -1,-2,-3,4,3]
Zi=[-5,-3,-2,-1,0,
    1,2,4,5,5,
    6,4,3,1,0,
    -1,-2,-4,-5,-5]
P=[]
for i in range(20):
    P.append((Xi[i],Yi[i]))



class bicubic:#双三次
    '''
    z=f(x,y)=c0+c1x+c2y+
    c3x^2+c4xy+c5y^2+
    c6x^3+c7x^2y+c8xy^2+c9y^3+
    c10xy^3+c11x^2y^2+c12x^3y+
    c13x^2y^3+c14x^3y^2
    +c15x^3y^3
    '''
    m=16 #m行n列,m>=16,n=16
    n=16
    A=0
    C=0
    points=0
    Zi=0
    def __init__(self,m,n,points,Zi):#传入矩阵规模,坐标点(大于16个)
        self.m = m
        self.n = n
        self.A=np.mat(np.zeros((m,n)))
        self.points=points
        self.Zi=Zi
        for i in range(m):
            self.A[i,0]=1
            self.A[i,1]=points[i][0]
            self.A[i,2]=points[i][1]
            
            self.A[i,3]=points[i][0]**2
            self.A[i,4]=points[i][0]*points[i][1]
            self.A[i,5]=points[i][1]**2
            
            self.A[i,6]=points[i][0]**3
            self.A[i,7]=points[i][0]**2*points[i][1]
            self.A[i,8]=points[i][0]*points[i][1]**2
            self.A[i,9]=points[i][1]**3
            
            self.A[i,10]=points[i][1]**3*points[i][0]
            self.A[i,11]=points[i][1]**2*points[i][0]**2
            self.A[i,12]=points[i][1]*points[i][0]**3
            
            self.A[i,13]=points[i][1]**3*points[i][0]**2
            self.A[i,14]=points[i][1]**2*points[i][0]**3
            
            self.A[i,15]=points[i][1]**3*points[i][0]**3
        
        self.C=self.A.T.dot((np.mat(Zi).T))
        self.C=self.A.T.dot(self.A).I.dot(self.C)
    def f(self,x,y):
        C=self.C.T.tolist()
        C=C[0]
        
        return C[0]*np.array([1 for i in range(100)])+C[1]*x+C[2]*y+\
            C[3]*x**2+C[4]*x*y+C[5]*y**2+\
            C[6]*x**3+C[7]*x**2*y+C[8]*x*y**2+C[9]*y**3+\
            C[10]*x*y**3+C[11]*x**2*y**2+C[12]*x**3*y+\
            C[13]*x**2*y**3+C[14]*x**3*y**2+\
            C[15]*x**3*y**3
    def paint(self):
        xv=np.linspace(-5.5,5.5,100)#分割需要相同份数，否则f内无法相加
        yv=np.linspace(-5.5,5.5,100)
        X,Y=np.meshgrid(xv,yv)
        z=self.f(X,Y)
        ax = plt.gca(projection='3d')
        for i in range(20):#画点
            ax.scatter3D(self.points[i][0],self.points[i][1],self.Zi[i],linewidth=4)
        ax.plot_surface(X,Y,z,cmap='jet')#画曲面
        ax.set_title('曲面')
        plt.show()
        
        
            
b=bicubic(20,16,P,Zi)
b.paint()
    
    