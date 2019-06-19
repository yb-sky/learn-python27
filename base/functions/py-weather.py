#!/usr/bin/python
#-*-coding:utf-8-*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests


def parse_character(url, params):
    req = requests.get(url, params=params)
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding

        # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        global encode_content
        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
        return encode_content

def get_weather(location):
    url = 'https://api.thinkpage.cn/v3/weather/daily.json'
    payload = {
        'days': 1,
        'key': 'lrtff1fcg9yym1bp',
        'location': location,
    }
    try:
        res = requests.get(url, params=payload)
        weather = res.json()['results'][0]['daily'][0]
        # print(weather)

    except:
        return
    data = "%s 今日天气\n%s  \t%s℃~%s℃" % (location, str(weather['text_day']), str(weather['low']), str(weather['high']))
    # if '雨' in weather['text_day']:
    #     data += '\n\n今天有雨，记得带伞啊。'
    data += '\n来自小机器人的温馨提示。'
    return data

if __name__ == '__main__':
    print get_weather("长沙")