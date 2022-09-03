# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:50:13 2020

@author: Eternity
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
#一次指数平滑，适合总体上在水平线的数据
x1 = [i for i in range(10)]
y1 = [446.6565,  454.4733,  455.663 ,  423.6322,  456.2713,  440.5881, 425.3325,  485.1494,  506.0482,  526.792 ]
data = pd.Series(y1,index=x1)

fit1 = SimpleExpSmoothing(data).fit(smoothing_level=0.6,optimized=False)#加权系数α=0.6情况,optimized=true时会自动寻找最贴近的α
#fcast1 = fit1.forecast(3).rename(r'$\alpha=0.6$')#只适合整数下标
pred1=fit1.predict(start=len(x1),end=len(x1)+2).rename(r'$\alpha=0.6$')#可用于小数下标
fit2=SimpleExpSmoothing(data).fit()#选择最小方差的加权系数
pred2=fit2.predict(start=len(x1),end=len(x1)+2).rename(r'$\alpha=%s$'%fit2.model.params['smoothing_level'])


ax = data.plot(marker='o', color='black', figsize=(12,8),label='raw data',legend=True)
pred1.plot(marker='o', ax=ax, color='blue', legend=True)
pred2.plot(marker='o', ax=ax, color='red', legend=True)#把需要显示legend的放在前面，否则color错误
fit1.fittedvalues.plot(marker='o', ax=ax, color='blue')
#fcast1.plot(marker='o', ax=ax, color='blue', legend=True)
fit2.fittedvalues.plot(marker='o', ax=ax, color='red')


plt.show()