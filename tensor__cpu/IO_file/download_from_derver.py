# -*- coding:utf-8 -*-
# Filename: try.py
# Author：zhang
# Date: 2018/3/4 22:41
"""
直接从服务器下载文件，不需要服务器搭建了  文件服务器
"""


import paramiko
import os

HOST_IP = '59.110.12.72'
REMOTE_PATH = '/proc'
REMOTE_FILENAME = 'meminfo'
LOCAL_PATH = './proc'
USERNAME = 'niu'
PASSWORD = '123456'


def remote_scp(host_ip, remote_path, local_path, file_name, username, password):
    t = paramiko.Transport((host_ip, 22))
    t.connect(username=username, password=password)  # 登录远程服务器
    sftp = paramiko.SFTPClient.from_transport(t)  # sftp传输协议
    src = remote_path + '/' + file_name
    des = local_path + '/' + file_name
    sftp.get(src, des)
    t.close()


if not os.path.isdir(LOCAL_PATH):
    os.makedirs(LOCAL_PATH)
if not os.path.isfile(LOCAL_PATH + '/' + REMOTE_FILENAME):
    fp = open(LOCAL_PATH + '/' + REMOTE_FILENAME, 'w')
    fp.close()

remote_scp(HOST_IP, REMOTE_PATH, LOCAL_PATH, REMOTE_FILENAME, USERNAME, PASSWORD)