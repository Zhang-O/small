# -*- coding:utf-8 -*-
# Filename: try.py
# Author：zhang
# Date: 2018/3/4 22:41
"""

"""
import time, random
from hashlib import sha1
import hmac
import base64
import requests
import json


def generate_sign():
    AppID = ""
    SecretID = ""
    SecretKey = ""

    u = 691259192
    t = int(time.time())
    e = int(time.time() + 1000)
    r = random.randint(1, 100000)

    orignal = 'u={}&a={}&k={}&e={}&t={}&r={}&f='.format(u, AppID, SecretID, e, t, r)

    my_sign = hmac.new(SecretKey.encode('utf-8'), msg=orignal.encode('utf-8'),
                       digestmod=sha1).digest() + orignal.encode('utf-8')
    my_sign = base64.b64encode(my_sign)
    return my_sign


def requests_post1(sign, url_image):
    url = 'https://api.youtu.qq.com/youtu/ocrapi/handwritingocr'
    headers = {
        "Content-Type": "application/json",
        "Host": "api.youtu.qq.com",
        "Authorization": sign
    }
    payload = {
        "app_id": "10119527",
        "url": url_image,
        "session_id": "10",
        "options": {"language": "lat"}
    }

    r = requests.post(url, headers=headers, data=json.dumps(payload))
    return json.loads(r.text)['items']


def requests_post1_from_str(sign, image):

    f = open(image, 'rb')  # 二进制方式打开图文件
    str_img = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()

    # print(str_img)

    url = 'https://api.youtu.qq.com/youtu/ocrapi/handwritingocr'
    headers = {
        "Content-Type": "application/json",
        "Host": "api.youtu.qq.com",
        "Authorization": sign
    }
    payload = {
        "app_id": "10119527",
        "image": bytes.decode( str_img),
        "session_id": "10",
        "options": {"language": "lat"}
    }

    r = requests.post(url, headers=headers, data=json.dumps(payload))
    return json.loads(r.text)['items']



sign = generate_sign()
# url_image = "http://202.104.134.107:8008/id_img/tencent/121963171115926-1.jpg"

image = "121963171115926-1.jpg"

# items = requests_post1_from_str(sign, image)
# rec = ' '.join([item["itemstring"] for item in items])
# txt_file = 'tec.txt'
# with open(txt_file, 'w') as f:
#     f.write(rec)

def img2txt(image, sign, txt_file):
    items = requests_post1_from_str(sign, image)
    rec = ' '.join([item["itemstring"] for item in items])

    with open(txt_file, 'w') as f:
        f.write(rec)


sign = generate_sign()
# url_image = "http://202.104.134.107:8008/id_img/tencent/121963171115926-1.jpg"

image = "121963171115926-1.jpg"
txt_file = 'tec.txt'
img2txt(image, sign, txt_file)