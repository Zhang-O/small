# -*- coding: utf-8 -*-
import os
from doc2txt import strQ2B_, check_chinese

# print(os.listdir('./xulian'))
# for (root, dirs, files) in os.walk('./xulian'):
#     print(root, dirs, files)

BASE_DIR = './xulian/'
SAVE_DIR = './xunlian_txt/'
SAVE_DIR2 = './xunlian_txt2/'

non_ansii_punctuation = set()
non_ansii_punctuation_unicode = set()
non_ansii_punctuation_dict = dict()
chinese = set()

_sum = 0

# --------  transform the docx format file to txt file
for score_dir in os.listdir(BASE_DIR):
    for file in os.listdir(os.path.join(BASE_DIR, score_dir)):
        if file.split('.')[1] == "txt":
            print(file)
            txt_file = os.path.join(os.path.join(BASE_DIR, score_dir), file)
            # rename to std format
            filename = score_dir + '_' + file
            txt_file_save_path = os.path.join(SAVE_DIR, filename)
            with open(txt_file, 'r') as f:
                # with open(txt_file_save_path, 'w') as fw:
                #     fw.write(strQ2B_(f.read()))
                #     _sum += 1
                #     print(_sum)

                for i in f.read():
                    # if ord(i) > 127:
                    #     non_ansii_punctuation.add(i)
                    #     non_ansii_punctuation_unicode.add(ord(i))
                    #     non_ansii_punctuation_dict[i] = ord(i)
                    if check_chinese(ord(i)):
                        chinese.add(i)

print(non_ansii_punctuation)
print(non_ansii_punctuation_unicode)
print(non_ansii_punctuation_dict)
print(chinese)



