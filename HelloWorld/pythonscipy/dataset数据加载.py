from sklearn.datasets import load_iris
from sklearn.datasets import fetch_20newsgroups

# load_* 加载小批量数据（本地）
# fetch_* 加载大规模数据（网络下载）

# 加载鸢尾花数据
iris = load_iris()

# 鸢尾花特征值
x = iris.data

# 鸢尾花目标值
y = iris.target

# 特征值名称
# 花萼 ['sepal length(cm)', 'sepal width(cm)']
# 花瓣  ['petal length(cm)', 'petal width(cm)']
feature_name = iris.feature_names

# 目标值名称
# 山鸢尾 虹膜鸢尾 变色鸢尾
target_name = iris.target_names

print(f"iris:{iris}\n" + "鸢尾花特征：{x}\n" + f"鸢尾花目标值：{y}\n" +
      f"特征值名称：{feature_name}\n" + f"目标值名称：{target_name}\n")
