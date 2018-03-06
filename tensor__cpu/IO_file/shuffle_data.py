import os
from sklearn.cross_validation import train_test_split
import shutil

SAVE_DIR = './xunlian_txt/'
train_dir = './xunlian_txt2/train/'
test_dir = './xunlian_txt2/test/'

data = os.listdir(SAVE_DIR)
train, test = train_test_split(data, test_size = 0.3)

print(len(train))
print(len(test))

for file_ in train:
    shutil.copy(SAVE_DIR + file_, train_dir)

for file_ in test:
    shutil.copy(SAVE_DIR + file_, test_dir)