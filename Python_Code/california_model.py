"""
This script implements a machine learning model on the
California Housing dataset to predict the price of a house
given a number of features.

The model is then converted to .mlmodel file to be used in an iOS
native app.

Author: Dr J Rogel

Last modified: 20251221
"""

import coremltools
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np


def glm_housing(X, y):
    print("Implementing a simple linear regression.")
    lm = linear_model.LinearRegression()
    gml = lm.fit(X, y)
    return gml


def main():
    print('Starting up - Loading California housing dataset.')
    housing = fetch_california_housing(as_frame=True)
    X_full = housing.data
    y = housing.target
    housing_df = pd.concat([X_full, y], axis=1)

    print("We now choose the features to be included in our model.")
    X = housing_df[['MedInc', 'AveRooms']]
    X.columns = ['Income', 'Rooms']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=7)

    my_model = glm_housing(X_train, y_train)

    coefs = [my_model.intercept_, my_model.coef_]

    print("The intercept is {0}.".format(coefs[0]))
    print("The coefficients are {0}.".format(coefs[1]))
    print(coefs)

    print("Let us check the predictions:")
    y_pred = my_model.predict(X_test)

    # calculate MAE, MSE, RMSE
    print("The mean absolute error is {0}.".format(
        metrics.mean_absolute_error(y_test, y_pred)))
    print("The mean squared error is {0}.".format(
        metrics.mean_squared_error(y_test, y_pred)))
    print("The root mean squared error is {0}.".format(
        np.sqrt(metrics.mean_squared_error(y_test, y_pred))))
    print("The r-squared {0}.".format(
        metrics.r2_score(y_test, y_pred)))

    # Sample
    sample = { 'income': X_test.iloc[0]['Income'],
                'rooms': X_test.iloc[0]['Rooms'] }
    ypred_sample = y_pred[0]

    print('A property with {0} is valued ${1:,.2f} dollars'.format(
        sample, ypred_sample*100000))

    print("Let us now convert this model into a Core ML object:")

    # Convert model to Core ML
    coreml_model = coremltools.converters.sklearn.convert(my_model,
                                            input_features=["income", "rooms"],
                                            output_feature_names="price")

    # Save Core ML Model
    coreml_model.author = 'JRogel'
    coreml_model.license = 'BSD'
    coreml_model.short_description = (
        'Predicts median house prices in California '
        'based on median income and average number of rooms (1990s)')
    coreml_model.input_description['income'] = (
        'Median income in the district (tens of thousands of USD per year)'
    )
    coreml_model.input_description['rooms'] = (
        'Average number of rooms per household')
    coreml_model.output_description['price'] = (
        'Predicted median house value (in thousands of USD)'
    )
    coreml_model.save('CaliforniaHousePricer.mlmodel')
    print('Done!')


if __name__ == '__main__':
    main()
