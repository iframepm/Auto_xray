import re
import subprocess
def sh(command, print_msg=True):
    global lj
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = []
    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('gbk')
        if print_msg:
            print(">>>", line)
            if "The subdomain result for" in line:
                global lj #csv路径
                lj=re.findall('(?::\s)(.+)',line)[0]
                print(lj)  #输出csv路径
            else:
                try:
                    if lj!="":
                        pass
                    else:
                        lj=""
                except:
                    pass
                pass
        lines.append(line)
    return lines,lj


if __name__ == '__main__':
    sh("python E:\OneForAll-master\oneforall.py --target {0} run".format(input('[INPUT] 请输入主域名：')))