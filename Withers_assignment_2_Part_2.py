# Data set A
# I used LASSO regression for my best model because we discussed in class that it usually
# produces the best R squared. I use the same data transforms as I used in the base model
# and then tested to see what the best alpha was for the LASSO model. I then created a 
# LASSO model with the best R squared from the tested R squares.

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

# Sets the feature columns as the explanatory variables
data_x = df[features]

# Sets the sale price as the response variable
data_y = df['SalePrice']

# Imputing the column means for missing values by column
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
data_x = imp.fit_transform(data_x)

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.2, random_state = 4)

# Tests multiple different alphas to figure out which one is the best at at predicting
# the sale prices of the houses by computing the R squared for each alpha
#alphas = [5,6,7,8,9,10,11,12,13,14]
#for i in alphas:
#	test_mod = linear_model.Lasso(alpha=i, normalize=True, fit_intercept=True)
#	test_mod.fit(x_train, y_train)
#	preds = test_mod.predict(x_test)
#	print('R^2 (Lasso Model with alpha=' + str(i) + '): ' + str(r2_score(y_test, preds)))

# Output:	
#R^2 (Lasso Model with alpha=5): 0.911597248641
#R^2 (Lasso Model with alpha=6): 0.912207154088
#R^2 (Lasso Model with alpha=7): 0.91230823727
#R^2 (Lasso Model with alpha=8): 0.912333541457
#R^2 (Lasso Model with alpha=9): 0.912320296083
#R^2 (Lasso Model with alpha=10): 0.912200358345
#R^2 (Lasso Model with alpha=11): 0.911988359197
#R^2 (Lasso Model with alpha=12): 0.911798915938
#R^2 (Lasso Model with alpha=13): 0.911639763512
#R^2 (Lasso Model with alpha=14): 0.911464648459

# Uses 8 (the best alpha from the alpha test) as the alpha for the best (LASSO) 
# regression model
best_mod = linear_model.Lasso(alpha=8, normalize=True, fit_intercept=True)
best_mod.fit(x_train, y_train)
preds = best_mod.predict(x_test)
print('R^2 (Best model): ' + str(r2_score(y_test, preds)))

# Data set A output:
# R^2 (Best Model): 0.912333541457