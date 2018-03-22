# -*-encoding: utf-8 -
import requests
import time
import hashlib
import random
import sys

access_key = "6f524f16"
access_secret = "019c299e69ce"
timestamp = str(int(time.time()))
nonce = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 5))
signature = hashlib.sha1(''.join(sorted([access_key, timestamp, nonce, access_secret])).encode("utf8")).hexdigest()
# url = 'http://www.kaoyanjiayou.com/api/v1/open/app/correct'
url ='http://kaoyan.hexinedu.com/api/v1/open/app/correct'

file = open('./3.jpg', 'rb')

req = requests.post(
    url,
    files={'file': file},
    data={'access_key': access_key, 'timestamp': timestamp, 'nonce': nonce, 'signature': signature}  # 身份验证
)
file.close()
res = req.json()
#print "1-------req=",req
task_id = res['data']['task_id']
while 1:  # 等待打分结果，获取到结果时跳出
    req = requests.get(url, {
        'access_key': access_key, 'timestamp': timestamp, 'nonce': nonce, 'signature': signature, # 身份验证
        'task_id': task_id,  # 上一步得到的task_id
        'include_text': True,  # 包括识别结果
    })
    #print "2----------req=",req
    res = req.json()

    if res['code']:
        #print 'wait......'
        time.sleep(3)
    else:
        print(res['data'])
        break

'''
{'score': 19.0, 'lines': ['', 'A letter to my best friend. ', 'Dear Tom,\n', "I don't know how to thank you these years. As ", 'the best friend of mine, you give me too much love ', "and care. You're the sunshine of my life ", "Last year, I couldn't believe that I could ", 'go to a good univercity because of my bad grade. ', 'At that time, you encouraged me everyday and gave ', 'me so much courage. You always took after me when ', 'I was ill, I still remember the moment that we ', 'studyed English every Sunday morning. Now, I have ', 'enterred a good university. There is no doubt that ', 'you helped me most when I was so sad. ', 'As we all know, friends are very important in ', "one's lifetime. We must thank them and care them.\n", 'Yours, Li Ming.']}



'''