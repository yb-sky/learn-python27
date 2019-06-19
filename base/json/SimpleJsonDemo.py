#!/usr/bin/python
#-*-coding:utf-8-*-

'''
第三方json库安装使用
SimpleJson是第三方json库，https://simplejson.readthedocs.io/en/latest/
下载：https://files.pythonhosted.org/packages/dc/c2/8c2db4cd1265913c59b6c204a6066f856802ed1911a6238f95d03ae4367b/simplejson-3.15.0-cp27-cp27m-win_amd64.whl
安装：pip install 上面文件

Created on 2018年6月27日
@author: SkyOne
'''

# import simplejson as json
import json
#
# res = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# print res
# # ["foo", {"bar": ["baz", null, 1.0, 2]}]
#
# res = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
# print res
# # {"a": 0, "b": 0, "c": 0}
#
# # 格式化输出
# print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4 * ' '))
# # {
# #     "4": 5,
# #     "6": 7
# # }
#

print('hello,%d' % 1)

j_data = json.loads('{"meta":{"success":true,"code":0,"message":"操作成功","enMessage":"ok"},"data":[{"id":-1,"name":"全球畅销","url":"http://obj.auto-learning.com/96b3f723-b11a-4092-b60e-cb7e0af2a8ae","isSplit":1},{"id":1,"name":"文学","url":"http://obj.auto-learning.com/092cf87e-01da-463f-bf98-8a5630cf603e","isSplit":1},{"id":6,"name":"历史","url":"http://obj.auto-learning.com/24bdb983-e77b-4350-a4ce-5e43790c2e07","isSplit":1},{"id":4,"name":"科普","url":"http://obj.auto-learning.com/5590c1f8-a495-44b9-bcf6-4ed8c8948b8d","isSplit":1},{"id":8,"name":"商业街","url":"http://obj.auto-learning.com/0bafee24-468a-45a5-a8ee-0d7d9e41de83","isSplit":1},{"id":3,"name":"思想库","url":"http://obj.auto-learning.com/a68e0d91-7be1-449e-b8bf-a9fd19882b1b","isSplit":1},{"id":13,"name":"亲子","url":"http://obj.auto-learning.com/855a9abe-a8d7-496c-b347-67f5a27f201f","isSplit":1}]}')
for key in j_data['data']:
    name = key['name']
    url = key['url']
    id = key['id']
    print name, url,id

    path = 'https://api.auto-learning.com/v3/xcx/search?nationId=0&typeId=%d&pageIndex=0&isAsc=0&isRead=0' % id

def dict_to_json():
    data = dict()
    data["code"]="123"
    data["name"] = "test"
    print json.dumps(data, ensure_ascii=False)
dict_to_json()