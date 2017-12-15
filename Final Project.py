# DSCI 401 Final Project

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

features = list(df) 
features.remove('win%')

# Sets the feature columns as the explanatory variables
data_x = df[features]

# Sets the sale price as the response variable
data_y = df['win%']

# Loop through the columns to print out a pairs plot containing 5 columns at a time and
# the sale price
x=0
for i in range(0,len(features)/5):
	sm = pd.plotting.scatter_matrix(df[features[x:x+5] + ['SalePrice']])
	plt.show()
	x+=5