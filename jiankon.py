# -!- coding: utf-8 -!-
import time
import threading
import os
from colorama import init,Fore,Back,Style
init(autoreset=True)

global cd
def shuaxin():
    global cd
    global vulns
    g=open(os.getcwd()+"\\log\\vulns.txt")
    lines=g.readlines()
    cd=len(lines)//3
    vulns = []
    for ii in range(cd):
        vulns.append([])
    i=0
    n=0
    try:
        for line in lines:
            i = i + 1
            if  not (i % 3) == 0 :
                vulns[n].append(line.strip())
            else:
                vulns[n].append(line.strip())
                n += 1
    except:
        pass
        # print('报错了！')

def get_vulnlog():
    global cd
    shuaxin()
    print("漏洞列表：")
    for vl in vulns:
        print(vl[0]+'    '+'\033[1;34;40m'+vl[2]+'\n', end=' ', flush=True)

    while 1:
        newlen=len(open(os.getcwd()+"\log\\vulns.txt").readlines())
        if not cd==newlen//3:
            lennew=newlen // 3-cd  #多出来的长度
            shuaxin()
            for shuzi in range(lennew):
                print(vulns[-(shuzi+1)][0]+'    '+'\033[1;34;40m'+vulns[-(shuzi+1)][2]+'    '+'\033[1;34;39m'+get_log()+'\n', end=' ', flush=True)
            cd =newlen // 3


def get_log():
    l = open(os.getcwd()+"\log\\vulns.txt").readlines()
    cd = len(l) // 3
    t = open(os.getcwd()+"\log\\logs.txt")
    x = open(os.getcwd()+"\\result.txt", encoding='gbk')
    lines=x.readlines()
    res = t.readlines()
    jd='进度：'+str(len(res)) + "/" + str(len(lines)) #进度
    bfb='百分比: {:.2%}'.format(len(res) / (len(lines))) #百分比
    sl='漏洞数：' + str(cd) #漏洞数
    out=jd+'  '+bfb+'  '+sl
    return out
def start_log():
    # 清除上次的记录
    open(os.getcwd()+"\log\\vulns.txt", 'w+')
    open(os.getcwd()+"\log\\logs.txt", 'w+')
    time.sleep(1)
    get_vulnlog()

start_log()
