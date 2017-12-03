# 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import naive_bayes
from data_util import *

data = pd.read_csv('./data/churn_data.csv')

#-------------- Data preparation --------------
del data['CustID']

features = list(data)
features.remove('Churn')
data_x = data[features]
data_y = data['Churn']

# Get the indices of the categorical features for a given dataframe
def cat_feature_inds(dataframe):
	td = pd.DataFrame({'a':[1,2,3], 'b':[1.0, 2.0, 3.0]})
	enums = zip(list(dataframe), range(len(list(dataframe))))
	selected = filter(lambda (name, ind): not(dataframe[name].dtype in [td['a'].dtype, td['b'].dtype]), enums)
	return map(lambda (x, y): y, selected)
	
data_x_cat = cat_feature_inds(data[features]) 

le = preprocessing.LabelEncoder()
for i in data_x_cat:
	data_x[features[i]] = le.fit_transform(data_x[features[i]])
data_y = le.fit_transform(data_y)

#----------- churn data training and testing ---------------
print('------------------- churn data training and testing -------------------')
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.3, random_state = 4)

gnb_mod = naive_bayes.GaussianNB()
gnb_mod.fit(x_train, y_train)
preds = gnb_mod.predict(x_test)
print_multiclass_classif_error_report(y_test, preds)

y_test_labs = le.inverse_transform(y_test)
pred_labs = le.inverse_transform(preds)
print('(Actual, Predicted): \n' + str(zip(y_test_labs, pred_labs)))

print('--------------------------------------------------------')
print('------------------- churn validation -------------------')
print('--------------------------------------------------------')

#------------ churn validation preparation and testing --------------
data_test = pd.read_csv('./data/churn_validation.csv')

del data_test['CustID']

features_test = list(data_test)
features_test.remove('Churn')
data_x_test = data_test[features_test]
data_y_test = data_test['Churn']

data_x_cat_test = cat_feature_inds(data_test[features_test])
le_test = preprocessing.LabelEncoder()
for i in data_x_cat_test:
	data_x_test[features_test[i]] = le_test.fit_transform(data_x_test[features_test[i]])
data_y_test = le_test.fit_transform(data_y_test)

gnb_mod_test = naive_bayes.GaussianNB()
preds_test = gnb_mod.predict(data_x_test)
print_multiclass_classif_error_report(data_y_test, preds_test)

y_labs = le.inverse_transform(data_y_test)
pred_labs_test = le.inverse_transform(preds_test)
print('(Actual, Predicted): \n' + str(zip(y_labs, pred_labs_test))) 






