import gevent
from gevent import monkey


def dance():
    for _ in range(10):
        print('跳舞')
        gevent.sleep(1)
        # yield


def sing():
    for _ in range(10):
        print('唱歌')
        gevent.sleep(1)
        # yield


if __name__ == '__main__':
    g1 = gevent.spawn(dance)
    g2 = gevent.spawn(sing)
    g1.join()
    g2.join()
