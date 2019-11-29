import threading
import time

g_num = 0
lock = threading.Lock()
lock2 = threading.Lock()

def sum1():
    global g_num
    for _ in range(100000):
        lock.acquire()
        print(threading.current_thread().name, '加1')
        g_num += 1
        lock.release()
        time.sleep(1)
    print(threading.current_thread().name, 'gum', g_num)


def sum2():
    global g_num
    for _ in range(100000):
        lock.acquire()
        print(threading.current_thread().name, '加1')
        g_num += 1
        lock.release()
        time.sleep(1)

    print(threading.current_thread().name, 'gum', g_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=sum1)
    t2 = threading.Thread(target=sum2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('main', g_num)
