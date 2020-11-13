from sklearn.linear_model import LinearRegression


# 1.获取数据

# 特征值
x = [[80, 86],
     [82, 80],
     [85, 78],
     [90, 90],
     [86, 82],
     [82, 90],
     [78, 80],
     [92, 94]]

# 目标值
y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]

# 2.机器学习（模型训练）
estimator = LinearRegression()
estimator.fit(x, y)

# 3.模型预测
ret = estimator.predict([[90, 100]])
print(ret)

# 3.1 系数矩阵
coef = estimator.coef_
print(f"系数矩阵：{coef}\n")