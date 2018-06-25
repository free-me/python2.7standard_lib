#__*__coding:utf-8 __*__
#Auth 启明星辰
#time 20180625
#
import os
import time
import shutil
import sys

fileList = [] #文件临时存放列表
tempDir = "c:\logs" #新添加文件移动位置
count = 0
endTime = "2018-07-15" #指定脚本停止时间
monPath = os.getcwd()


#初始化文件列表
def initFiles(monPath):
    global count
    global fileList
    dir_list = []
    for p in os.listdir(monPath):
        fullname = os.path.join(monPath,p)
        if os.path.isdir(fullname):
            initFiles(fullname)
        print fullname
        fileList.append(os.path.abspath(fullname))
        count = count+1


#检查更新
def checkFileList(monPath):
    global fileList
    print "check list file!"
    #time.sleep(10)
    for p in os.listdir(monPath):
        fullname = os.path.join(monPath,p)
        if os.path.isdir(fullname):
            print fullname
            checkFileList(fullname)
        if fullname not in fileList:
            print "move files to logs"
            print fullname
            shutil.move(fullname, tempDir)
            print "mvoe  succeed!!!"

def main():
    global fileList
    try:
        os.mkdir(tempDir)
    except WindowsError:
        pass
    initFiles(monPath)
    print "初始化完成共统计%s个文件!!!" % count
    print fileList
    t = 0
    while True:
        checkFileList(monPath)
        time.sleep(1)
        t = t+1
        if time.strftime("%y-%m-%d") =="18-07-15":
            break
    print "script stop!!!"

main()


