import threading
#  和进程不同，主进程结束了，守护进程就不运行了
#  线程是主线程结束的时候，有非守护线程还在运行，那么守护线程还是要执行
import time


def foo():
    for i in range(10):
        print(threading.current_thread().name, i)
        time.sleep(1)


if __name__ == '__main__':
    t = threading.Thread(target=foo, name='守护线程')
    t.setDaemon(True)
    t.start()
    t1 = threading.Thread(target=foo)
    # p.daemon = True
    t1.start()

    time.sleep(5)
    print('主线程结束')
    exit()
    print('主线程结束aaaaaaaaaaaaaa')

    # 进程1执行了5次   进程2执行了10次
