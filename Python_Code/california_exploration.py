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

X = housing_df[['MedInc', 'AveRooms']]
X.columns = ['Income', 'Rooms']
X.describe()

# Income         Rooms
# count  20640.000000  20640.000000
# mean       3.870671      5.429000
# std        1.899822      2.474173
# min        0.499900      0.846154
# 25%        2.563400      4.440716
# 50%        3.534800      5.229129
# 75%        4.743250      6.052381
# max       15.000100    141.909091
