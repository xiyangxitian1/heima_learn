import threading
import time


def foo():
    for _ in range(10):
        time.sleep(20)


if __name__ == '__main__':

    for __ in range(10):
        threading.Thread(target=foo).start()

    print('线程数量：', len(threading.enumerate()))
    # for i, name in threading.enumerate():
    #     print(i, name)
