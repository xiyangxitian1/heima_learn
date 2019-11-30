import gevent
import time


def foo(n):
    for i in range(10):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(foo, 3)
    g2 = gevent.spawn(foo, 4)
    g2.name = 'gevent2'
    g1.join()
    g2.join()
