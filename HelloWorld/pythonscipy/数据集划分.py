from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

"""
数据分割
训练数据：70%~80%
测试数据：20%~30%
"""
# 加载鸢尾花数据
iris = load_iris()
# 特征值
x = iris.data
# 目标值
y = iris.target

# 数据结构
# test_size = 0.2 测试集占20% 训练集占80%
# random_state 随机种子，如果随机种子相同， 那么采样的数据也就随之相同
# x 特征值
# y 目标值
# train 训练集
# test 测试集
# x_train 训练集特征值
# x_test 测试集特征值
# y_train 训练集目标值
# y_test 测试集目标值
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=22)
x_train1, x_test1, y_train1, y_test1 = train_test_split(x, y, test_size=0.2, random_state=22)

x_train2, x_test2, y_train2, y_test2 = train_test_split(x, y, test_size=0.2, random_state=60)

print("random_state=22的训练集特征值：\n", x_train)
print("random_state=22的训练集特征值：\n", x_train1)
print("random_state=60的训练集特征值：\n", x_train2)

# 实列化转换对象
transfer = StandardScaler()
# 100% = 80% + 20%
x_train = transfer.fit_transform(x_train)
# x_test = transfer.fit_transform(x_test)
x_test = transfer.transform(x_test)

print("x_train:\n", x_train)
print("x_test:\n", x_test)
