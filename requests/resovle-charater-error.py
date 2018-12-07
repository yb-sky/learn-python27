#!/usr/bin/python
#-*-coding:utf-8-*-
import requests

req = requests.get("http://www.lushishi30.com/")

if req.encoding == 'ISO-8859-1':
    encodings = requests.utils.get_encodings_from_content(req.text)
    if encodings:
        encoding = encodings[0]
    else:
        encoding = req.apparent_encoding

    # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    global encode_content
    encode_content = req.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符；


print(encode_content)

with open('test.html', 'w') as f:
    f.write(encode_content.encode('utf-8'))