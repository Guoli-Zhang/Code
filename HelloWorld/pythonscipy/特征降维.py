import pandas as pd
from sklearn.feature_selection import VarianceThreshold


def var_demo():
    """

    :return:
    """

    data = pd.read_csv("data/factor_returns.csv")

    print(data)
    print(data.shape)

    transfer = VarianceThreshold