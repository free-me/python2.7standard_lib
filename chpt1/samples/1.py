#__*__coding:utf-8 __*__
#os模块操作目录
#listdir
import os
import time
import datetime
reload(os)

fileList = []
checkFileLists = []
scanExt = []
count = 0
endTime = "2018-07-15"
monPath = os.getcwd()
def initFiles(monPath):
    global count
    global fileList
    #print '1'
    dir_list = []
    for p in os.listdir(monPath):
        print fileList, "1"
        if os.path.isdir(p):
            initFiles(p)
        fileList.append(os.path.basename(p))
        if os.path.basename(p) not in fileList:
            if os.path.splitext(p)[1] in ["java","jsp","asp","php","aspx"]:
                #os.remove(os.path.abspath(p))
                print "要删除的文件为："+ os.path.abspath(p)
        newExt = list(set(fileList))
        print fileList


def checkFileList(monPath):
    global checkFileLists
    for p in os.listdir(monPath):
        if os.path.isdir(p):
            checkFileList(p)
        if os.path.splitext(p)[1] in checkFileLists:
            print p

def newTime():
    t = time.time()
    t1 = time.strftime("%Y-%m-%d", time.localtime(t))
    return t1
def main():
    #global endTime
    #print newTime()
    if time.strftime("%y-%m-%d") =="2018-06-21":
        print "this now end!!"
    initFiles(monPath)

    print os.path.abspath("builtin-apply-example-1.py")
    while True:
        checkFileList(monPath)
        time.sleep(5)



if __name__ == '__main__':
    main()


