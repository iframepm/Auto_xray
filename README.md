# Auto_xray
xray多线程批量扫描工具
# 简介
![image](https://z3.ax1x.com/2021/10/26/55XwCj.png)
** xray社区版貌似没有批量扫描，这就让安服仔使用起来很不方便，扫站得一个个手动添加，非常难受。**

选项1：oneforall+xray 输入一个主域名，自动采集子域名然后添加到xray任务列表里。

选项2：导入一个txt，直接用xray批量扫

选项3：输入主域名，只采集子域名，不扫

# 说明
1. 扫描结果会在.\result文件夹里，文件名就是目标站点域名。

2. oneforall结果在其.\oneforall\result根目录下

3. \log\vuluns.txt中存储上次漏洞记录

4. 漏洞扫描结果会实时显示在监控终端中。

## 演示

![image](https://z3.ax1x.com/2021/10/26/5Ig9w6.gif)
