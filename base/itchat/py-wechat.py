#!/usr/bin/python
# -*-coding:utf-8-*-

"""
itchat: https://itchat.readthedocs.io/zh/latest/
itchat是一个开源的微信个人号接口，使用python调用微信从未如此简单。
使用不到三十行的代码，你就可以完成一个能够处理所有信息的微信机器人。
当然，该api的使用远不止一个机器人，更多的功能等着你来发现，比如这些。
该接口与公众号接口itchatmp共享类似的操作方式，学习一次掌握两个工具。
如今微信已经成为了个人社交的很大一部分，希望这个项目能够帮助你扩展你的个人的微信号、方便自己的生活。
"""

import itchat

def do_send_msg_to_file_assistant():
    # 发消息给文件助手
    itchat.send('Hello, filehelper', toUserName='filehelper')
    # 发消息给朋友
    itchat.send('Hello, bluesky', toUserName='kids-code')

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

if __name__ == '__main__':
    itchat.auto_login()
    do_send_msg_to_file_assistant()