import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# dataframe是一个二维数组，是多个Series的集合体

# 通过字典创建
dict = {'One': Series(data=[1., 2., 3.], index=['a', 'b', 'c']),
        'Two': Series(data=[1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = DataFrame(dict)

# 指定行和列创建
df2 = DataFrame(dict, index={'r', 'd', 'a'}, columns=['One', 'Two'])

print(df2)

# 使用concat函数基于Series创建DataFrame
a = Series(range(5))
b = Series(np.linspace(4, 20, 5))
df3 = pd.concat([a, b], axis=1)

print(df3)

# 按行合并
df4 = DataFrame()
index = ['alpha', 'beta', 'gamma', 'delta', 'eta']
for i in range(5):
    a = DataFrame([np.linspace(i, 5 * i, 5)], index=[index[i]])
    df4 = pd.concat([df4, a], axis=0)
print(df4)

# DataFrame默认按列选取
print(df4[1])
df4.columns = ['a', 'b', 'c', 'd', 'e']
print(df4['b'])

# 选取行
print(df4.iloc[1])
print(df4.loc['beta'])

# 使用切片和布尔类型向量选区行
print(df4[1:3])
bool_vec = [True, False, True, False, True]
print(df4[bool_vec])

# 指定使用某个位置的元素
print(df4.iat[2, 3])
print(df4.at['gamma', 'd'])
