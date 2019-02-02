# 这里如此定义会提示PEP 8: do not assign a lambda expression, use a def
# 因为lamda表达式最好用于不想定义函数，而此函数是想定义的函数
f = lambda x, y: x + y

print(f(1, 2))

# 此处定义就不会提示，因为这里需要隐式定义
res = map(lambda x: x ** 2, [0, 1, 2, 3, 4, 5])
print(list(res))


