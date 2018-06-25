#-*-coding:utf-8 -*-
#本脚本用于对指定网站目录下文件进行监控
#编写时间：20180625

import time
import os

initFilesList=[]
checkFileList=[]
count = 0
endTime = ""
monPath = os.getcwd()
def initFiles(monPath):
    global initFilesList
    for p in os.listdir(monPath):
        print initFileslist
        if os.path.isdir(p):
            initFiles(p)
        initFileslist.append(os.path.basename(p))


def main():
    initFiles(monPath)
    print initFilesList

main()