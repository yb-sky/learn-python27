#!/usr/bin/python
#-*-coding:utf-8-*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import itchat



def send_msg(wechat_name,wechat_msg):
    friends = itchat.search_friends(name=wechat_name)
    print friends
    # [ < User: {u'UserName': u'@096a9f783a31c9841bf86649f5c0b32009274d6c72a25bc830074cb4470a0f2c',
    #            u'City': u'\u957f\u6c99', u'DisplayName': u'', u'UniFriend': 0, 'MemberList'
    #            : < ContactList: [] >, u'PYQuanPin': u'bluesky', u'RemarkPYInitial': u'', u'Uin': 0, u'AppAccountFlag': 0, u'VerifyFlag': 0, u'Province': u'\u6e56\u5357', u'KeyWord': u'', u'RemarkName': u'', u'PYInitial': u'BLUESKY', u'ChatRoomId': 0, u'IsOwner': 0, u'HideInputBarFlag': 0, u'EncryChatRoomId': u'', u'AttrStatus': 4133, u'SnsFlag': 0, u'MemberCount': 0, u'OwnerUin': 0, u'Alias': u'', u'Signature': u'\u7f16\u7a0b\u4eba\u751f', u'ContactFlag': 3, u'NickName': u'bluesky', u'RemarkPYQuanPin': u'', u'HeadImgUrl': u'/cgi-bin/mmwebwx-bin/webwxgeticon?seq=684439675&username=@096a9f783a31c9841bf86649f5c0b32009274d6c72a25bc830074cb4470a0f2c&skey=@crypt_14f1eacd_1b1d125ec69711fa503362a530bb13ac', u'Sex': 1, u'StarFriend': 0, u'Statues': 0} >]

    try:
        user_name = friends[0]["UserName"]
        print user_name
        itchat.send('Hello, filehelper', toUserName='filehelper')
        itchat.send_msg(wechat_msg, toUserName=user_name)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    send_msg( "bluesky", "hello, it come from itchat roboot")