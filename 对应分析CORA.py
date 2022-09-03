# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 22:00:26 2020

@author: Eternity
"""

import mca
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)#不使用科学计数法
plt.rcParams['font.family']='simhei'
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size']=12.0


data = pd.read_table('CORA.txt',sep=' ', index_col=0, header=0)#index_col表示哪一列数据做纵轴,header表示哪一列数据做横轴
#X = data.drop('1975', axis=1)#删除某列
ncols=len(data.columns)#元素列数
T=0#全矩阵元素和
for index,row in data.iterrows():
    T=T+row.sum()


mca_ben = mca.MCA(data, ncols=ncols,TOL=1e-6)
mca_ind = mca.MCA(data, ncols=ncols, benzecri=False,TOL=1e-6)#不使用benzecri，TOL为精度，默认1e-


print('奇异值:',mca_ind.s)#如出现零说明奇异值过小，相应下面的量会少列
print('主惯量:',mca_ind.L)
print('chi2:',mca_ind.L*T)
print('贡献率:',mca_ind.L/mca_ind.L.sum())
print('累计贡献率:',np.cumsum(mca_ind.L/mca_ind.L.sum()))
#一般累计至0.8的所有维度都有大贡献，极端情况可能只有一个维度有大贡献，分析时只分析有大贡献的维度

print('选取的维度数:贡献率一般>=80%,默认2维')
select=2

mca_ind.fs_r(1)#计算矩阵F,一二列即行指标对应的坐标
mca_ind.fs_c(1)#计算矩阵G,一二列即列指标对应的坐标
F=mca_ind.F[:,0:2]#科目对应的坐标
Flabel=data.index
G=mca_ind.G[:,0:2]#年份对应的坐标
Glabel=data.columns

plt.xlabel('dim1')
plt.ylabel('dim2')
markers = '^', 'o'
colors = 'r','b'
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')

#一般的，在图上处于同一象限的点/几何距离/垂直径向距离临近的点有较大相关性
#在只有一个大贡献维度时，则dim1值临近的点有相关性，至于具体的增减，大小等关系需要在data中寻找
plt.plot(F[:,0],F[:,1],linestyle='',marker=markers[0],color=colors[0]
         ,alpha=0.3,ms=12,label='行指标')
for label,pos in zip(Flabel,F[:,0:2]):
    plt.annotate(label, xy=pos, xytext=(pos[0] + 0.001, pos[1]))
    
plt.plot(G[:,0],G[:,1],linestyle='',marker=markers[1],color=colors[1]
         ,alpha=0.3,ms=12,label='列指标')
for label,pos in zip(Glabel,G[:,0:2]):
    plt.annotate(label, xy=pos, xytext=(pos[0] + 0.001, pos[1]))

plt.legend()
plt.margins(0.1)#周边空白0.1倍