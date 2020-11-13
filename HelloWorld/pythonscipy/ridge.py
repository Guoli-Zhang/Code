from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDClassifier
from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, Lasso
from sklearn.metrics import mean_absolute_error


# class _BaseRidgeCV(LinearModel):


def ridge_demo():
    """
    线性回归 - 岭回归 = 梯度下降 + L2
    :return:
    """
    # 1.获取数据
    boston = load_boston()
    # 2.数据集划分（数据分割）
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)
    # 3.特征工程-标准化（特征预处理）
    transfer = StandardScaler()
    # 4.机器学习-线性回归（岭回归）（随机梯度下降算法）
    # alpha=0.1 正则化力度
    # estimator = Ridge(alpha = 0.1, fit_intercept = True)
    # 网格搜索 & 交叉验证
    # alphas = [0.1, 1, 10]正则化力度超参数
    # cv = 4  4折交叉验证
    estimator = RidgeCV(alphas=[0.1, 1, 10], cv=4)
    # 5.模型评估(模型训练)
    estimator.fit(x_train, y_train)
    # 预测值
    # 测试数据 特征值
    y_predict = estimator.predict(x_test)
    # 5.1 获取系数等值
    print("预测值：\n", y_predict)
    print("偏置：\n", estimator.intercept_)
    print("系数：\n", estimator.coef_)
    # 5.2评价
    # 均方误差
    mse = mean_absolute_error(y_test, y_predict)
    print("误差：\n", mse)


if __name__ == "__main__":
    ridge_demo()
