from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 0.获取数据
iris = load_iris()

x = iris.data

y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

transfer = StandardScaler()

x_train = transfer.fit_transform(x_train)

x_test = transfer.fit_transform(x_test)

estimator = KNeighborsClassifier(n_neighbors=3)

estimator.fit(x_train, y_train)

y_predict = estimator.predict(x_test)

print("预测值：\n", y_predict)

print("目标值：\n", y_test)

score = estimator.score(x_test, y_test)

print("准确率：\n", score)