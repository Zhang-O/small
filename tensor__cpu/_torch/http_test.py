# -*- coding : utf-8 -*-
import urllib.request
import urllib.parse
import json

params = urllib.parse.urlencode({'uniqueid':11111111111})
url = 'http://202.104.134.108:8008/exam/progress/?%s' % params
req = urllib.request.Request(url)
req.add_header('appkey', 123456)

with urllib.request.urlopen(req) as f:
    data = f.read().decode('utf-8')
    print(type(data))
    print(type(json.loads(data)))
    print(json.loads(data)['data'])
