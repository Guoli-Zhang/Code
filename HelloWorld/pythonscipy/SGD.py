from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_absolute_error


def linear_demo():
    """
    线性回归-正规方程-小批量
    :return:
    """
    # 1.加载数据
    boston = load_boston()
    # 特征值
    x = boston.data
    # 目标值
    y = boston.target
    # 2.数据基本处理-数据分割
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=22)
    # 3.特征预处理
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
    # 4.机器学习-训练模型
    estimator = LinearRegression(fit_intercept=True)
    estimator.fit(x_train, y_train)
    # 5.模型预测&模型评估
    y_predict = estimator.predict(x_test)
    print("预测值：\n", y_predict)
    # 均方误差
    # y_test 测试集目标值
    # y_predict  预测值
    error = mean_absolute_error(y_test, y_predict)
    print("均方误差：\n", error)
    # 系数矩阵
    coef = estimator.coef_
    intercept = estimator.intercept_
    print("系数矩阵：\n", coef)
    print("偏置：\n", intercept)


def sgd_demo():
    """
    线性回归-随机梯度下降算法-大规模
    :return:
    """
    # 1.加载数据
    boston = load_boston()
    # 2.数据分割
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)
    # 3.特征预处理
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
    # 4.机器学习-随机梯度下降算法
    # max_iter=1000 最大的样本数据
    # loss="squared_loss" 损失函数使用最小二乘法
    # fit_intercept=True 参与偏置计算
    # learning_rate = "constant" 自定义学习率
    # eta0=0.01 具体学习率
    # estimator = SGDClassifier(loss="squared_loss", fit_intercept=True, learning_rate="constant", eta0=0.001)
    estimator = SGDRegressor(max_iter=10000, loss="squared_loss", fit_intercept=True, learning_rate="constant", eta0=0.0001)
    # 模型训练
    estimator.fit(x_train, y_train)
    # 预测值
    # 测试数据特征值
    y_predict = estimator.predict(x_test)
    print("预测值：\n", y_predict)
    # 均方误差
    mse = mean_absolute_error(y_test, y_predict)
    print("误差：\n", mse)

    print("偏置：\n", estimator.intercept_)
    print("系数：\n", estimator.coef_)
    # return None


if __name__ == "__main__":
    # linear_demo()
    sgd_demo()
