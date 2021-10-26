# 扫完之后邮件提醒
# 以后再加进去，目前版本没有这个功能...加进去也不是啥难事，师傅们可以自己改一下
# 不用server酱的原因是..她收费，邮箱提醒免费

import os
import time
import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def sendEmail(add_jilu):
    host_server = 'smtp.qq.com'  # qq邮箱smtp服务器
    sender_qq = '1046141213@qq.com'  # 发件人邮箱
    pwd = ''# smtp密钥
    receiver = ['1046141213@qq.com']  # 收件人邮箱
    mail_title = '漏洞扫描提醒'  # 邮件标题，（标题可自由修改）
    mail_content = add_jilu  # 邮件正文内容
    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    msg['To'] = ";".join(receiver)
    # 邮件正文内容
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    smtp = SMTP_SSL(host_server)  # ssl登录
    smtp.login(sender_qq, pwd)
    smtp.sendmail(sender_qq, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    sendEmail("test")