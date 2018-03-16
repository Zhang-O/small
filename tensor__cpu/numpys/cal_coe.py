# -*- coding: utf-8 -*-

import numpy as np

predict_score = []
human_score = []
fea1 = []
fea2 = []
fea3 = []
fea4 = []
fea5 = []
fea6 = []
op1 = []
op2 = []
op3 = []

feas = [fea1, fea2, fea3, fea4, fea5, fea6, op1, op2, op3, predict_score, human_score]


with open('./test_result1.txt', 'r') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]
    for line in lines:
        predict_score.append(line[-2])
        human_score.append(line[-1])

        fea1.append(line[0])
        fea2.append(line[1])
        fea3.append(line[2])
        fea4.append(line[3])
        fea5.append(line[4])
        fea6.append(line[5])
        op1.append(line[6])
        op2.append(line[7])
        op3.append(line[8])

feas = np.array(feas, dtype='float32')

print(feas.shape)
print(np.corrcoef(feas[9], feas[10])[0][1])
print(np.corrcoef(feas[8], feas[10])[0][1])
print(np.corrcoef(feas[7], feas[10])[0][1])
print(np.corrcoef(feas[6], feas[10])[0][1])
print(np.corrcoef(feas[5], feas[10])[0][1])
print(np.corrcoef(feas[4], feas[10])[0][1])
print(np.corrcoef(feas[3], feas[10])[0][1])
print(np.corrcoef(feas[2], feas[10])[0][1])
print(np.corrcoef(feas[1], feas[10])[0][1])




# predict_score = np.array(predict_score, dtype='float32')
# human_score = np.array(human_score, dtype='float32')

# print predict_score.dtype
# print human_score.dtype

# for item_ in feas:
#     print np.corrcoef(item_, human_score)

# print np.corrcoef(feas[0], feas[1])

