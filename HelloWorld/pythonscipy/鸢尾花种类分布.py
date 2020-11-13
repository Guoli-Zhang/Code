from sklearn.datasets import load_iris
import seaborn
import pandas as pd
import matplotlib.pyplot as plt

# 加载鸢尾花数据
iris = load_iris()

# 特征值
x = iris.data

# 目标值
y = iris.target

# 将特征值和目标值构建成一个DataFrame
df = pd.DataFrame(data=x, columns=['sepal length (cm)', 'sepal width (cm)',
                                   'petal length (cm)', 'petal width (cm)'])

# 将目标值添加到DataFrame中
df["target"] = y

# 通过seaborn绘制出鸢尾花种类的分布
def seaborn_blot(data, x, y):
    """

    :param data:鸢尾花DataFrame数据（目标值数据）
    :param x: x轴标题
    :param y: y轴标题
    :return:
    """
    # fit_reg BOOL: 是否需要进行线性拟合
    seaborn.lmplot(x=x, y=y, data=data, hue="target", fit_reg=False)

    plt.xlabel("花萼" + x)
    plt.xlabel("花瓣" + y)

    # 展示图像
    plt.show()

if __name__ == "__main__":
    seaborn_blot(df, x='sepal length (cm)', y='petal length (cm)')