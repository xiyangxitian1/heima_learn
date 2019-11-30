import gevent
import time
from gevent import monkey

monkey.patch_all()


def sing(n):
    for i in range(n):
        print('sing', i)
        time.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(sing, 5)
    g1.join()


