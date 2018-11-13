#! /usr/bin/env python
# encoding: utf-8
'''
@author:JackMyth
@contact:wwwbkkk@126.com
@file: EveryDayHPic.py
@time:2018/11/13 20:57
'''
import os
import random

from lxml import etree

import requests
import zxing


QRPath="./EveryDayHPic/QR"
ImgPath="./EveryDayHPic/Pic"
s=requests.session()
s.headers={"User-Agent": "Mozilla/5.0 (Linux; Android 7.0; SM-G920F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
               "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/jpeg,*/*;q=0.8"}

def DownImage(websiteURL):
    HTMLrespond = s.get(websiteURL)
    HTMLTree=etree.HTML(HTMLrespond.text)
    Imglist = HTMLTree.xpath('//div[@class="note-content"]/div/img/@src')
    for ImgURL in Imglist:
        ImgRespond = s.get(str(ImgURL))
        filename = str(random.randint(0,1000000))+".jpg"
        while os.path.isfile(ImgPath+"/"+filename):
            filename = str(random.randint(0, 1000000)) + ".jpg"
            with open(filename, "wb") as f:
                f.write(ImgRespond.content)


QRList = os.listdir(QRPath)
zx = zxing.BarCodeReader()
for File in QRList:
    FilePath=QRPath+"/"+File
    website = zx.decode(FilePath,True)
    print(File)
    DownImage(website.raw)
print("Finished!")