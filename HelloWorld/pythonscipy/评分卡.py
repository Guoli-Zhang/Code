import pandas as pd
data.obs_mth.unique()
#
train = data[data.obs_mth != "2018-11-30"].reset_index().copy()
train.head()
train.shape
import lightgbm

train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=0, test_size=0.2)

