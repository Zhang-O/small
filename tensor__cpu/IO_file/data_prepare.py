# -*- coding: utf-8 -*-
import os
from doc2txt import doc2txt

# print(os.listdir('./xulian'))
#
# for (root, dirs, files) in os.walk('./xulian'):
#     print(root, dirs, files)

BASE_DIR = './xulian/'
SAVE_DIR = './xunlian_txt/'
SAVE_DIR2 = './xunlian_txt2/'

# --------  transform the docx format file to txt file
for udir in os.listdir(BASE_DIR):
    for file in os.listdir(os.path.join(BASE_DIR, udir)):
        doc_file = os.path.join(os.path.join(BASE_DIR, udir), file)

        filename = udir + '_' + file.split('.')[0] + '.txt'
        txt_file = os.path.join(SAVE_DIR, filename)
        doc2txt(doc_file, txt_file)


# 160 --> 32
for ufile in os.listdir(SAVE_DIR):
    with open(os.path.join(SAVE_DIR, ufile),'r', encoding='utf-8') as f1:
        ustring = f1.read()

        rstring = ""
        for uchar in ustring:
            inside_code = ord(uchar)
            if inside_code == 160:  # 全角空格直接转换
                inside_code = 32
            rstring += chr(inside_code)

        with open(os.path.join(SAVE_DIR2, ufile), 'w') as f2:
            f2.write(rstring)


# check file encode
with open(SAVE_DIR2 + '24.0_16694168510253.txt', 'r') as f:
    for i in f.read():
        print(ord(i))
        print(i)


