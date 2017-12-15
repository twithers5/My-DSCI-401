import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
from sklearn import ensemble
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
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

# Sets the sale price as the response variable
data_y = df['win%']

# Imputing the column means for missing values by column
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
data_x = imp.fit_transform(data_x)

bagging_mod = ensemble.BaggingClassifier(linear_model.LogisticRegression(), n_estimators=200)
k_fold = KFold(n_splits=5, shuffle=True, random_state=4) # Shuffling is needed since classes are ordered.
bagging_mod_scores = cross_val_score(bagging_mod, data_x, data_y, scoring='f1_macro', cv=k_fold)
print('CV Scores (Bagging NB) ' + str(bagging_mod_scores))