# Data set A
# I used linear regression for my base model because it is the most basic regression model 
# that takes every column and uses it to predict the sale price. I started off by 
# preparing my data and then testing and training the data using a the linear model.
# I then printed out the R squared for the base model.

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
df = pd.read_csv('./data/AmesHousingSetA.csv')

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

# Loop through the columns to print out a pairs plot containing 5 columns at a time and
# the sale price
#x=0
#for i in range(0,len(features)/5):
#	sm = pd.plotting.scatter_matrix(df[features[x:x+5] + ['SalePrice']])
#	plt.show()
#	x+=5

# Sets the feature columns as the explanatory variables
data_x = df[features]

# Sets the sale price as the response variable
data_y = df['SalePrice']

# Imputing the column means for missing values by column
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
data_x = imp.fit_transform(data_x)

# Create a least squares linear regression model.
base_mod = linear_model.LinearRegression()

# Split training and test sets from main set
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.2, random_state = 4)

# Fit the model
base_mod.fit(x_train,y_train)

# Makes predictions on test data and prints the results
preds = base_mod.predict(x_test)
print('R^2 (Base Model): ' + str(r2_score(y_test, preds)))

# Data set A output:
# R^2 (Base Model): 0.89687188219
