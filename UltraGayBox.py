#! /usr/bin/env python
# encoding: utf-8
'''
@author:JackMyth
@contact:wwwbkkk@126.com
@file: UltraGayBox.py
@time:2018/11/21 15:27
'''
import json
import random
from time import sleep

import requests

MinRank=7

def ImGood(HowGoodIam):
    return
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s=requests.session()
    s.headers=\
        {
            "Connection":"keep-alive",
            "User-Agent":"Mozilla/5.0 (Linux; Android 8.1; ONEPLUS A5000 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x26070233) NetType/4G Language/zh_CN",
            "Accept":"*/*",
            "Referer":"https://api.xiaoheihe.cn/game/festival_activity/index/share/?heybox_id=11712790&sid=dbac4eb11bd149a817aec395dd8a00cd&act_id=5bf260fa98c8ff0bec3dc0dd",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,en-US;q=0.8",
            "X-Requested-With": "com.tencent.mm"
        }
    sa1 = []
    sa2 = []
    for i in range(HowGoodIam):
        sa1.clear()
        sa2.clear()
        for i in range(8):
            sa1.append(random.choice(seed))
        for i in range(19):
            sa2.append(random.choice(seed))
        salt = ''.join(sa1) + "-" + ''.join(sa2)
        s.cookies.set("usrid", salt)
        print(salt)
        r = s.get(
            "https://api.xiaoheihe.cn/game/festival_activity/share_support/?heybox_id=11712790&sid=dbac4eb11bd149a817aec395dd8a00cd&act_id=5bf260fa98c8ff0bec3dc0dd")

mainS=requests.session()
mainS.headers=\
    {
        "Connection":"keep-alive",
        "Accept":"application/json, text/plain, */*",
        "User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; ONEPLUS A5000 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36",
        "Referer":"https://api.xiaoheihe.cn/game/festival_activity/index/?heybox_id=11712790&act_id=5bf260fa98c8ff0bec3dc0dd&sid=dbac4eb11bd149a817aec395dd8a00cd&os_type=Android&version=1.1.40&os_version=8.1.0&imei=99001062484874&_time=1542783445",
        "Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,en-US;q=0.9"
    }
mainS.cookies.set("user_heybox_id","11712790")
mainS.cookies.set("user_pkey","MTUzNzYyODk4NC42OF8xMTcxMjc5MHN5bXJxemxxcmF6YXFxbmQ__")
mainS.cookies.set("Hm_lvt_16e641db29b184261dffedec98f2570b","1541119389")
mainS.cookies.set("Hm_lpvt_16e641db29b184261dffedec98f2570b","1541119457")
while(True):
    mainR=mainS.get("https://api.xiaoheihe.cn/game/festival_activity/data/?heybox_id=11712790&act_id=5bf260fa98c8ff0bec3dc0dd&sid=dbac4eb11bd149a817aec395dd8a00cd&os_type=webinapp")
    jsonobj=json.loads(mainR.text)
    if jsonobj["result"]["error"]==0:
        ranklist= jsonobj["result"]["share_award"]["rank_list"]
        haveme=False
        for i in range(len(ranklist)):
            if ranklist[i]["user_info"]["username"]=="Jack.Myth":
                haveme=True
                print("Current Rank:"+str(i+1))
                if i>=MinRank:
                    print("Too low,need rise...")
                    ImGood(2)
                else:
                    break
        if haveme==False:
            ImGood(10)
    sleep(5)