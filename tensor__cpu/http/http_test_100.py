# -*- coding : utf-8 -*-

import urllib.request
import urllib.parse
import requests
import json
import time
import multiprocessing
import os


# base_url = "http://10.33.2.231:8008"
base_url = "http://edu.hivoice.cn:8085/eval/mp3"


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
            'mode': 'D',
            'examUniqueID': 2017110901
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
        print(r2.text)
        # print(r2.request.headers)

# requests_post(1)



if __name__ == "__main__":

    localtime0 = time.asctime(time.localtime(time.time()))
    print(localtime0)
    t0 = time.time()

    for i in range(100):
        requests_post(1)
    t1 = time.time()
    print('time sp', (t1-t0,))
    localtime1 = time.asctime(time.localtime(time.time()))
    print(localtime1)


