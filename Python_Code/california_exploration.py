"""
This script lets us explore the values in the California Housing
dataset. We will use this information to develop a machine learning
model to be deployed in an iOS app.

Author: Dr J Rogel

Last modified: 20251221
"""

import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

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


plt.figure(figsize=(8, 10))

# Top plot: Income vs Target
plt.subplot(2, 1, 1)
plt.scatter(X['Income'], y, facecolors='none',
            edgecolors='black',
            alpha=0.6)
plt.xlabel('Median Income', fontsize=12)
plt.ylabel('Median House Value', fontsize=12)
plt.title('Median Income vs Median House Value', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Bottom plot: Rooms vs Target
plt.subplot(2, 1, 2)
plt.scatter(X['Rooms'], y, facecolors='none',
            edgecolors='black',
            alpha=0.6)
plt.xlabel('Average Number of Rooms', fontsize=12)
plt.ylabel('Median House Value', fontsize=12)
plt.title('Average Number of Rooms vs Median House Value', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()
plt.show()