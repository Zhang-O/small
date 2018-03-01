# -*- coding : utf-8 -*-

import urllib.request
import urllib.parse
import requests
import json
import time
import multiprocessing
import os
from args_http import args


base_url = "http://10.33.2.231:8008"

# single post request
def requests_post( **arg ):
    interface = arg['interface']
    text = arg['text']
    item_type = arg['type']
    examUniqueID = arg['examUniqueID']
    path = arg['path']

    url = base_url + interface
    payload = {'audioFormat': 'mp3'}
    headers = {'appkey': str(123456)}
    data_form = {
            'text': text,
            'type': item_type,
            'mode': 'A',
            'examUniqueID': examUniqueID
            }
    # path = './QT-742440ans.mp3'
    path = path
    t0 = time.time()
    with open(path,'rb') as f:
        # print(f.read())
        files = {'voice':f}
        # print(data_form)
        r2 = requests.post(url, params=payload, headers=headers, data=data_form, files=files)
        # print(r2.headers)
        t1 = time.time()
        print(t1-t0)
        # print(r2.json())
        # print(r2.text)
        # print(r2.request.headers)

# requests_post(1)


# single student
def post_student_ans(num):
    for arg in args:
        requests_post(**arg)


if __name__ == "__main__":
    result = []

    cpu_count = multiprocessing.cpu_count()
    # currnet time
    localtime0 = time.asctime(time.localtime(time.time()))
    print(localtime0)

    t0 = time.time()



    pool = multiprocessing.Pool(processes=4)
    for i in range(1):
        post_student_ans(i)
        #result.append(pool.apply_async(post_student_ans, (i, ))) # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        # result.append(pool.apply_async(os.getpid, ()))
        # print(result[i].get())
        # pool.apply_async(requests_get, (i,))

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束

    t1 = time.time()
    print('time sp', (t1-t0,))

    # time over
    localtime1 = time.asctime(time.localtime(time.time()))
    print(localtime1)
    print("Sub-process(es) done.")
    print('length', len(result))

    # when uploading is done , poll the progress
    # while not urllib_request(1):
    #     # print('not over')
    #     pass

    print('over')

    localtime2 = time.asctime(time.localtime(time.time()))
    print(localtime2)

