# 每隔1s打印https://ak-conf.hypergryph.com/config/prod/official/Android/version
# 用于监控游戏版本号

import requests
import time

url = 'https://ak-conf.hypergryph.com/config/prod/official/Android/version'
old = '{"resVersion":"23-07-24-13-21-30-90fb63","clientVersion":"2.0.40"}'

while True:
    try:
        r = requests.get(url)
        if r.status_code == 200:
            if r.text != old:
                print('version change')
                print(r.text)
                old = r.text
            print('version not change')
    except:
        print('error')
    time.sleep(1)