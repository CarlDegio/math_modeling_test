# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:18:25 2020

@author: Eternity
"""


import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()#无向图
G.add_edges_from([('s','v1'),('s','v3'),('v1','v3'),
                  ('v1','v2'),('v3','v4'),('v2','v3'),
                  ('v4','t'),('v2','t'),('v4','v2')])
print(nx.has_eulerian_path(G))
print(list(nx.eulerian_path(G)))#欧拉路径，有0或2奇数顶点则存在欧拉路径
print(nx.is_eulerian(G))#是否是欧拉回路图，需要0个奇数顶点才存在

DG = nx.DiGraph({0: [3], 1: [2], 2: [3], 3: [0, 1]})
print(nx.is_eulerian(DG))
print(list(nx.eulerian_circuit(DG)))
#有向图，每个顶点入=出则存在欧拉回路
#欧拉通路：存在某顶点入度比出度大1，另一顶点出度比入度大1，其余顶点入度等于出