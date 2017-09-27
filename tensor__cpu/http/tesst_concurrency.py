# coding = utf-8

from urllib import request, parse
from urllib.error import URLError
import json
import multiprocessing
import time

NUM_SUCCESS = 0

# def get_http(num):
#     global NUM_SUCCESS
#
#     while num > 0:
#         url = 'http://10.33.2.61:8008/score/queryanswer/?examid=3003&paperid=PAPER-14777&itemid=4-1&studentid=217167569'
#         req = request.Request(url=url)
#         # print(req)
#
#         res_data = request.urlopen(req)
#         # print(res_data)
#         res = res_data.read()
#         json_data = json.loads(res.decode('utf-8'))
#         print(json_data)
#         if json_data['code'] == 200:
#             NUM_SUCCESS += 1
#             print('NUM_SUCCESS', NUM_SUCCESS)
#         num -= 1

result = []

def get_http(num):

    global NUM_SUCCESS
    url = 'http://10.33.2.61:8008/score/queryanswer/?examid=3003&paperid=PAPER-14777&itemid=4-1&studentid=217167569'
    req = request.Request(url=url)
    # print(req)

    res_data = request.urlopen(req)
    # print(res_data)
    res = res_data.read()
    json_data = json.loads(res.decode('utf-8'))
    # print(json_data)
    if json_data['code'] == 200:
        NUM_SUCCESS += 1
        # print(num)
        return num
        # print('NUM_SUCCESS', NUM_SUCCESS)


if __name__ == "__main__":
    cpu_count = multiprocessing.cpu_count()
    t0 = time.time()
    # p = multiprocessing.Process(target = get_http, args = (10,))
    # p.start()
    # print("p.pid:", p.pid)
    # print("p.name:", p.name)
    # print("p.is_alive:", p.is_alive())
    #
    # p.join()
    # print('end')

    pool = multiprocessing.Pool(processes=cpu_count)
    for i in range(10000):
        result.append(pool.apply_async(get_http,(i,))) # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    t1 = time.time()
    print('time sp', (t1-t0,))
    print("Sub-process(es) done.")
    # print('NUM_SUCCESS', NUM_SUCCESS)

    print('length', len(result))
