#! /usr/bin/env python
# encoding: utf-8
'''
@author:JackMyth
@contact:wwwbkkk@126.com
@file: GoodGayBox.py
@time:2018/11/21 12:24
'''
import random

import requests

tttttimes=int(input("How many Like you want to get?"))
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
for i in range(tttttimes):
    sa1.clear()
    sa2.clear()
    for i in range(8):
        sa1.append(random.choice(seed))
    for i in range(19):
        sa2.append(random.choice(seed))
    salt = ''.join(sa1) + "-" + ''.join(sa2)
    s.cookies.set("usrid", salt)
    print(salt)
    r = s.get("https://api.xiaoheihe.cn/game/festival_activity/share_support/?heybox_id=11712790&sid=dbac4eb11bd149a817aec395dd8a00cd&act_id=5bf260fa98c8ff0bec3dc0dd")