"""
This script lets us explore the values in the Boston prices
dataset . We will use this information to develop a machine learning
model to be deployed in an iOS app.

Author: Dr J Rogel

Last modified: 20251221
"""

import pandas as pd
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)
X_full = housing.data
y = housing.target

housing_df = pd.concat([X_full, y], axis=1)

housing_df.columns
housing_df.describe()

X = boston_df[['CRIM', 'RM']]
X.columns = ['Crime', 'Rooms']
X.describe()

# Crime       Rooms
# count  506.000000  506.000000
# mean     3.593761    6.284634
# std      8.596783    0.702617
# min      0.006320    3.561000
# 25%      0.082045    5.885500
# 50%      0.256510    6.208500
# 75%      3.647423    6.623500
# max     88.976200    8.780000
