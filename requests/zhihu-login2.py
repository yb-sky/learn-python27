#!/usr/bin/python
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
from PIL import Image
import requests
import json,os

class zhihuspider:
    IndexUrl = "http://www.zhihu.com"
    LoginUrl = "http://www.zhihu.com/login/email"
    captchaUrl = 'http://www.zhihu.com/captcha.gif'
    cookies_file = './zhihuCookies.data'

    postData={
            'email':'*****',#email账户
            'remember_me':"true",
            'password':'*****', #密码
            'phone_num' : '18973017693'
    }

    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Host": "www.zhihu.com",
        "Upgrade-Insecure-Requests": "1",
        }

    def login(self):
        session = self.__session
        print(session.get(self.IndexUrl).content)
        xsrf = BeautifulSoup(session.get(self.IndexUrl).content,'html.parser').find("input",{"name":'_xsrf'})['value']
        self.postData['_xsrf'] = xsrf
        captcha =session.get(self.captchaUrl,stream = True).content
        with open('./images/captcha.gif', "wb") as output:
            output.write(captcha)
        Image.open('./images/captcha.gif').show()
        captcha = input("请输入验证码：")
        self.postData['captcha'] = captcha

        response = session.post(self.LoginUrl, self.postData, self.headers)
        print("msg:",response.json()['msg'])

        self.saveCookies(session.cookies)

    def getFollowees(self):
        session = self.__session
        userUrl = 'https://www.zhihu.com/people/ling-long-xie-seng/followees'
        session = self.__session
        response = session.get(userUrl).content
        soup = BeautifulSoup(response,'html.parser')
        print(soup.title.string)

    def saveCookies(self,cookies):
        with open(self.cookies_file, "w") as output:
            self.zhihuCookie = cookies.get_dict()
            json.dump(self.zhihuCookie,output)

    def loadCookies(self):
        if os.path.exists(self.cookies_file):
            with open(self.cookies_file,'r') as cookies_input:
                zhihuCookies = json.load(cookies_input)
                return zhihuCookies
        else:
            return None

    def __init__(self):
        self.__session = requests.session()
        self.__session.headers = self.headers
        self.zhihuCookie = self.loadCookies()

        if self.zhihuCookie:
            self.__session.cookies.update(self.zhihuCookie)
            self.getFollowees()
        else:
            self.login()

if __name__ == '__main__':
    spider = zhihuspider()
