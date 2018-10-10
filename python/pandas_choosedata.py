import numpy as np
import pandas as pd

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(1,25).reshape(6,4),index=dates,columns=['a','b','c','d'])

print(df.a)

# 筛选

print(df[0:3])

print(df['20130104':'20130105'])

# 根据标签

print(df.loc[:,['c','d']])

# 根据序列

print(df.iloc[[1,3,5],1:3])

# # 混合选择

# print(df.ix[:3],['A','C'])

# 判断选择

print(df[df.a>9])
