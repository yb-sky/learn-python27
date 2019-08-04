#!/usr/bin/python
# -*-coding:utf-8-*-

# 163 smtp群发邮件

import smtplib
from email.header import Header
from email.mime.text import MIMEText

# smtp服务器
mail_host = "smtp.163.com"
mail_user = "" # 用户名
mail_pass = ""

sender = "" # 发件人邮件
receives = ['']

content = "全国城市投资潜力排行榜"
title = "吴伯凡认知方法论"


def send_mail():
    message = MIMEText(content, 'plain', 'utf-8')  # 内容 格式 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receives)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信
        smtpObj.login(mail_user, mail_pass)  # 登陆验证
        smtpObj.sendmail(sender, receives, message.as_string())  # 发送邮件
        print("Mail has been send successfully.")
    except smtplib.SMTPException as e:
        print('异常\n', e)


def send_mail_non_ssl():
    email_client = smtplib.SMTP(mail_host)
    email_client.login(mail_user, mail_pass)

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(title, 'utf-8')
    msg['From'] = sender
    msg['To'] = receives
    email_client.sendmail(sender, receives, msg.as_string())
    email_client.quit()


if __name__ == '__main__':
    send_mail()
