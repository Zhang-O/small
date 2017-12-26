# -*- coding: utf-8 -*-

from sklearn import preprocessing
import numpy as np

X_train = np.array([[ 1., 1.,  1.], [ 1.,  1.,  1.], [ 1.,  1., -1.]])
X_scaled = preprocessing.scale(X_train)
print(X_scaled)

def get_scaler_from_data(data):
    return preprocessing.StandardScaler().fit(data)

scaler = get_scaler_from_data(X_train)
print(scaler)
print(scaler.transform(X_train))