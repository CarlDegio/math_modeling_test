# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:51:26 2020

@author: Eternity
"""

import torch as t
import matplotlib.pyplot as plt
#用自动求导和反向传播，学习参数w和b
#其中rawdata由y=w*x*x+b加上一个小噪声合成
t.manual_seed(100)#随机数种子，保证数据可重复验证
x=t.unsqueeze(t.linspace(-1,1,100),dim=1)#变为列向量,size=[10,1]
y=3*x.pow(2)+2+0.2*t.rand(x.size())

plt.subplot(2,1,1)
plt.scatter(x.numpy(),y.numpy())
plt.show()

w=t.randn(1,1,dtype=t.float,requires_grad=True)
b=t.randn(1,1,dtype=t.float,requires_grad=True)#初始化w和b

lr=0.01#learning rate学习率
for i in range(800):
    y_pred=x.pow(2).mm(w)+b
    loss=0.5*(y_pred-y)**2;#定义的损失函数，最小化时认为得到了正确的w和b
    loss=loss.sum();#损失函数和
    
    loss.backward();#反向传播，计算出损失函数关于w和b的梯度
    
    with t.no_grad():#手动改变参数时，停止求导计算，否则会改变w和b的梯度运算逻辑
        w-=lr*w.grad
        b-=lr*b.grad
        w.grad.zero_()
        b.grad.zero_()

plt.subplot(2,1,2)
plt.scatter(x.numpy(),y.numpy(),label='real')#原数据点
plt.plot(x.numpy(),y_pred.detach().numpy(),'r-',label='predict')#预测的二次曲线,detach作用为取消grad
plt.legend()
plt.show();
print(w,b)