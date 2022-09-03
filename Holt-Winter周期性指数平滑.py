# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:57:17 2020

@author: Eternity
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

#https://otexts.com/fpp2/holt-winters.html
#Holt's Winter
x3 = np.linspace(0, 4 * np.pi, 100)
y3 = pd.Series(20 + 0.1 * np.multiply(x3, x3) + 8 * np.cos(2 * x3) + 2 * np.random.randn(100))
#原数据

ets3 = ExponentialSmoothing(y3, trend='add', seasonal='add', seasonal_periods=25)#加法模型additive
r3 = ets3.fit(use_boxcox=True)#boxcox方法，开并且自动计算三个最优参数γαβ
pred3 = r3.predict(start=len(y3), end=len(y3) + len(y3)//2)#预测数据

pd.DataFrame({
    'origin': y3,
    'fitted': r3.fittedvalues,
    'pred': pred3
}).plot(legend=True)