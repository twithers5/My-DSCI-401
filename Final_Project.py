# DSCI 401 Final Project
# This file creates a basic linear regression model to train and test the MLB data from
# the 2010 to 2016 regular seasons and predict the teams' winning percentage based on the
# teams' stats during the regular season. The out put is shown with a comment at the 
# bottom of the file.

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

# Loop through the columns to print out a pairs plot containing 6 columns at a time and
# the sale price
#x=0
#for i in range(0,len(features)/6):
#	sm = pd.plotting.scatter_matrix(df[features[x:x+6] + ['win%']])
#	plt.show()
#	x+=6

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
print('R^2 (Model 1): ' + str(r2_score(y_test, preds)))

# 2010-2016 data set output:
# R^2 (Model 1): 0.880319278696