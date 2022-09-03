# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 21:13:24 2020

@author: Eternity
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import Holt
#https://otexts.com/fpp2/holt.html
#Holt法，能贴合近似直线型的数据
data = [17.5534,  21.86  ,  23.8866,  26.9293,  26.8885,  28.8314, 30.0751,  30.9535,  30.1857,  31.5797,  32.5776,  33.4774, 39.0216,  41.3864,  41.5966]
index= pd.date_range(start='1990', end='2005', freq='A')
air = pd.Series(data, index)

fit1 = Holt(air).fit(smoothing_level=0.8, smoothing_slope=0.2, optimized=False)#α=0.8，β=0.2
fcast1 = fit1.forecast(5).rename(r"Holt's linear trend,$\alpha=0.8,\beta=0.2$")#对平滑值的一阶差分也作一次平滑
fit3 = Holt(air, damped=True).fit(smoothing_level=0.8, smoothing_slope=0.2)
fcast3 = fit3.forecast(5).rename(r"Additive damped trend,$\alpha=0.8,\beta=0.2$")#短期有趋势、长期趋于稳定的序列，带阻尼系数

fit4=Holt(air).fit()#自适应曲线，找出使方差最小的α和β，damped=true时也能找出Φ:damping_slope
print(fit4.model.params)#自适应参数

ax = air.plot(color="black", marker="o", figsize=(12,8),label='raw data',legend=True)
fcast1.plot(ax=ax, color='blue', marker="o", legend=True)
fcast3.plot(ax=ax, color='green', marker="o", legend=True)

fit1.fittedvalues.plot(ax=ax, color='blue')
fit3.fittedvalues.plot(ax=ax, color='green')
fit4.fittedvalues.plot(ax=ax, color='red')
