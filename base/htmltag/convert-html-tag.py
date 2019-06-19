#!/usr/bin/python
# -*-coding:utf-8-*-

import HTMLParser
import cgi

def html_tag_convert(str):
    print str
    html_parser = HTMLParser.HTMLParser()
    txt = html_parser.unescape(str) #这样就得到了txt = '<abc>'
    print txt

    html = cgi.escape(txt) # 这样又回到了 html = '&lt;abc&gt'
    print html

def do_test():
    # html = '&lt;abc&gt;'
    html = u''' &lt;div&gt;1945年英国议会通过了大英银行国有化法案，建立了英国史上第一个国家银行；1946年政府将800家公司收归国有；1947年政府在电力、航空、电讯、航运等企业部门推行国有化。这表明&amp;nbsp;&amp;nbsp;&amp;nbsp;（&amp;nbsp;&amp;nbsp;&amp;nbsp;）&lt;/div&gt;'''
    html_tag_convert(html)

do_test()