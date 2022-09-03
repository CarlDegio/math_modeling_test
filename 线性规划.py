# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:59:54 2020

@author: Eternity
"""


import numpy as np
from scipy.optimize import linprog

dest=np.array([80,45])#目标函数80x1+45x2的最大值

Inequal_Constraint=np.array([[20,5],[15,10]])#不等式约束，默认小于，如20x1+5x2<=...
Constraint_board=np.array([400,450])#20x1+5x2<=400,第二个同理

#equal_Constraint=np.array([[20,5],[15,10]])#等式约束，默认小于，如20x1+5x2==...
#Constraint_board1=np.array([400,450])20x1+5x2==400，这两个参数写在不等约束后面

result=linprog(-dest,Inequal_Constraint,Constraint_board,bounds=([0,None],[0,None]))#函数默认求最小值
print(result)
#fun代表最优化值，这里需要取负号
#x向量代表最优位置
