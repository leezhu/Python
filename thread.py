#encoding=utf-8
#describe:python线程练习
#time:20160603
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(3)
            msg = "I`m"+self.name +'@'+str(i)
            print msg

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__'
    test()
