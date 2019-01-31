import pandas as pd

d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

df = pd.DataFrame(d)

# 默认axis=0 按列进行sum，设置axis=1为按行进行sum，字符串不进行计算
print(df.sum(axis=0))

# 平均值
print(df.mean())

# 标准差
print(df.std())

# 汇总数据
print(df.describe())

# 迭代 iteritems() 按列迭代
for k, v in df.iteritems():
    print(k, v)

# 迭代 iterrows() 按行迭代
for row_index, row in df.iterrows():
    print(row_index, row)

# 迭代 itertumples() 按行迭代，第一个元素为行索引
for row in df.itertuples():
    print(row)