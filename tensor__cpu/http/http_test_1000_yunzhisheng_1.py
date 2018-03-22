# -*- coding : utf-8 -*-

import urllib.request
import urllib.parse
import requests
import json
import time
import multiprocessing
import os
import pymysql

config = {
    'db': 'AItest',
    'user': 'user',
    'passwd': '123456',
    'cursorclass': pymysql.cursors.DictCursor,
    'host': '10.33.2.231',
    'use_unicode': True
}

base_url = "http://edu.hivoice.cn:8085/eval/mp3"

text = 'It is summer. It is midnight. We are headed south. As they travel south, the men and women in this ship will be bitterly cold. Some will burn their faces, wind will sear them, but they will feel fortunate to have become part of a great adventure. For thousands of years, as human beings spread across the planet, no one came here. Antarctica was as remote as the moon. Ancient Greeks reasoned that the world was round, and that there must be a great southern continent. They imagined a land of strange beasts. It was the greatest mystery on Earth.'


# -------  send request with upload file by requests ---------
def requests_post(arg, factor):
    conn = pymysql.connect(**config)
    try:
        with conn.cursor() as cursor:
            try:
                cursor.execute('insert into yun (studentid, score_human, score_coefficient, begin) VALUES (%s ,%s, %s, %s)',
                               (arg['studentid'], arg['score_human'], factor, int(time.time())))
                conn.commit()
                conn.close()


                url = base_url
                headers = {'appkey': "u7capvdv33lozvoarpz2uagbptwgczgb7oy76ga3", 'score-coefficient': str(factor)}
                data_form = {
                        'text': text,
                        'mode': 'D',
                        }

                path = '''./A-1000/''' + arg['file']
                t0 = time.time()
                with open(path,'rb') as f:
                    files = {'voice':f}
                    r2 = requests.post(url, headers=headers, data=data_form, files=files)
                    t1 = time.time()
                    print(t1-t0)
                    result= r2.json()['lines'][0]
                    m_score = result['score']
                    fluency = result['fluency']
                    pronuciation = result['pronunciation']
                    intergrity = result['integrity']


                    conn = pymysql.connect(**config)
                    with conn.cursor() as cursor:
                        cursor.execute("update `yun` set `score_machine`=%s,`fluency`=%s ,`pronuciation`=%s, `intergrity`=%s, end=%s, file=%s where `studentid`=%s and score_coefficient=%s",(m_score, fluency, pronuciation, intergrity,int(time.time()), arg['file'], arg['studentid'], factor))
                        conn.commit()
                    conn.close()


            except Exception:
                print(Exception)
    except Exception:
        print(Exception)





# [0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]

for factor in [1.0, 1.2]:
    with open('./index.txt') as f:
        contents = f.readlines()[1:]
        content = [content.split('\t') for content in contents ]
        for line in content:
            arg = {'studentid': line[2], 'score_human': line[4], 'file': line[3] }
            requests_post(arg, factor)


if __name__ == "__main1__":

    localtime0 = time.asctime(time.localtime(time.time()))
    print(localtime0)
    t0 = time.time()

    for i in range(100):
        requests_post(1)
    t1 = time.time()
    print('time sp', (t1-t0,))
    localtime1 = time.asctime(time.localtime(time.time()))
    print(localtime1)


