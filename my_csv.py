# -!- coding: utf-8 -!-
import csv
import os
def load_csv(dizhi):
    with open(dizhi) as f:
        reader = csv.reader(f)
        column=[row[4] for row in  reader]
        del (column[0])
        print(column[::2])
        print("子域名条数："+str(len(column[::2])))
        for url in column[::2]:
            print(url)
        print("子域名条数：" + str(len(column[::2])))
        f=open("./domain.txt","w+")
        for lines in column[::2]:
            f.write(lines+"\n")
        print("导出的txt路径："+os.getcwd()+"\domain.txt")
