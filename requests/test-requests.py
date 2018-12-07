#!/usr/bin/python
#-*-coding:utf-8-*-

import requests

'''
requests 的作者是 Kenneth Reitz 大神
功能包括 Keep-Alive、连接池、Cookie持久化、内容自动解压、HTTP代理、SSL认证、连接超时、Session等很多特性，
最重要的是它同时兼容 python2 和 python3。
requests 的安装可以直接使用 pip 方法：pip install requests
'''

# GET 请求
response = requests.get("https://foofish.net")

# 状态码
print("状态码: %d" % response.status_code)

# 原因短语
print("原因短语: %s" % response.reason)

# 响应首部
print("响应首部\n: ")
for name,value in response.headers.items():
    print("%s:%s" % (name,value))

# 响应内容
print("响应内容\n: ")
print(response.content)


'''
request支持的方法：包括 POST、PUT、DELTET、HEADT、OPTIONS方法
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
'''

url = "http://fav.foofish.net"

# 查询参数
args = {"p": 4, "s": 20}
response = requests.get("http://fav.foofish.net", params = args)
print(response.url)

# 请求首部
r = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})

# 请求体
    # 请求体表单模式：data
    # 请求体json模式：json
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)

# 响应内容,响应体相关的属性有：content、text、json()

# content 是 byte 类型，适合直接将内容保存到文件系统或者传输到网络中
r = requests.get("https://pic1.zhimg.com/v2-2e92ebadb4a967829dcd7d05908ccab0_b.jpg")
type(r.content)
# 另存为 test.jpg
with open("test.jpg", "wb") as f:
    f.write(r.content)

# text 是 str 类型，比如一个普通的 HTML 页面，需要对文本进一步分析时，使用 text。
r = requests.get("https://foofish.net/understand-http.html")
type(r.text)
r.compile('xxx').findall(r.text)

#json
r = requests.get('https://www.v2ex.com/api/topics/hot.json')
r.json()

# 代理设置
proxies = {
  'http': 'socks5://127.0.0.1:1080',
  'https': 'socks5://127.0.0.1:1080',
}
requests.get('https://foofish.net', proxies=proxies, timeout=5)

# 超时设置,给每个请求显示地指定一个超时时间
r = requests.get("http://www.google.coma", timeout=5)



# 会话：Session，为了维持客户端与服务器之间的通信状态，使用 Cookie 技术使之保持双方的通信状态
# 构建一个session会话之后，客户端第一次发起请求登录账户，服务器自动把cookie信息保存在session对象中，
# 发起第二次请求时requests 自动把session中的cookie信息发送给服务器，使之保持通信状态

# 构建会话
session  = requests.Session()
#　登录url
session.post(login_url, data={username, password})
#　登录后才能访问的url
r = session.get(home_url)
session.close()

'''
参考：
    1. https://foofish.net/http-requests.html
    2. requests文档：http://docs.python-requests.org/en/master/
    3. Python实现知乎自动登录：https://foofish.net/python-auto-login-zhihu.html

'''