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
    g1 = None
    g2 = None
    if g1 is None:
        for i in range(5):
            print("g1:", i)
            g1 = gevent.spawn(sing, i)
            break
    if not g2:
        for i in range(5):
            print('g2:', i)
            g2 = gevent.spawn(dance, i)
            break

    # g2.join()
    gevent.joinall([g1, g2])
