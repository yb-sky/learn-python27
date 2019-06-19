#!/usr/bin/python
#-*-coding:utf-8-*-

# 线程同步
# 使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，
# 对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间


import threading
import time

exitFlag = 0

class myThread(threading.Thread): #继承父类threading.Thread
    def __init__(self,theadId,name,counter):
        threading.Thread.__init__(self)
        self.theadId = theadId
        self.name = name
        self.counter = counter

    # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        print "Starting "+self.name
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        self.print_time(self.name, self.counter,5)
        # 释放锁
        threadLock.release()
        print "Exiting " + self.name

    def print_time(self,name,delay,counter):
        while counter:
            time.sleep(delay)
            print "%s: %s" % (name,time.ctime(time.time()))
            counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, 'thread-1',1)
thread2 = myThread(2, 'thread-2',2)

# 开启线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 添加线程到线程列表
for t in threads:
    t.join()

print "Exiting Main Thread"
print "\r\n"