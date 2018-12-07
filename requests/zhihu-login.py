#!/usr/bin/python
#-*-coding:utf-8-*-

import requests
import sys
reload(sys)
try:
    import cookielib
except:
    import http.cookiejar as cookielib

sys.setdefaultencoding('utf-8')

'''
模拟浏览器登陆知乎，实现流程
分析知乎登陆关键的信息：
    登录的 URL 地址是 https://www.zhihu.com/login/email
    登录需要提供的表单数据有4个：用户名（email）、密码（password）、验证码（captcha）、_xsrf。
    获取验证码的URL地址是 https://www.zhihu.com/captcha.gif?r=1490690391695&type=login

1. 登录时所依赖的两个第三方库是 requests 和 BeautifulSoup
    pip install beautifulsoup4
    pip install requests
2. 
'''

class zhihuLogin:
    agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
    headers = {'User-Agent': agent}

    def __init__(self,url='https://www.zhihu.com/login/email'):
        # 使用登录cookie信息
        self.session = requests.Session()
        self.session.cookies = cookielib.lwp_cookie_str(filename='cookies')
        try:
            self.session.cookies.load(ignore_discard = True)
        except:
            print('Cookie 未加载')

if __name__ == '__main__':
    zhihuLogin = zhihuLogin()
