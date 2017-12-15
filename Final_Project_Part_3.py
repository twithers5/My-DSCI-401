# DSCI 401 Final Project
# This file creates the basic linear regression model that was made in part 1 of this
# project to train and test the MLB data from the 2010 to 2016 regular seasons and predict
# the teams' winning percentage based on the teams' stats during the regular season. It 
# then tests the model on the 2017 season to see if the model is able to predict the
# teams' regular season winning percentages with high accuracy. The out put is shown with
# a comment at the bottom of the file.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn import preprocessing

# Read in data
df = pd.read_csv('./data/MLB Stats 10-16.csv')

# Sets features equal to the columns titles and removes the win percentage column
features = list(df) 
features.remove('win%')

# Removes "runs" column because it is the same data as the "rpg" column
features.remove('runs')

# Sets the feature columns as the explanatory variables
data_x = df[features]

# Sets the winning percentage as the response variable
data_y = df['win%']

# Imputing the column means for missing values by column
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
data_x = imp.fit_transform(data_x)

# Create a least squares linear regression model.
model1 = linear_model.LinearRegression()

# Split training and test sets from main set
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.2, random_state = 4)

# Fit the model
model1.fit(x_train,y_train)

# Makes predictions on test data and prints the results
preds = model1.predict(x_test)
print('R^2 (2010-2016): ' + str(r2_score(y_test, preds)))

#------------ 2017 validation preparation and testing --------------

# Read in 2017 data
df17 = pd.read_csv('./data/MLB Stats 17.csv')

# Sets features equal to the columns titles and removes the win percentage column
features17 = list(df17) 
features17.remove('win%')

# Removes "runs" column because it is the same data as the "rpg" column
features17.remove('runs')

# Sets the feature columns as the explanatory variables
data_x17 = df17[features17]

# Sets the winning percentage as the response variable
data_y17 = df17['win%']

# Imputing the column means for missing values by column
imp17 = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
data_x17 = imp17.fit_transform(data_x17)

# Makes predictions on test data and prints the results
preds17 = model1.predict(data_x17)
print('R^2 (2017): ' + str(r2_score(data_y17, preds17)))

# Output:
# R^2 (2010-2016): 0.880319278696
# R^2 (2017): 0.913911803018