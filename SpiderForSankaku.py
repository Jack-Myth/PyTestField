import os
import signal
import time

import requests
import threading
from lxml import etree

imgCount = 0
sankakuURL = "https://chan.sankakucomplex.com"
TargetTag = ""
MaxThread=1
ThreadList=[]
Login=""
Pass_Hash=""
s=requests.session()

def GenSession():
    global s
    s=requests.session()
    s.cookies.set("login", Login)
    s.cookies.set("pass_hash", Pass_Hash)
    s.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
               "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/jpeg,*/*;q=0.8"}

def GetImg(Path):
    global imgCount
    global TargetTag
    global s
    while True:
        try:
            ImgPageResp = s.get(str(Path))
            ImgPageTree = etree.HTML(ImgPageResp.text)
            ImgAddressList = ImgPageTree.xpath('//div[@id="stats"]/ul/li[contains(text(),"Original")]/a/@href')
            if len(ImgAddressList)==0:
                '''Maybe It's not a image(but a Flash or something)'''
                ImgAddressList=ImgPageTree.xpath('//div[@id="non-image-content"]/p/a/@href')
            ImgAddress=ImgAddressList[0]
            break;
        except Exception:
            print("\t\t<i>Exception Detected,Sleep for a while.")
            time.sleep(30)
            GenSession()
    FileName = os.path.basename("https:" + str(ImgAddress))
    FileName = FileName.split("?")[0]
    if MaxThread==1:
        print("\t" + FileName+"...",end="",flush=True)
    r = s.get("https:" + str(ImgAddress))
    r.raise_for_status()
    with open(TargetTag + "/" + FileName, "wb") as f:
        f.write(r.content)
    imgCount += 1
    if MaxThread == 1:
        print("OK")
    else:
        print("\t->" + FileName)


def GetPage(TargetURL):
    global sankakuURL
    global MaxThread
    global ThreadList
    global s
    MyResponce = s.get(TargetURL);
    HTMLTree = etree.HTML(MyResponce.text)
    NextPageList = HTMLTree.xpath('//div[@class="pagination"]/@next-page-url')
    if len(NextPageList) != 0:
        NextPage = NextPageList[0]
    else:
        NextPage = ""
    ImgPathList = HTMLTree.xpath('//div[@class="content"]/div/span/a/@href')
    MaxThreadNum=len(ImgPathList) if len(ImgPathList)<MaxThread else MaxThread
    for ImgPath in ImgPathList:
        t=threading.Thread(target=GetImg,args=(sankakuURL + str(ImgPath),))
        t.setDaemon(True)
        t.start()
        ThreadList.append(t)
        while True:
            for t in ThreadList:
                if not t.isAlive():
                    ThreadList.remove(t)
                    break
            if len(ThreadList)<MaxThreadNum:
                break
            time.sleep(0.1)
    for t in ThreadList:
        t.join()
    ThreadList.clear()
    if NextPage == "":
        return ""
    else:
        return sankakuURL + NextPage


def Exiting(signum, frame):
    print("You choose to exit the script")
    print("The last downloading Page is in the file named \"LastVisitedURL\"")
    print("If you want to continue download, provide the URL before next download.")
    print("Bye~")
    exit()


TargetTag = input("Input the Tag of the image that you want to get:")
TargetTag = TargetTag.replace(" ", "+")
BeginURL = "https://chan.sankakucomplex.com/?tags=" + TargetTag
MaxPage = int(input("Input the max page you want to get:"))
MaxThreadStr=input("Input the max thread you want to use(leave it empty for 1):")
if MaxThreadStr!="":
    MaxThread=int(MaxThreadStr)
Login = input("Input Cookie login")
Pass_Hash = input("Input Cookie pass_hash")
StartPageNum = input("Provide the page you want to begin with(less than 50 or leave it empty):")
inputStartURL=""
if os.path.isfile("LastVisitedURL"):
    shouldUseIt = input("Find \"LastVisitedURL\" File,Use It?[Y/n]")
    if shouldUseIt=="" or shouldUseIt.lower()=="y":
        with open("LastVisitedURL","r") as f:
            inputStartURL=f.readline()
if inputStartURL=="":
    inputStartURL = input("Maybe You want to provide an URL to start from(or leave it empty):")
if StartPageNum != "":
    BeginURL += "&page=" + StartPageNum
if inputStartURL != "":
    BeginURL = inputStartURL
GenSession()
PageNumber = 0
signal.signal(signal.SIGINT, Exiting)
signal.signal(signal.SIGTERM, Exiting)
print("Downloading Page" + str(PageNumber) + "...")
print("Page URL:" + BeginURL)
if not os.path.isdir(TargetTag):
    os.mkdir(TargetTag)
with open("LastVisitedURL", "w") as f:
    f.write(BeginURL)
NextPage = GetPage(BeginURL)
PageNumber += 1
while (NextPage != "" and PageNumber < MaxPage):
    print("Downloading Page" + str(PageNumber) + "...")
    print("Page URL:" + NextPage)
    if NextPage!="":
        with open("LastVisitedURL", "w") as f:
            f.write(NextPage)
    NextPage = GetPage(NextPage)
    PageNumber += 1
print("Seems the downloading is finished.")
print(str(imgCount) + " Images have been downloaded.")
print("You can find them in \"" + TargetTag + "\" folder.")
print("Press any key to exit.")
os.system("pause>nul");
