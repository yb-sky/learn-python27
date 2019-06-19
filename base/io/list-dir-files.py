#!/usr/bin/python
#encoding=utf-8
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from chardet import detect  # detect(str),参数只能是str,不能是unicode编码的

def list_files(path):
    import os
    for child in os.listdir(path):
        childPath = os.path.join(path, child)
        if os.path.isdir(childPath):
            list_files(childPath)
        else:
            # print childPath
            # print codecs.open(childPath, 'rb', 'gb18030')
            # print os.popen(childPath).read()


            if not isinstance(childPath, unicode):
                line = childPath.decode(detect(childPath)['encoding']).rstrip().lower()
                print line
            else:
                print 'not parser: %s' % childPath


list_files('D:\Data\jilin')
