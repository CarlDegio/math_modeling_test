# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:37:35 2020

@author: Eternity
"""

import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt

#vrp问题，从一个原点出发构造若干条回路，最后遍历所有点且总路程最短，约束一个回路上点数有限
num_customers = 15#外围点
num_vehicle = 5#最多回路数
num_points = 1 + num_customers#外围点+中心点
max_capacity = 5#一条回路最多点数

customers_coordinate = np.random.rand(num_points, 2)  # 生成外围点
depot_coordinate = np.array([[0.5, 0.5]])
points_coordinate = np.concatenate([depot_coordinate, customers_coordinate], axis=0)


distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')#距离矩阵


def cal_total_distance(routine):
    '''The objective function. input routine, return total distance.
    cal_total_distance(np.arange(num_points))
    '''
    num_points, = routine.shape
    return distance_matrix[0, routine[0]] \
           + sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)]) \
           + distance_matrix[routine[-1], 0]
           #按固定起点为0号点，末点为0号点计算需要被最小化的dis，实际上起末点不参与GA


def constraint_capacity(routine):#路径合法性检验,为正不合法
    capacity = 0
    c = 0
    for i in routine:
        if i != 0:
            c += 1
        else:
            capacity = max(capacity, c + 1)
            c = 0
    capacity = max(capacity, c + 1)
    return capacity - max_capacity 


from sko.GA import GA_TSP

ga_tsp = GA_TSP(func=cal_total_distance, n_dim=num_points, size_pop=50, max_iter=500, prob_mut=1, )#50条染色体

ga_tsp.Chrom = np.concatenate([np.zeros(shape=(ga_tsp.size_pop, num_vehicle-2), dtype=np.int), ga_tsp.Chrom], axis=1)#存疑，实际上只会经过原点最多四次(起末点是手工连的)
ga_tsp.has_constraint = True
ga_tsp.constraint_ueq = [constraint_capacity]
best_points, best_distance = ga_tsp.run()
print(best_points)#最优点路径，起末未必0


fig, ax = plt.subplots(1, 2)
best_points_ = np.concatenate([[0], best_points, [0]])
best_points_coordinate = points_coordinate[best_points_, :]
ax[0].plot(best_points_coordinate[:, 0], best_points_coordinate[:, 1], 'o-r')#路径图
ax[1].plot(ga_tsp.generation_best_Y)#最短距离随迭代次数的变化
ax[1].set_ylim([4,10])
plt.show()