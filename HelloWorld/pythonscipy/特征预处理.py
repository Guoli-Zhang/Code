from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def minmax_scaler():
    """
    归一化
    :return:
    """
    # 1.加载数据
    data = pd.read_csv("data/dating.txt")
    print(data)
    data = pd.DataFrame


if __name__ == "__main__":
    minmax_scaler()
    pass