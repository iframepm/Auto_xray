# -!- coding: utf-8 -!-
import re
import subprocess
import os
from colorama import init,Fore,Back,Style
init(autoreset=True)
def sh(command, print_msg=True):
    VulnType=[] #漏洞类型存在这里
    Target=[] #漏洞站点存在这里
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = []
    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('utf-8')
        if print_msg:
            print(">>>", line)
            if "[Vuln:" in line:
                Target.append(line)
            elif "Target" in line:
                Target.append(line)
            elif "VulnType" in line:
                Target.append(line)
            else:
                pass
        lines.append(line)
        #如果line里面的记录不是空的则写入到文件
    for vuln in Target:
        w = open(os.getcwd()+"\log\\vulns.txt", 'a+')  # 存储漏洞信息的txt
        w.write(vuln+"\n")
    return lines


if __name__ == '__main__':
    sh('xray.exe webscan {0} --html-output wwwwwwwwwww.html --basic-crawler'.format(input("网站：")))