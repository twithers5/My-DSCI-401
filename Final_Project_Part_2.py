# DSCI 401 Final Project
# LASSO

import pandas as pd
import matplotlib.pyplot as plt
import pprint
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn import preprocessing

# Read in data
df = pd.read_csv('./data/MLB Stats 10-16.csv')

features = list(df) 
features.remove('win%')

# Removes "runs" column because it is the same data as the "rpg" column
features.remove('runs')

# Sets the feature columns as the explanatory variables
data_x = df[features]

# Sets the sale price as the response variable
data_y = df['win%']

# Imputing the column means for missing values by column
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
data_x = imp.fit_transform(data_x)

print(df.head())

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.2, random_state = 4)

# Tests multiple different alphas to figure out which one is the best at at predicting
# the sale prices of the houses by computing the R squared for each alpha
alphas = [0.1,0.5,1,2,3,4,5,6,7,8,9,10]
for i in alphas:
	test_mod = linear_model.Lasso(alpha=i, normalize=True, fit_intercept=True)
	test_mod.fit(x_train, y_train)
	preds = test_mod.predict(x_test)
	print('R^2 (Lasso Model with alpha=' + str(i) + '): ' + str(r2_score(y_test, preds)))
