#!/usr/bin/python
#-*-coding:utf-8-*-

# SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式
# smtplib.SMTP( [host [, port [, local_hostname]]] )
# host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如: runoob.com，这个是可选参数。
# port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下 SMTP 端口号为25。
# local_hostname: 如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可

import smtplib
import pdb
from email.mime.text import MIMEText
from email.header import Header

''''' 
邮件发送操作工具类
Created on 2018年6月27日  
@author: SkyOne 
'''

class SemdMail:

    # 第三方 SMTP 服务
    __mail_host = "smtp.163.com"  # 设置服务器
    __mail_user = "yeaskyone@163.com"  # 用户名
    __mail_pass = ""  # 口令

    def __init__(self,sender,receivers,content,title):
        self.sender = sender
        self.receivers = receivers
        self.content = content
        self.title = title

        msgBody = self.constuctMsgBody(self.sender,self.receivers,self.content,self.title)
        self.sendMail(msgBody)

    # 构造消息体
    def constuctMsgBody(self,sender,receivers,content,title):
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header(sender, 'utf-8')
        message['To'] = ";".join(receivers)
        message['Subject'] = Header(title, 'utf-8')
        print("receivers: %s" % message.as_string())
        return message

    def sendMail(self,body):
        server = None
        try:
            # 断点
            # pdb.set_trace()
            server = smtplib.SMTP()
            server.connect(self.__mail_host, 25)
            server.login(self.__mail_user, self.__mail_pass)
            server.sendmail(self.sender, self.receivers, body.as_string())
            # server.close()
            print 'Send mail success.'
        except smtplib.SMTPException, e:
            print("Error: ", e)
        finally:
            server.quit()



sender = 'yeaskyone@163.com'
receivers = ['yuanbingkun14307@talkweb.com.cn','yeaskyone@126.com']
content = "欢迎使用悦听小程序，悦听小程序集合了当前各大付费平台音频，采用重酬方式，以廉价的服务为您提供最前沿的知识和思维升级"
title = "听知识，就来悦听小程序！"
mail = SemdMail(sender,receivers,content,title)



