# import gevent
# from gevent import monkey
#
import time


#
#
# monkey.patch_all()


def sing():
    for i in range(5):
        print('sing%d' % i)
        time.sleep(0.5)
        yield i


def dance():
    for i in range(5):
        print('dance%d' % i)
        time.sleep(0.5)
        yield i


# 猜测协程的实现原理是这种形式
if __name__ == '__main__':
    s = sing()
    d = dance()
    while True:
        a = next(s)
        print(a)
        b = next(d)
        print(b)
        if a is None and b is None:
            break
