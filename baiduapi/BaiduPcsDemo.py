#!/usr/bin/python
#-*-coding:utf-8-*-

from baidupcs import PCS

class BaiduPcsDemo:
    def test(self):
        pcs = PCS('access_token')
        response = pcs.info()
        print(response)
        if response.status_code == 200:
            print(response.content)

if __name__ == '__main__':

    obj = BaiduPcsDemo()
    obj.test()
