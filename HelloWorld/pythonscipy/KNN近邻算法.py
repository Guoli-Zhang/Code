from sklearn.neighbors import KNeighborsClassifier

"""
1.获取数据
2.数据基本处理
3.特征工程
4.机器学习（训练模型）*****
5.模型评估
"""

# 获取数据
# 特征值
x = [[2], [4], [8], [16]]
# 目标值
y = [4, 8, 16, 32]

# 2.机器学习
# 创建模型
# n_neighbors 邻居数量
estimator = KNeighborsClassifier(n_neighbors=4)

# 模拟训练-监督学习
# x 特征值
# y - 目标值
estimator.fit(x, y)

# 3.模型预测
result = estimator.predict([[1]])
print(result)
