# -*- coding: utf-8 -*-

import numpy as np




def consistent(array1, array2, score):

    return np.sum(abs(array1 - array2) <= score) / array1.shape[0]



# a = np.random.rand(1000) * 100
# b = np.random.rand(1000) * 100
# print(a.shape)
# print(b.shape)
# print(np.concatenate((a, b), axis=0))
#
# c = abs(a - b) <= 15
#
# print(np.sum(c, axis=0) / a.shape[0])
#
#
#
# print(consistent(a, b, 15))

