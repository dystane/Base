import pandas as pd
import numpy as np
from pandas import Series,DataFrame

a = np.random.rand(5)

#Series 可以被认为是带索引（index）的一维数组
s = Series(data=a,index=['a','b','c','d','e'],name='first series')

#由dict创建
dict = {'a':0.,'b':1 ,'c':2}
s1 = Series(data=dict)

#数据访问
s2 = Series(np.random.randn(10),index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(s2)
print(s2[:2])
print(s2[['e','i']])
print(s2 > 5)    #每个元素判断一边并输出true or false
print(s2[s2 > 0.1])    #输出符合条件的元素
print('a' in s2)
