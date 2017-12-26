# -*- coding: utf-8 -*-

import numpy as np
import logging
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn import svm
from data_statistic import consistent
from sklearn.externals import joblib


with open('../numpys/test_result1.txt', 'r') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]
    lines = np.array(lines, dtype='float64')
    print(lines.flags)
    train, test = train_test_split(lines, test_size=0.3)

    train_data = train[:, :9]
    train_target = train[:, -1] * 4.0
    print('------- train data shape ------')
    print(train_data.shape)
    print(train_target.shape)

    test_data = test[:, :9]
    test_target = test[:, -1] * 4.0
    print('------- test data shape --------')
    print(test_data.shape)
    print(test_target.shape)


print('-------------------------- ordinary linear regression---------------------------------------')
reg = linear_model.LinearRegression()
reg.fit (train_data, train_target)

test_result = reg.predict(test_data)

test_result[test_result > 100.0] = 100
test_result[test_result < .0] = 0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))


print('-------------------------- ridge regression with alpha = 0.1 ---------------------------------------')

ridge_reg = linear_model.Ridge(alpha=0.1)
ridge_reg.fit (train_data, train_target)

test_result = ridge_reg.predict(test_data)

test_result[test_result > 100.0] = 100
test_result[test_result < .0] = 0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))


print('-------------------------- ridge regression with alpha = 0.5 ---------------------------------------')

ridge_reg = linear_model.Ridge(alpha=0.5)
ridge_reg.fit (train_data, train_target)

test_result = ridge_reg.predict(test_data)

test_result[test_result > 100.0] = 100
test_result[test_result < .0] = 0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))






print('-------------------------- ridge regression with alpha = 1 ---------------------------------------')

ridge_reg = linear_model.Ridge(alpha=1.0)
ridge_reg.fit (train_data, train_target)

test_result = ridge_reg.predict(test_data)

test_result[test_result > 100.0] = 100.0
test_result[test_result < .0] = 0.0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))

print('-------------------------- ridge regression with alpha = 10 ---------------------------------------')

ridge_reg = linear_model.Ridge(alpha=10.0)
ridge_reg.fit (train_data, train_target)

test_result = ridge_reg.predict(test_data)

test_result[test_result > 100.0] = 100.0
test_result[test_result < .0] = 0.0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))


print('-------------------------- lasso regression with alpha = 0.1 ---------------------------------------')

lasso_reg = linear_model.Lasso(alpha=0.1)
lasso_reg.fit (train_data, train_target)

test_result = lasso_reg.predict(test_data)

test_result[test_result > 100.0] = 100
test_result[test_result < .0] = 0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))

print('-------------------------- lasso regression with alpha = 0.5 ---------------------------------------')

lasso_reg = linear_model.Lasso(alpha=0.5)
lasso_reg.fit (train_data, train_target)

test_result = lasso_reg.predict(test_data)

test_result[test_result > 100.0] = 100
test_result[test_result < .0] = 0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))

print('-------------------------- lasso regression with alpha = 1 ---------------------------------------')

lasso_reg = linear_model.Lasso(alpha=1.0)
lasso_reg.fit (train_data, train_target)

test_result = lasso_reg.predict(test_data)

test_result[test_result > 100.0] = 100.0
test_result[test_result < .0] = 0.0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))


print('-------------------------- svr  ---------------------------------------')

clf = svm.SVR(kernel='rbf', C=1e3, gamma=0.1)
clf.fit(train_data, train_target)

test_result = clf.predict(test_data)

test_result[test_result > 100.0] = 100.0
test_result[test_result < .0] = 0.0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))
joblib.dump(clf, './svm.SVR.pkl')
print('\n')


clf = svm.SVR(kernel='linear', C=1e3)
clf.fit(train_data, train_target)

test_result = clf.predict(test_data)

test_result[test_result > 100.0] = 100.0
test_result[test_result < .0] = 0.0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))
print('\n')

clf = svm.SVR(kernel='poly', C=1e3, degree=2)
clf.fit(train_data, train_target)

test_result = clf.predict(test_data)

test_result[test_result > 100.0] = 100.0
test_result[test_result < .0] = 0.0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))
print('\n')

# train_result = clf.predict(train_data)
# train_result[train_result > 100.0] = 100
# train_result[train_result < .0] = 0
# print(np.corrcoef(train_result, train_target)[0][1])
#
# with open('./results.txt', 'w') as f:
#     for i in list(range(test_result.shape[0])):
#         f.write(str(test_result[i] / 4.0))
#         f.write(' ')
#         f.write(str(test_target[i] / 4.0))
#         f.write('\n')
#
#     for i in list(range(train_target.shape[0])):
#         f.write(str(train_result[i] / 4.0))
#         f.write(' ')
#         f.write(str(train_target[i] / 4.0))
#         f.write('\n')


print('-------------------------- Nu svr  ---------------------------------------')

clf = svm.NuSVR()
clf.fit(train_data, train_target)

test_result = clf.predict(test_data)

test_result[test_result > 100.0] = 100.0
test_result[test_result < .0] = 0.0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))


print('-------------------------- linear svr  ---------------------------------------')

clf = svm.LinearSVR()
clf.fit(train_data, train_target)

test_result = clf.predict(test_data)

test_result[test_result > 100.0] = 100.0
test_result[test_result < .0] = 0.0
print(np.corrcoef(test_result, test_target)[0][1])
print(consistent(test_result, test_target, 15))
print(consistent(test_result, test_target, 25))