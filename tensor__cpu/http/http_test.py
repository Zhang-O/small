# -*- coding : utf-8 -*-

import urllib.request
import urllib.parse
import requests
import json
import time
import multiprocessing
import os

# -------- send request by urllib --------

base_url = "http://10.33.3.93:8008"

def urllib_request(num):

    params = urllib.parse.urlencode({'uniqueid':314})
    url = base_url + '/exam/progress/?%s' % params
    req = urllib.request.Request(url)
    req.add_header('appkey', 123456)  # add header

    with urllib.request.urlopen(req) as f:
        data = f.read().decode('utf-8')
        # print(type(data))
        # print(type(json.loads(data)))
        # print(json.loads(data)['data'])
        json_data = json.loads(data)
        # print(json_data)
    if json_data['data']['finished_items'] == json_data['data']['items']:
        return True
    else:
        return False

print(urllib_request(1))

# -------  send request by requests ---------

def requests_get(num):
    url = base_url + '/exam/progress/'
    payload = {'uniqueid':11111111111}
    headers = {'appkey': str(123456)}
    r = requests.get(url, params=payload, headers=headers)
    # print(r.json())
    # print(os.getpid())
    return num



# -------  send request with upload file by requests ---------

def requests_post(num):
    url = base_url + '/voice/eval/'
    payload = {'audioFormat': 'mp3'}
    headers = {'appkey': str(123456)}
    data_form = {
            'text': "We've got to the bottom of the ocean but it's not the end of the journey."
                    " Because the power of the earth machine beneath the seafloor affects the lives of millions of people."
                    " As the seafloor spreads out from the Mid Ocean ridge it eventually collides with the land."
                    " Massive pressure builds up.  Until suddenly it gives. "
                    "This is what happened off the coast of Japan in March, 2011. "
                    "An earthquake beneath the sea floor created the devastating tsunami that hit Japan. "
                    "It was a horribly power reminder that the whole of the pacific region is very "
                    "unstable and earthquakes are frequent.",
            'type': 'Read',
            'mode': 'A',
            'examUniqueID': 314
            }

    path = '''c:/zhang/AI/Doctor_Luo/student_answers/voiceType/100V1.0.1/zip_638798/1190416241/QT-742440ans.mp3'''
    #path = './QT-742440ans.mp3'
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




if __name__ == "__main__":
    result = []

    cpu_count = multiprocessing.cpu_count()
    localtime0 = time.asctime(time.localtime(time.time()))
    print(localtime0)
    t0 = time.time()
    # p = multiprocessing.Process(target = get_http, args = (10,))
    # p.start()
    # print("p.pid:", p.pid)
    # print("p.name:", p.name)
    # print("p.is_alive:", p.is_alive())
    #
    # p.join()
    # print('end')

    #pool = multiprocessing.Pool(processes=5)
    for i in range(10):
        requests_post(1)
        #result.append(pool.apply_async(requests_post, (i, ))) # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        # result.append(pool.apply_async(os.getpid, ()))
        # print(result[i].get())
        # pool.apply_async(requests_get, (i,))
    # multiple_result = [pool.apply_async((requests_get, (i,))) for i in range(100)]

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    #pool.close()
    #pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    t1 = time.time()
    print('time sp', (t1-t0,))
    localtime1 = time.asctime(time.localtime(time.time()))
    print(localtime1)
    print("Sub-process(es) done.")
    # print('NUM_SUCCESS', NUM_SUCCESS)

    print('length', len(result))
    # print(result)

    # when uploading is done , poll the progress
    while not urllib_request(1):
        # print('not over')
        pass

    print('over')

    localtime2 = time.asctime(time.localtime(time.time()))
    print(localtime2)

