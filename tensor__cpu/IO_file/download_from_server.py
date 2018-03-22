# -*- coding:utf-8 -*-
# Filename: try.py
# Author：zhang
# Date: 2018/3/4 22:41
"""
直接从服务器下载文件，不需要服务器搭建了  文件服务器
"""


import paramiko
import os

HOST_IP = '10.33.3.91'
basic_files = ["TestRecord.mp3", "QT-960341ans.mp3", "QT-562662ans.mp3", "QT-354093ans.mp3", "QT-37370ans.mp3", "Display.log", "Answer.xml"]
BASIC_LOCAL_PATH = './new/'
USERNAME = 't91'
PASSWORD = 't91123'
remote_basic_path = "/home/t91/kaldi/egs/NBAutoScore/s5/part1/2101/"


t = paramiko.Transport((HOST_IP, 22))
t.connect(username=USERNAME, password=PASSWORD)  # 登录远程服务器
sftp = paramiko.SFTPClient.from_transport(t)  # sftp传输协议

with open('./exception_file.txt') as f:
    paths = f.readlines()

all_mid_paths = []
for path in paths:
    print(path)
    mid_path = '/'.join(path.strip().split('/')[5:])[0: -4]
    all_mid_paths.append(mid_path)
    dir_name = path.strip().split('/')[-1][0 :-4]
    print(mid_path)
    print(dir_name)
    if not os.path.isdir(BASIC_LOCAL_PATH + dir_name):
        os.makedirs(BASIC_LOCAL_PATH + dir_name)

    # if not os.path.isfile(LOCAL_PATH + '/' + REMOTE_FILENAME):
    #     fp = open(LOCAL_PATH + '/' + REMOTE_FILENAME, 'w')
    #     fp.close()

    for filename in basic_files:
        des_file = BASIC_LOCAL_PATH + dir_name + '/' + filename
        if not os.path.isfile(des_file):
            fp = open(des_file, 'w')
            fp.close()
        src_file = remote_basic_path + mid_path + '/' + filename
        print(src_file)

        # sftp.get(src_file, des_file)


t.close()




