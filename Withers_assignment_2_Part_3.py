# Data set B
# After preparing the data set like I did for data set A, I tested both my base and best
# model on data set B.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
df = pd.read_csv('./data/AmesHousingSetB.csv')

# Deletes the PID column because an ID number is useless for predicting the price
del df['PID']

# Get a list of the categorical features for a given dataframe
def cat_features(dataframe):
	td = pd.DataFrame({'a':[1,2,3], 'b':[1.0, 2.0, 3.0]})
	return filter(lambda x: not(dataframe[x].dtype in [td['a'].dtype, td['b'].dtype]), list(dataframe))

# Get the indices of the categorical features for a given dataframe
def cat_feature_inds(dataframe):
	td = pd.DataFrame({'a':[1,2,3], 'b':[1.0, 2.0, 3.0]})
	enums = zip(list(dataframe), range(len(list(dataframe))))
	selected = filter(lambda (name, ind): not(dataframe[name].dtype in [td['a'].dtype, td['b'].dtype]), enums)
	return map(lambda (x, y): y, selected)

# Transform the df to a one-hot encoding	
df = pd.get_dummies(df, columns=cat_features(df))

# Sets features equal to the columns titles and removes the sale price column
features = list(df) 
features.remove('SalePrice')

# Sets the feature columns as the explanatory variables
data_x = df[features]

# Sets the sale price as the response variable
data_y = df['SalePrice']

# Imputing the column means for missing values by column
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
data_x = imp.fit_transform(data_x)

# ----------------------------------- Base Test --------------------------------------
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.2, random_state = 4)
base_mod = linear_model.LinearRegression()
base_mod.fit(data_x,data_y)
preds = base_mod.predict(x_test)
print('R^2 (Base Model): ' + str(r2_score(y_test, preds)))

# Base model data set B output:
# R^2 (Base Model): 0.964752376326

# ----------------------------------- Best Test --------------------------------------
test_mod = linear_model.Lasso(alpha=8, normalize=True, fit_intercept=True)
test_mod.fit(data_x,data_y)
preds = test_mod.predict(x_test)
print('R^2 (Best model): ' + str(r2_score(y_test, preds)))

# Best model data set B output:
# R^2 (Best model): 0.96123833943

