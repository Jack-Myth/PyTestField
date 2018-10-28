#! /usr/bin/env python
# encoding: utf-8
'''
@author:JackMyth
@contact:wwwbkkk@126.com
@file: tmpProcessFile.py
@time:2018/10/28 13:57
'''
import string
from sys import argv

hanzip=('】。》…」』')

with open(argv[1],"r") as f:
    output=open(argv[2],"w")
    lastcharacter=''
    while True:
        line=f.readline()
        if(not line):
            break
        if(string.punctuation.find(lastcharacter)!=-1):
            output.write("\n")
        elif (hanzip.find(lastcharacter) != -1):
            output.write("\n")
        if(line!="\n"):
            lastcharacter = line[-2]
            line=line.replace("    ","",1)
            line=line.replace("\n","")
            output.write(line)
            if (len(line) < 20):
                output.write("\n")
                lastcharacter='x'