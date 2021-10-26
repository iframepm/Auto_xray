import os
import re
import threading
import my_xray
import my_email
import subprocess

#真正的扫描函数
def do_scan(targeturl,outputfilename):
    scan_command="xray.exe webscan --basic-crawler {} --html-output .\\result\{}.html".format(targeturl,outputfilename)
    my_xray.sh(scan_command)
    #记录进度函数,每扫完一条就写一行
    q = open(os.getcwd()+"/log/logs.txt",'a')
    q.write(targeturl+"\n")
    q.close()
    return

#多线程实时读取进度,打开一个新窗口来监控进度
def start_log():
    subprocess.call("start /wait python "+os.getcwd()+"/jiankon.py", shell=True)


def get_url(lines):
    pattern = re.compile(r'^(https|http)://')
    for line in lines:
        try:
            if not pattern.match(line.strip()):
                targeturl="http://"+line.strip()
            else:
                targeturl=line.strip()
                filename=re.sub("(:)", "D", re.findall("(?:http://|https://)([^/]+)",targeturl)[0])
            do_scan(targeturl.strip(), filename)
        except Exception as e:
            pass
    print("[INFO] ---------Scan End-------------- ")
    return
#启动扫描
def scan(txt):
    if "domain.txt" in txt:
        XC = 10 #默认10线程
        f = open(txt, encoding='gbk')
    else:
        XC = int(input("[INPUT] 请输入线程数："))
        f = open(input("[INPUT] 输入txt："), encoding='gbk')
    lines = f.readlines()
    x=open(os.getcwd() + "\\result.txt",'w+', encoding='gbk')
    for line1 in lines:
        x.write(line1)
    x.close()
    print('[INFO] 一共'+str(len(lines))+'行')
    leng=len(lines)
    print("[INFO] 能分成"+str(leng//XC)+"份")
    print('[INFO] 余'+str(leng%XC)+'行')
    shuzu=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    yushu=[]
    #多线程启动监控函数
    threading.Thread(target=start_log).start()
    for i in range((leng//XC)):
        for h in range(XC):
            shuzu[i].append(lines[i*XC+h].strip())
        print(shuzu[i])
        threading.Thread(target=get_url, args=(shuzu[i],)).start()

    for k in  range(leng%XC):
        yushu.append(lines[len(lines)-1-k].strip())
    #这个地方有个bug，当网站数量被线程数量整除的时候，他就会直接跳过这个函数，因为这个函数是用来处理无法被线程数整除的站点的。
    get_url(yushu)
    #扫描结束之后发邮件提醒！'
    #my_email.sendEmail('扫描结束')

if __name__ == '__main__':
    scan()


