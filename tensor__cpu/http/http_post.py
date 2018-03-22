# -*- coding : utf-8 -*-

import urllib.request
import urllib.parse
import requests
import json
import time
import multiprocessing
import os

# -------- send request by urllib --------

base_url = "http://10.33.2.231:8008"

def urllib_request(num):

    params = urllib.parse.urlencode({'uniqueid':24})
    url = base_url + '/exam/progress/?%s' % params
    req = urllib.request.Request(url)
    req.add_header('appkey', 123456)  # add header

    with urllib.request.urlopen(req) as f:
        data = f.read().decode('utf-8')
        print(type(data))
        print(type(json.loads(data)))
        # print(json.loads(data)['data'])
        json_data = json.loads(data)
        print(json_data)
    if json_data['data']['finished_items'] == json_data['data']['items']:
        return True
    else:
        return False

# print(urllib_request(1))

# -------  send request by requests ---------

def requests_get(num):
    url = base_url + '/exam/progress/'
    payload = {'uniqueid':11111111111}
    headers = {'appkey': str(123456)}
    r = requests.get(url, params=payload, headers=headers)
    print(r.headers)
    print(r.request.headers)
    # print(r.json())
    # print(os.getpid())
    return num


def requests_get1(num):
    url = 'http://202.104.134.107:8008/static/css/adminLte.min.css'
    payload = {'uniqueid':11111111111}
    headers = {'appkey': str(123456)}
    r = requests.get(url, params=payload, headers=headers)
    with open('./' + url.split('/')[-1], 'wb') as f:
        f.write(r.content)

    return num


# -------  send request with upload file by requests ---------

def requests_post(num):
    url = 'http://10.33.2.160:9090/h5voicemp3/callback'
    headers = {"Content-Type": "application/json"}
    payload = {
            'score':100,
            'taskid':100,
            'msg':'success'
            }

    r = requests.post(url,headers=headers, data=json.dumps(payload) )
    print(r.headers)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)




def requests_post1():
    url = 'http://202.104.134.107:8008/voice/posttest/'
    headers = {"Content-Type": "application/json"}
    payload = {
            'score':100,
            'taskid':100,
            'msg':'success'
            }

    r = requests.post(url,headers=headers, data=json.dumps(payload) )
    print(r.headers)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)

# requests_post1()


def mrequest(taskid, post_url, itemscore):
    # payload={'audioFormat':'mp3'}
    # headers={'appkey':'123456'}
    headers = {"Content-Type": "application/json"}
    payload = {
        'score': itemscore,
        'taskid': taskid
    }
    # payload = {
    #       'score':100,
    #       'taskid':100
    #       }


    r=requests.post(post_url, headers=headers, data=json.dumps(payload))
    print(r.headers)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)

mrequest(100,'http://202.104.134.107:8008/voice/posttest/',100)





