from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.datasets import fetch_20newsgroups
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# load_* 加载小批量数据
# fetch_* 加载大规模数据（download）

x = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
estimator = KNeighborsClassifier(n_neighbors=2)
estimator.fit(x, y)
estimator.predict([[1]])

# 加载鸢尾花数据
iris = load_iris()
print("iris:\n", iris)

# 特征值
x = iris.data
print("鸢尾花特征值：\n", x)

# 目标值
y = iris.target
print("鸢尾花目标值：\n", y)

# 将目标值和特征值构建成一个DataFrame
df = pd.DataFrame(data=x, columns=['Sepal_Length(cm)', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])

df["target"] = y

# print(df)


def seaborn_plot(data, x, y):
    """

    :param data:鸢尾花DataFrame数据
    :param x:
    :param y:
    :return:
    """
    sns.lmplot(x=x, y=y, hue="target", fit_reg=True, data=iris)

    plt.xlabel("花萼" + x)
    plt.ylabel("花瓣" + y)

    plt.show()
# if __name__ == "__main__":
#     seaborn_plot(df)
#     pass

