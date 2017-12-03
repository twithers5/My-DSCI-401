# This illustrates a niave bayesian classifier (Gaussian) on the iris data set.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import naive_bayes
from data_util import *

data = pd.read_csv('./data/iris.csv')

print(data.head())

# Select x and y data
features = list(data)
features.remove('Species')
data_x = data[features]
data_y = data['Species']

# Convert the different class labels to unique numbers with label encoding.
le = preprocessing.LabelEncoder()
data_y = le.fit_transform(data_y)

# Split training and test sets from main set.
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.3, random_state = 4)

# Build and evaluate the model
gnb_mod = naive_bayes.GaussianNB()
gnb_mod.fit(x_train, y_train)
preds = gnb_mod.predict(x_test)
print_multiclass_classif_error_report(y_test, preds)

# Illustrate recoding numeric classes back into original (text-based) labels.
y_test_labs = le.inverse_transform(y_test)
pred_labs = le.inverse_transform(preds)
print('(Actual, Predicted): \n' + str(zip(y_test_labs, pred_labs)))