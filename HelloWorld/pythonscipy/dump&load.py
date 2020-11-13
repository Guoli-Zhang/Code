from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeCV, Ridge
from sklearn.metrics import mean_absolute_error


def ridge_demo():
    """
    线性回归-岭回归=梯度下降 + L2
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
    # alpha=0.1正则化力度
    # estimator = Ridge(alpha=0.001, fit_intercept=True)
    # 网络搜索 & 交叉验证
    # alphas = [0.001, 1, 10] 正则化力度超参数
    # CV = 4， 4折交叉验证
    estimator = RidgeCV(alphas=[0.001, 1, 10], cv=4)
    # 5.模型训练
    estimator.fit(x_train, y_train)
    # 预测值
    # 测试数据特征值
    y_predict = estimator.predict(x_test)
    print("预测值：\n", y_predict)
    # 均方误差
    mse = mean_absolute_error(y_test, y_predict)
    print("误差：\n", mse)


if __name__ == "__main__":
    ridge_demo()
