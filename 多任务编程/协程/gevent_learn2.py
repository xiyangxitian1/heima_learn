import gevent
from gevent import monkey

import time


monkey.patch_all()


def sing():
    for i in range(5):
        print('sing%d' % i)
        time.sleep(0.5)
        # gevent.sleep(1)


def dance():
    for i in range(5):
        print('dance%d' % i)
        time.sleep(0.5)
        # gevent.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dance)

    # g2.join()
    g1.join()
    gevent.joinall([g1, g2])
