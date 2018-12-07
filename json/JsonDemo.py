#!/usr/bin/python
#-*-coding:utf-8-*-

# JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。

# 使用 JSON 函数需要导入 json 库：import json
# 函数	                描述
# json.dumps	将 Python 对象编码成 JSON 字符串
# json.loads	将已编码的 JSON 字符串解码为 Python 对象

import json
# import simplejson
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# print help(json)

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

# 简单输出
json.dumps(data)
# 格式化输出
jsonData1 = json.dumps(data, sort_keys=True, indent=4, separators=(',',':'))
# print jsonData1

jsonData1 = json.dumps(data, sort_keys=True)
# print jsonData1

# son.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(jsonData)
print text['a']

str = '{"province":{"1":{"id":"1","name":"北京市","upid":"0","level":"1","pinyin":"beijing","shortname":"京"},"2":{"id":"2","name":"天津市","upid":"0","level":"1","pinyin":"tianjin","shortname":"津"},"3":{"id":"3","name":"河北省","upid":"0","level":"1","pinyin":"hebei","shortname":"冀"},"4":{"id":"4","name":"山西省","upid":"0","level":"1","pinyin":"shanxi","shortname":"晋"},"5":{"id":"5","name":"内蒙古","upid":"0","level":"1","pinyin":"neimenggu","shortname":"蒙"},"6":{"id":"6","name":"辽宁省","upid":"0","level":"1","pinyin":"liaoning","shortname":"辽"},"7":{"id":"7","name":"吉林省","upid":"0","level":"1","pinyin":"jilin","shortname":"吉"},"8":{"id":"8","name":"黑龙江","upid":"0","level":"1","pinyin":"heilongjiang","shortname":"黑"},"9":{"id":"9","name":"上海市","upid":"0","level":"1","pinyin":"shanghai","shortname":"沪"},"10":{"id":"10","name":"江苏省","upid":"0","level":"1","pinyin":"jiangsu","shortname":"苏"},"11":{"id":"11","name":"浙江省","upid":"0","level":"1","pinyin":"zhejiang","shortname":"浙"},"12":{"id":"12","name":"安徽省","upid":"0","level":"1","pinyin":"anhui","shortname":"皖"},"13":{"id":"13","name":"福建省","upid":"0","level":"1","pinyin":"fujian","shortname":"闽"},"14":{"id":"14","name":"江西省","upid":"0","level":"1","pinyin":"jiangxi","shortname":"赣"},"15":{"id":"15","name":"山东省","upid":"0","level":"1","pinyin":"shandong","shortname":"鲁"},"16":{"id":"16","name":"河南省","upid":"0","level":"1","pinyin":"henan","shortname":"豫"},"17":{"id":"17","name":"湖北省","upid":"0","level":"1","pinyin":"hubei","shortname":"鄂"},"18":{"id":"18","name":"湖南省","upid":"0","level":"1","pinyin":"hunan","shortname":"湘"},"19":{"id":"19","name":"广东省","upid":"0","level":"1","pinyin":"guangdong","shortname":"粤"},"20":{"id":"20","name":"广西","upid":"0","level":"1","pinyin":"guangxi","shortname":"桂"},"21":{"id":"21","name":"海南省","upid":"0","level":"1","pinyin":"hainan","shortname":"琼"},"22":{"id":"22","name":"重庆市","upid":"0","level":"1","pinyin":"chongqin","shortname":"渝"},"23":{"id":"23","name":"四川省","upid":"0","level":"1","pinyin":"sichuan","shortname":"川"},"24":{"id":"24","name":"贵州省","upid":"0","level":"1","pinyin":"guizhou","shortname":"黔"},"25":{"id":"25","name":"云南省","upid":"0","level":"1","pinyin":"yunnan","shortname":"滇"},"26":{"id":"26","name":"西藏","upid":"0","level":"1","pinyin":"xizang","shortname":"藏"},"27":{"id":"27","name":"陕西省","upid":"0","level":"1","pinyin":"shxi","shortname":"陕"},"28":{"id":"28","name":"甘肃省","upid":"0","level":"1","pinyin":"gansu","shortname":"甘"},"29":{"id":"29","name":"青海省","upid":"0","level":"1","pinyin":"qinghai","shortname":"青"},"30":{"id":"30","name":"宁夏","upid":"0","level":"1","pinyin":"ningxia","shortname":"宁"},"31":{"id":"31","name":"新疆","upid":"0","level":"1","pinyin":"xinjiang","shortname":"疆"},"32":{"id":"32","name":"台湾","upid":"0","level":"1","pinyin":"taiwang","shortname":"台"},"33":{"id":"33","name":"香港","upid":"0","level":"1","pinyin":"xianggang","shortname":"港 "},"34":{"id":"34","name":"澳门","upid":"0","level":"1","pinyin":"aomen","shortname":"澳"},"35":{"id":"35","name":"海外","upid":"0","level":"1","pinyin":"haiwai","shortname":"外"},"36":{"id":"36","name":"其他","upid":"0","level":"1","pinyin":"qita","shortname":"他"}},"types":{"7":"中考模拟","8":"中考真卷"},"years":{"2018":"2018","2017":2017,"2016":2016,"2015":2015,"2014":2014,"2013":2013,"2012":2012,"2011":2011,"2010":2010,"2009":2009},"terms":[{"pid":"16","name":"七年级上学期"},{"pid":"17","name":"七年级下学期"},{"pid":"18","name":"八年级上学期"},{"pid":"19","name":"八年级下学期"},{"pid":"20","name":"九年级上学期"},{"pid":"21","name":"九年级下学期"},{"pid":"22","name":"中考阶段"},{"pid":"14","name":"六年级上学期"},{"pid":"15","name":"六年级下学期"}]}'
text = json.loads(str)
print type(text)
for row in text:
    print row

print text['province']['1']
